"""
This script contains all logic for the 'Jump-To' buttons, including 
storing and parsing through data.
"""


from tkinter import *
from datetime import datetime
from dateutil.relativedelta import relativedelta 
import numpy as np
class JumpToButtons():           
    def __init__(self, data):
        self.data = data
        self.state = True # Noting True means to calculate within the current year
        self.first_year = datetime.strptime(self.data[0][0], '%Y-%m-%d %H:%M:%S').year
        self.last_year = datetime.strptime(self.data[len(data)-1][0], '%Y-%m-%d %H:%M:%S').year
        tmp = []
        self.total=[]
        self.len=[0]
        curr_yr=int(self.first_year)
        # Creating a list of data for a given year and appending it 
        # to a list. This allows for easier navigation to yearly data
        # when finding max/min/etc within the year.
        for i in range (0, len(data)-1):
            if int(datetime.strptime(self.data[i][0], '%Y-%m-%d %H:%M:%S').year) == curr_yr:
                tmp.append(data[i])
            else:
                self.total.append(tmp)
                tmp = []
                curr_yr = curr_yr+1
                self.len.append(i+1) # +1 because i is the position of the FINAL sample of teh current year and we want array 'len' to hold the starting positions of each year (which is one position after the final position of the previous year)
        self.total.append(tmp)
    
    def toggleState(self):
        # Change the state. Called to when toggle button is pressed.
        self.state = not self.state
    
    def get_year(self, date):
        # Returns the currently selected year as the differencce between it and the first year.
        year = int(datetime.strptime(self.data[date][0], '%Y-%m-%d %H:%M:%S').year)
        return year - int(self.first_year)
    
    def total_position(self, year, pos_in_yr):
        if self.state:
            return self.len[year] + pos_in_yr
        else:
            return pos_in_yr
        
    def hottest(self, date):
        # Returns the date of highest temperature.
        if self.state:
            pos = self.get_year(date)
            data = self.total[pos] # Set data to only data from that year
        else:
            pos=0
            data=self.data # Use all data
        max_pos = 0
        max_val = float(data[0][4])
        for i, entry in enumerate(data):
            if (float(entry[4]) > max_val):
                max_pos = i
                max_val = float(entry[4])    
        return self.total_position(pos, max_pos)
    
    def coldest(self, date):
        # Returns the date of lowest temperature.
        if self.state:
            pos = self.get_year(date)
            data = self.total[pos]
        else:
            pos=0
            data=self.data
        min_pos = 0
        min_val = 100.0
        for i, entry in enumerate(data):
            if (float(entry[4]) != 0.0):
                # assume a reading of exactly 0.0 is reader shut down and skip
                if (float(entry[4]) < min_val):
                    min_pos = i
                    min_val = float(entry[4])
        return self.total_position(pos, min_pos)

    def lowpress(self, date):
        # Returns the date of lowest atmospheric pressure.
        if self.state:
            pos = self.get_year(date)
            data = self.total[pos]
        else:
            pos=0
            data=self.data
        min_pos = 0
        min_val =float(data[0][1])
        for i, entry in enumerate(data):
            if (float(entry[1]) != 0.0):
                if (float(entry[1]) < min_val):
                    min_pos = i
                    min_val = float(entry[1])
        return self.total_position(pos, min_pos)
    
    def rainy(self, date):
        # Returns the date of highest precipitation.
        if self.state:
            pos = self.get_year(date)
            data = self.total[pos]
        else:
            pos=0
            data=self.data
        max_pos = 0
        max_val =float(data[0][3])
        for i, entry in enumerate(data):
            if (float(entry[3]) > max_val):
                max_pos = i
                max_val = float(entry[3])
        return self.total_position(pos, max_pos)
    
    def high_tide(self, date):
        # Returns the date of highest actual tide.
        if self.state:
            pos = self.get_year(date)
            data = self.total[pos]
        else:
            pos=0
            data=self.data
        max_pos = 0
        max_val =float(data[0][11])
        for i, entry in enumerate(data):
            if (float(entry[11]) > max_val):
                max_pos = i
                max_val = float(entry[11])
        return self.total_position(pos, max_pos)
    
    def biggest_dif(self, date):
        # Returns the date of largest difference between actual and predicted tides.
        if self.state:
            pos = self.get_year(date)
            data = self.total[pos]
        else:
            pos=0
            data=self.data
        max_pos = 0
        max_val =float(data[0][12])
        for i, entry in enumerate(data):
            if float(entry[11]) > (-2.5): # checking to see if tide height is valid.
                #assume error in reading otherwise and skip
                if (float(entry[12]) > max_val):
                    max_pos = i
                    max_val = float(entry[12])
        return self.total_position(pos, max_pos)
    
    def high_wave(self, date):
        # Return the date of highest wave height.
        if self.state:
            pos = self.get_year(date)
            data = self.total[pos]
        else:
            pos=0
            data=self.data
        max_pos = 0
        max_val =float(data[0][8])
        for i, entry in enumerate(data):
            if (float(entry[11]) > max_val):
                max_pos = i
                max_val = float(entry[11])
        return self.total_position(pos, max_pos)
    
    def strong_wind(self, date):
        # Return the date of highest wind speed.
        if self.state:
            pos = self.get_year(date)
            data = self.total[pos]
        else:
            pos=0
            data=self.data
        max_pos = 0
        max_val =float(data[0][6])
        for i, entry in enumerate(data):
            if (float(entry[11]) > max_val):
                max_pos = i
                max_val = float(entry[11])
        return self.total_position(pos, max_pos)
    
    def up_down_search(self, start, iter):
        # Search up and down an array. Funciton is iteravely called until case is found.
        if (start+iter <= len(self.data)):
            if (self.data[start+iter][15] != ''):
                return (start+iter)
        if(start-iter >= 1):
            if(self.data[start-iter][15] != ''):
                return (start-iter)
        return self.up_down_search(start, iter+1)
    
    def closest_storm(self, date):
        # Return the date of closest instance of a storm event.
        if date < 75800:
            date = 75800
        pos = date
        storm = self.up_down_search(pos, 0)
        return storm
    
    