"""
This script opens and parses through CSV files containing various measurements. Additional parameters are calculated and all relevant parameters are written to one CSV file. 

Collected parameters from file M2 are:
- atmospheric pressure
- air temperature
- wind speed
- wind direction
- wave height
- wave period

Collected parameters from file Dublin Airport are:
- precipitation

Collected parameters from file Dublin Tide gauge are:
- date & time
- actual tidal height

""" 
import csv
from datetime import datetime, timedelta
import ephem

######################################
## ------ MOON FUNCTION BEGIN------ ##
## CREDIT :: https://stackoverflow.com/questions/2526815/moon-lunar-phase-algorithm

def get_phase_on_day(date: datetime):
  """Returns a floating-point number from 0-1. where 0=new, 0.5=full, 1=new"""
  #Ephem stores its date numbers as floating points, which the following uses
  #to conveniently extract the percent time between one new moon and the next
  #This corresponds (somewhat roughly) to the phase of the moon.


  # using code from Ephem web page :: https://rhodesmill.org/pyephem/
  dublin = ephem.Observer()
  # lat lon taken from :: https://www.latlong.net/place/dublin-ireland-712.html
  dublin.lat = '53.35'
  dublin.lon = '-6.27'
  #Use Year, Month, Day as arguments
  date = ephem.Date(date)

  nnm = ephem.next_new_moon(date)
  pnm = ephem.previous_new_moon(date)
  lunation = (date-pnm)/(nnm-pnm) # NOTE 50% is a full moon. Although not intuitive, this allows us to see if we are trending towards or away from a full moon (to know if the moon is waxing or waning)

  #Note that there is a ephem.Moon().phase() command, but this returns the
  #percentage of the moon which is illuminated. This is not really what we want.

  return lunation
## ------ MOON FUNCTION END------ ##
####################################



# -----------------------------------------------------------------------------
#                               Gathering data
# -----------------------------------------------------------------------------

# Parsing M2 Buoy data
with open(r'C:\Users\melan\Desktop\COLLEGE\YR 4\Final Project\Data\m2_buoy_2001-2024_feb.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    atmo_pressure = []
    water_temp = []
    air_temp = []
    wind_speed = []
    wind_dir = []
    wave_height = []
    wave_period = []
    curr_time = datetime(2007, 3, 20, 7, 0, 0)
    
    next(reader, None)
    next(reader, None)
    
    for i, row in enumerate(reader): 
        date = datetime.strptime(row[4], '%Y-%m-%dT%H:%M:%SZ')
        
        if (date >= datetime(2007,3,20,7)):
            # If gauge is out of commission and data is missing, set data as 0
            while( date != curr_time):
                atmo_pressure.append(0)
                water_temp.append(0)
                air_temp.append(0)
                wind_speed.append(0)
                wind_dir.append(0)
                wave_height.append(0)
                wave_period.append(0)
                curr_time = curr_time + timedelta(hours=1)
            atmo_pressure.append(float(row[5]))
            water_temp.append(float(row[15]))
            air_temp.append(float(row[13]))
            wind_speed.append(float(row[7]))
            wind_dir.append(float(row[6]))
            wave_height.append(float(row[9]))
            wave_period.append(float(row[10]))
            curr_time = curr_time + timedelta(hours=1)
    
    csv_file.close()
    
# Parsing Dublin Airport data
with open(r'C:\Users\melan\Desktop\COLLEGE\YR 4\Final Project\Data\dublin_airport_1943-2024_feb.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    sea_pressure = []
    precipitation = []
    curr_time = datetime(2007, 3, 20, 7, 0, 0)
    
    # Skipping header and legend
    for i in range (24):
        next(reader, None)
        
    for i, row in enumerate(reader): 
        date = datetime.strptime(row[0], '%d/%m/%Y %H:%M')
        if (date >= datetime(2007,3,20,7)):
            # If gauge is out of commission and data is missing, set data as 0
            while( date != curr_time):
                sea_pressure.append(0)
                precipitation.append(0)
                curr_time = curr_time + timedelta(hours=1)
            sea_pressure.append(float(row[10]))
            precipitation.append(float(row[2]))
            curr_time = curr_time + timedelta(hours=1)
    csv_file.close()

# Parsing Dublin Port Gauge data
with open(r'C:\Users\melan\Desktop\COLLEGE\YR 4\Final Project\Data\dublin_port_tide_gauge_2007-2024_feb.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
   
    time = []
    act_height = []
    curr_time = datetime(2007, 3, 20, 7, 0, 0)
    moon = []    # Moon illumination is done in here so we dont have to parse through all time values again.
    
    # Skipping header rows
    next(reader, None)
    next(reader, None)
    
    for i, row in enumerate(reader): 
        date = datetime.strptime(row[0], '%Y-%m-%dT%H:%M:%SZ')
        if (date.minute == 0): # Only log readings at the beginning of an hour
            # If gauge is out of commission and data is missing, set data as 0
            while( date > curr_time):
                time.append(curr_time)
                act_height.append(0)
                moon.append(get_phase_on_day(curr_time))
                curr_time = curr_time + timedelta(hours=1)
            time.append(curr_time)
            act_height.append(float(row[7]))
            moon.append(get_phase_on_day(curr_time))
            curr_time = curr_time + timedelta(hours=1)
    csv_file.close()
        
# Parsing predicted tide height data
with open(r'C:\Users\melan\Desktop\COLLEGE\YR 4\Final Project\Data\predicted_tide_2000-2100.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    
    pred_height = []
    curr_time = datetime(2007, 3, 20, 7, 0, 0)
    
    # Skipping header rows
    next(reader, None)
    next(reader, None)

    for i, row in enumerate(reader): 
        date = datetime.strptime(row[0], '%m/%d/%Y %H:%M')
        if (date >= datetime(2007,3,20,7)):
            # If gauge is out of commission and data is missing, set data as 0
            while( date != curr_time):
                pred_height.append(0)
                curr_time = curr_time + timedelta(hours=1)
            pred_height.append(float(row[1]))
            curr_time = curr_time + timedelta(hours=1)
    csv_file.close()


with open(r'C:\Users\melan\Desktop\COLLEGE\YR 4\Final Project\Data\storms_2015-2024.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    
    storms = []
    curr_time = datetime(2007, 3, 20, 7, 0, 0)


    # Skipping header rows
    next(reader, None)
    for i, row in enumerate(reader): 
        start_date = datetime.strptime(row[0], '%d/%m/%Y')
        end_date = datetime.strptime(row[1], '%d/%m/%Y')
        
        # Fill in blank until next storm
        while( start_date > curr_time):
            storms.append('')
            curr_time = curr_time + timedelta(hours=1)
        # Fill in storm name until storm has passed
        while(end_date >= curr_time):
            storms.append(row[2])
            curr_time = curr_time + timedelta(hours=1)
    csv_file.close()



difference = []
serious_case = []
for act, pred in zip(act_height, pred_height):
    # Parameter 'diff' gives the difference such that a negative value indicates a smaller 
    # than predicted actual tide height around the normal and opposite for positive values.
    diff = abs(act) - abs(pred)  
    difference.append(diff)
    if (abs(act - pred) > serious):
        serious_case.append(True)
    else:
        serious_case.append(False)
    
        
with open('data\data.csv', 'w', newline='') as data:
    writer = csv.writer(data)
    writer.writerow(["Time", "Atmospheric Pressure", "Sea Pressure", "Precipitation", "Air Temperature", "Sea Temperature", "Wind Speed", "Wind Direction", "Wave Height", "Moon Illumination", "Predicted Tide Height", "Actual Tide Height", "Difference", "Serious", "Wave Period", "Storm"])
    for row in zip(time, atmo_pressure, sea_pressure, precipitation, air_temp, water_temp, wind_speed, wind_dir, wave_height, moon, pred_height, act_height, difference, serious_case, wave_period, storms):
        writer.writerow(row)
    csv_file.close()
    

