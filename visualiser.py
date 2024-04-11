import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg) 
import numpy as np

import csv
from datetime import datetime, timedelta

from tkinter import *
from tkinter import Tk

from img_selector import *
from jump_to_buttons import *
from tide_plot import *

import sys
import os

# https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

height = 900
width = 1650 * (900/1450)


# from PIL import Image
# size = (100/1650)*width, (100/1450)*height 
# # FOR RESCALING IMAGES WITHOUT LOSING RES
# im = Image.open("graphics/refs/tideloc.png")
# im.thumbnail(size)
# im.save("graphics/refs/tideloc1.png")
# im = Image.open("graphics/refs/m2_loc.png")
# im.thumbnail(size)
# im.save("graphics/refs/m2_loc1.png")
# im = Image.open("graphics/refs/airloc.png")
# im.thumbnail(size)
# im.save("graphics/refs/airloc1.png")
# size = 200, 200
# im = Image.open("graphics/refs/map.png")
# im.thumbnail(size)
# im.save("graphics/refs/map1.png")
# size = (600/1650)*width, (600/1450)*height 
# im = Image.open("graphics/refs/size_ref.png")
# im.thumbnail(size)
# im.save("graphics/refs/size_ref1.png")


# Alignment parameters
screen_edge = 10
widget_x_edge = 800 +170 +10
UI_x_edge = 1020+170 +20


# Creating window
root = Tk()
geo = str(int(width))+'x'+str(int(height))
root.geometry(geo)
root.config(bg='white')
# root.tk.call('tk', 'scaling', width)




with open(resource_path('data\\data.csv'), 'r') as csv_file:
    reader = csv.reader(csv_file)
    data = []
    next(reader, None) # Skipping header row
    for row in reader:
        data.append(row)
    csv_file.close()

def toggle():
    if toggle_button.config('text')[-1] == 'This Year':
        toggle_button.config(text='All Time')
    else:
        toggle_button.config(text='This Year')
    butnObj.toggleState()

#TODO func takes dismiss since sliders want to give value to func. is there a more elegant solution to this then taking and dismissing a var?  
def plotTide(dismiss):
    date = timeSlide.get()
    res = resSlide.get()
    resolution = res//2
    time = []
    act = []
    pred = []
    
    # Parsing through data
    for i in range (date-resolution, date+resolution):
        if(((i) < 0.0)):
            time.append((datetime.strptime(data[date][0], '%Y-%m-%d %H:%M:%S')+timedelta(hours=(i))).strftime("%d/%b/%Y, %H:%M"))
            act.append(0.0)
            pred.append(0.0)
        elif ((i) >= len(data)):
            time.append((datetime.strptime(data[date][0], '%Y-%m-%d %H:%M:%S')+timedelta(hours=(i-len(data)))).strftime("%d/%b/%Y, %H:%M"))
            act.append(0.0)
            pred.append(0.0)
        else:
            time.append(datetime.strptime(data[i][0], '%Y-%m-%d %H:%M:%S').strftime("%d/%b/%Y, %H:%M"))
            act.append(float(data[i][11]))
            pred.append(float(data[i][10]))
    
    # Storing snapshot data
    temp = float(data[date][4])
    press = float(data[date][1])
    moon = float(data[date][9])
    precip = float(data[date][3])
    wind_sp = float(data[date][6])
    wind_dir = float(data[date][7])
    wave_h = float(data[date][8])
    wave_p = float(data[date][14])
    
    

    plotObj.update_plot(time, act, pred, resolution)
    # Calling to functions to configure widgets of snapshot data
    additional_param_canvas.canvasEditor(root, temp, wind_dir, wind_sp, press, moon, precip)
    res_text = calcRes(res)
    curr_date_label.config(text=datetime.strptime(data[date][0], '%Y-%m-%d %H:%M:%S').strftime("%d %B %Y, %H:%M"))
    curr_res_label.config(text=res_text)
    
    if (((wave_p == 0) | (wave_p != wave_p)) & (wave_h != 0)):
        x = np.arange(0.0, 12, 0.1)
        wave_signal = wave_h*np.sin(((2 * np.pi)/(5)) * x)
        wave_plot.plot(x, wave_signal, 'b')
        wave_plot.set_title('Current Recorded Wave', fontsize=12)
        wave_plot.set_ylabel('Height (m)', fontsize=10)
        wave_plot.set_xlabel('Period (s) - Unknown', fontsize=10)
        wave_plot.set_ylim(-6,6)
        wave_plot.set_xlim(0,12)
        wave_plot.grid(True)
        plt.tight_layout()
        # plt.tick_params(
        #     axis='x',          # changes apply to the x-axis
        #     which='both',      # both major and minor ticks are affected
        #     bottom=False,      # ticks along the bottom edge are off
        #     top=False,         # ticks along the top edge are off
        #     labelbottom=False) # labels along the bottom edge are off
        wave_plot_canvas.draw() 
        wave_plot.clear()
    elif (((wave_p == 0) | (wave_p != wave_p)) & (wave_h == 0)):
        wave_plot.clear()
        wave_plot.set_title('Current Recorded Wave', fontsize=12)
        wave_plot.set_ylabel('Height (m) - Unknown', fontsize=10)
        wave_plot.set_xlabel('Period (s) - Unknown', fontsize=10)
        wave_plot.set_ylim(-6,6)
        wave_plot.set_xlim(0,12)
        wave_plot.grid(True)
        
        wave_plot_canvas.draw() 
    else:
        x = np.arange(0.0, 12, 0.1)
        wave_signal = wave_h*np.sin(((2 * np.pi)/(wave_p)) * x)
        wave_plot.plot(x, wave_signal, 'b')
        wave_plot.set_title('Current Recorded Wave', fontsize=12)
        wave_plot.set_ylabel('Height (m)', fontsize=10)
        wave_plot.set_xlabel('Period (s)', fontsize=10)
        wave_plot.set_ylim(-6,6)
        wave_plot.set_xlim(0,12)
        wave_plot.grid(True)
        wave_plot_canvas.draw() 
        wave_plot.clear()
        
        
        
    act_stormless = []
    n_stormless = []
    n_storm = []
    act_storm = []
    new_time = []
    for i in range (-720, 720): # next and previous months
        if(((date+i) < 0.0)):
            act_stormless.append(0.0)
            n_stormless.append(i+720)
            new_time.append((datetime.strptime(data[date][0], '%Y-%m-%d %H:%M:%S')+timedelta(hours=(i))).strftime("%d/%b/%Y"))
        elif (((date+i) >= len(data))):
            act_stormless.append(0.0)
            n_stormless.append(i+720)
            new_time.append((datetime.strptime(data[date][0], '%Y-%m-%d %H:%M:%S')+timedelta(hours=(i-len(data)))).strftime("%d/%b/%Y"))
        elif (data[date+i][15] == ''):
            act_stormless.append(float(data[date+i][11]))
            n_stormless.append(i+720)
            new_time.append(datetime.strptime(data[date+i][0], '%Y-%m-%d %H:%M:%S').strftime("%d/%b/%Y"))
        else:
            act_storm.append(float(data[date+i][11]))
            n_storm.append(i+720)
            new_time.append(datetime.strptime(data[i][0], '%Y-%m-%d %H:%M:%S').strftime("%d/%b/%Y"))

    scatter_plot.scatter(n_stormless, act_stormless, s=.3, label='No Storm')
    scatter_plot.scatter(n_storm, act_storm, s=.3, label='Storm')
    scatter_plot.legend(loc="upper right", markerscale=10, fontsize=14)
    scatter_plot.set_title('Tidal Tracker: Storm Events & Data Outliers', fontsize=8)
    scatter_plot.set_ylabel('Height (m)', fontsize=10)
    scatter_plot.set_xlabel('Time', fontsize=10)
    scatter_plot.axvline(x=720, color='k', linestyle='--', linewidth=1)
    scatter_plot.set_xticks([1440//8, 720, 1440 - 1440//8])
    scatter_plot.set_xticklabels([new_time[1440//8], new_time[720], new_time[1440 - 1440//8]], fontsize = 6)
    scatter_plot.set_ylim(-8, 8)
    scatter_plot.grid(True)
    scatter_plot_canvas.draw()
    scatter_plot.clear()
    
    return 

def calcRes(res):
    text = ""
    months = res // 720
    days = (res % 720) // 24
    hours = res - months*720 - days*24
    if months > 0:
        text = str(months) + " mnths "
    if days > 0:
        text += str(days) + " days "
    if hours > 0:
        text += str(hours) + " hrs"
    return text

plotObj = TidePlot(root, width, height)
ref_img = PhotoImage(file=resource_path("graphics\\refs\\size_ref1.png"))
height_ref_canvas = Canvas(root, width=(200/1650)*width, height=(800/1450)*height, bg='white')
height_ref_canvas.place(x=(screen_edge/1650)*width, y=0)
height_ref_canvas.create_image((300/1650)*width, (410/1450)*height, image=ref_img)

fig2 = plt.figure(figsize = ((4.3/1650)*width,(4.3/1450)*height), dpi = 100) 
wave_plot_canvas = FigureCanvasTkAgg(fig2, master = root)   
wave_plot_canvas.draw() 
# placing the canvas on the Tkinter window 
wave_plot_canvas.get_tk_widget().place(x=((screen_edge+50)/1650)*width, y=(1000/1450)*height) 
# adding the subplot 
wave_plot = fig2.add_subplot() 
wave_plot.set_title('Current Recorded Wave', fontsize=14)
wave_plot.set_ylabel('Height (m)', fontsize=10)
wave_plot.set_xlabel('Period (s)', fontsize=10)
wave_plot.set_ylim(-6,6)

fig3 = plt.figure(figsize = ((4.3/1650)*width,(4.3/1450)*height), dpi = 100) 
# adding the subplot 
scatter_plot = fig3.add_subplot() 
scatter_plot.set_title('Actual Tide Scatter Plot', fontsize=14)
scatter_plot.set_ylabel('Height (m)', fontsize=(14/1650)*width)
scatter_plot.set_xlabel('Time', fontsize=(14/1650)*width)
scatter_plot_canvas = FigureCanvasTkAgg(fig3, master = root)   
scatter_plot_canvas.draw() 
# placing the canvas on the Tkinter window 
scatter_plot_canvas.get_tk_widget().place(x=((screen_edge+500)/1650)*width,y=(1000/1450)*height) 

# Creating sliders to navigate through time and zoom in and out
### --- Time Slider --- ###
slide_label = Label(root, text = 'Timeline', font='Ariel 12 bold', bg='white').place(x=(screen_edge/1650)*width, y=(820/1450)*height)
timeSlide = Scale(root, from_=0, to=(len(data)-1), length=(950/1450)*height, width=(20/1650)*width, orient=HORIZONTAL, command=plotTide, showvalue=0, bg='white')
timeSlide.place(x=(screen_edge/1650)*width, y=(850/1450)*height)
timeSlide.set(25)
curr_date_label = Label(root, text='', font='Ariel 12', anchor="center", bg='white')
curr_date_label.place(x=((screen_edge+450)/1650)*width, y=(880/1450)*height)

### --- Resolution Slider --- ###
# Zooming is restricted between 2 days and approx 2 months (60 days)
slide_label = Label(root, text = 'Zoom', font='Ariel 12 bold', bg='white').place(x=(screen_edge/1650)*width, y=(910/1450)*height)
resSlide = Scale(root, from_=48, to=1440, length=(950/1450)*height, width=(20/1650)*width, orient=HORIZONTAL, command=plotTide, showvalue=0, bg='white')
resSlide.place(x=(screen_edge/1650)*width, y=(940/1450)*height)
curr_res_label = Label(root, text='2 days', font='Ariel 10', anchor="center", bg='white')
curr_res_label.place(x=((screen_edge+500)/1650)*width, y=(970/1450)*height)

def setSlider(date, funct):
    pos = date
    if funct == 0:
        pos = butnObj.hottest(date)
    if funct == 1:
        pos = butnObj.coldest(date)
    if funct == 2:
        pos = butnObj.lowpress(date)
    if funct == 3:
        pos = butnObj.rainy(date)
    if funct == 4:
        pos = butnObj.high_tide(date)
    if funct == 5:
        pos = butnObj.biggest_dif(date)
    if funct == 6:
        pos = butnObj.high_wave(date)
    if funct == 7:
        pos = butnObj.strong_wind(date)
    if funct == 8:
        pos = butnObj.closest_storm(date)
        
    timeSlide.set(pos)


# https://stackoverflow.com/questions/3221956/how-do-i-display-tooltips-in-tkinter
class CreateToolTip(object):
    """
    create a tooltip for a given widget
    """
    def __init__(self, widget, text='widget info'):
        self.waittime = 100     #miliseconds
        self.wraplength = 180   #pixels
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)
        self.id = None
        self.tw = None

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)

    def showtip(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        # creates a toplevel window
        self.tw = Toplevel(self.widget)
        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(self.tw, text=self.text, justify='left',
                       background="#ffffff", relief='solid', borderwidth=1,
                       wraplength = self.wraplength, font='Arial 14')
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tw
        self.tw= None
        if tw:
            tw.destroy()

rf = 6
btnfontsize= 10
font= 'Arial ' + str(btnfontsize) + ' bold'
btnwidth = 12
btnheight = 3

### --- Jump to Buttons --- ###
jumptofont='Arial ' + str(22-rf) + ' bold'
jumptolabel = Label(root, text = 'Jump To', font=jumptofont, bg='white')
button1_ttp = CreateToolTip(jumptolabel, 'Click these buttons to jump to the extreme days within the year you are on!')
jumptolabel.place(x=(UI_x_edge/1650)*width, y=(30/1450)*height)

toggle_button = Button(root, text="This Year", font=font,  width=10,height=1, command=toggle, bg='white')
toggle_button.place(x=((UI_x_edge+200)/1650)*width,y=(35/1450)*height)
butnObj = JumpToButtons(data)
hottest_btn = Button(root, bg='white',  text='Hottest', font=font, command=lambda: setSlider(timeSlide.get(), 0), width=btnwidth,height=btnheight, wraplength=100)
# hottest_ttp = CreateToolTip(hottest_btn, 'Jumps to instance of highest temperature recorded')
hottest_btn.place(x=(UI_x_edge/1650)*width, y=((280-180)/1450)*height)
coldest_btn = Button(root, bg='white',  text='Coldest', font=font, command=lambda: setSlider(timeSlide.get(), 1), width=btnwidth,height=btnheight, wraplength=100)
# coldest_ttp = CreateToolTip(coldest_btn, 'Jumps to instance of lowest temperature recorded')
coldest_btn.place(x=((UI_x_edge+200)/1650)*width, y=((280-180)/1450)*height)
press_btn = Button(root, bg='white',  text='Lowest Pressure', font=font, command=lambda: setSlider(timeSlide.get(), 2), width=btnwidth,height=btnheight, wraplength=100)
# press_ttp = CreateToolTip(press_btn, 'Jumps to instance of lowest atmospheric pressure recorded')
press_btn.place(x=(UI_x_edge/1650)*width, y=((400-180)/1450)*height)
rain_btn = Button(root, bg='white',  text='Most Rain', font=font, command=lambda: setSlider(timeSlide.get(), 3), width=btnwidth,height=btnheight, wraplength=100)
# rain_ttp = CreateToolTip(rain_btn, 'Jumps to instance of most rain recorded')
rain_btn.place(x=((UI_x_edge+200)/1650)*width, y=((400-180)/1450)*height)
tide_btn = Button(root, bg='white',  text='Highest Actual\nTide', font=font, command=lambda: setSlider(timeSlide.get(), 4), width=btnwidth,height=btnheight, wraplength=100)
# tide_ttp = CreateToolTip(tide_btn, 'Jumps to instance of highest actual tide recorded')
tide_btn.place(x=(UI_x_edge/1650)*width, y=((520-180)/1450)*height)
diff_btn = Button(root, bg='white',  text='Biggest Difference in Prediction', font='Arial 10 bold', command=lambda: setSlider(timeSlide.get(), 5), width=12,height=3, wraplength=100)
# diff_ttp = CreateToolTip(diff_btn, 'Jumps to instance of largest difference between the predicted tide height and the actual tide height recorded')
diff_btn.place(x=((UI_x_edge+200)/1650)*width, y=((520-180)/1450)*height)
wave_btn = Button(root, bg='white',  text='Highest Wave', font=font, command=lambda: setSlider(timeSlide.get(), 6), width=btnwidth,height=btnheight, wraplength=100)
# wave_ttp = CreateToolTip(wave_btn, 'Jumps to instance of highest wave recorded')
wave_btn.place(x=(UI_x_edge/1650)*width, y=((640-180)/1450)*height)
wind_btn = Button(root, bg='white',  text='Strongest Wind', font=font, command=lambda: setSlider(timeSlide.get(), 7), width=btnwidth,height=btnheight, wraplength=100)
# wind_ttp = CreateToolTip(wind_btn, 'Jumps to instance of strongest wind speeds recorded')
wind_btn.place(x=((UI_x_edge+200)/1650)*width, y=((640-180)/1450)*height)
storm_btn = Button(root, bg='white',  text='Closest Storm', font=font, command=lambda: setSlider(timeSlide.get(), 8), width=btnwidth,height=btnheight, wraplength=100)
# storm_ttp = CreateToolTip(storm_btn, 'Jumps to the closest instance of a storm')
storm_btn.place(x=(UI_x_edge/1650)*width, y=((760-180)/1450)*height)


## --- Topographic Map --- ###
Label(root, text = 'Map', font='Arial 14 bold', bg='white').place(x=(UI_x_edge/1650)*width, y=(850/1450)*height)
map_canvas = Canvas(root, width=(300/1650)*width, height=(300/1450)*height, bg='grey')
map_canvas.place(x=((UI_x_edge-20)/1650)*width, y=(900/1450)*height)
map_img=PhotoImage(file=resource_path("graphics\\refs\\map1.png"))
tidegauge_img=PhotoImage(file=resource_path("graphics\\refs\\tideloc1.png"))
m2_img=PhotoImage(file=resource_path("graphics\\refs\\m2_loc1.png"))
airport_img=PhotoImage(file=resource_path("graphics\\refs\\airloc1.png"))
map_canvas.create_image((150/1650)*width, (150/1450)*height, image=map_img)


tideg = Button(root, bg='white',  image=tidegauge_img, height=(100/1450)*height,width=(100/1650)*width)
tideg_ttp=CreateToolTip(tideg, 'Tide Gauge location: This is where actual tidal height measurements have been taken')
tideg.place(x=((UI_x_edge+300)/1650)*width, y=(890/1450)*height)

m2b = Button(root, bg='white',  image=m2_img, height=(100/1450)*height,width=(100/1650)*width)
m2b_ttp=CreateToolTip(m2b, 'M2 Buoy location: This is where temperature, wave, wind, and atmospheric pressure measurements have been taken')
m2b.place(x=((UI_x_edge+300)/1650)*width, y=((890+110)/1450)*height)

airb = Button(root, bg='white',  image=airport_img, height=(100/1450)*height,width=(100/1650)*width)
airb_ttp=CreateToolTip(airb, 'Airport Weather Station location: This is where precipitation measurements have been taken')
airb.place(x=((UI_x_edge+300)/1650)*width, y=((890+220)/1450)*height)

## --- Additional Parameters --- ###
additional_param_canvas = CanvasEditor(width, height)
additional_param_canvas.canvasCreator(root, (200/1650)*width, (widget_x_edge/1650)*width, (10/1450)*height)

about_frame = Frame(root, bg='white')

# Create a frame for information
info_frame = Frame(root, bg='white')
info_frame.pack(fill=BOTH, expand=True)

# Add labels or text widgets to describe the information
info_label = Label(info_frame, text="Dublin Bay\nTide Visualisation", font=("Arial bold", 42), bg='white')
info_label.pack(pady=50)

def open_info_page(prev_frame):
    info_frame = Frame(root, bg='white')
    info_frame.pack(fill=BOTH, expand=True)

    # Add labels or text widgets to describe the information
    info_label = Label(info_frame, text="Dublin Bay\nTide Visualisation", font=("Arial", 24), bg='white')
    info_label.pack(pady=20)
    # Button to proceed to the main page
    proceed_button = Button(info_frame, text="Start", command=open_main_page)
    proceed_button.pack()
    
    # Button to proceed to the main page
    about_button = Button(info_frame, text="About Data", command=open_about_page)
    about_button.pack()

    # Button to proceed to the main page
    tutorial_button = Button(info_frame, text="Tutorial", command=open_tut_page)
    tutorial_button.pack()
        
    prev_frame.destroy()

import webbrowser

def open_met_link(event):
    webbrowser.open("https://www.met.ie/climate/available-data/historical-data")

def open_m2_link(event):
    webbrowser.open("https://erddap.marine.ie/erddap/tabledap/IWBNetwork.csv?station_id%2CCallSign%2Clongitude%2Clatitude%2Ctime%2CAtmosphericPressure%2CWindDirection%2CWindSpeed%2CGust%2CWaveHeight%2CWavePeriod%2CMeanWaveDirection%2CHmax%2CAirTemperature%2CDewPoint%2CSeaTemperature%2Csalinity%2CRelativeHumidity%2CSprTp%2CThTp%2CTp%2CQC_Flag&longitude=-5.4302&latitude=53.4836&time%3C=2024-03-10T13%3A13%3A39Z")
    
def open_tide_link(event):
    webbrowser.open("https://erddap.marine.ie/erddap/tabledap/IrishNationalTideGaugeNetwork.csv?time%2Caltitude%2Clatitude%2Clongitude%2Cstation_id%2Cdatasourceid%2CWater_Level_LAT%2CWater_Level_OD_Malin%2CQC_Flag&time%3C=2024-03-10T13%3A18%3A45Z&station_id%3E=%22Dublin%20Port%22")

# Function to open the main page
def open_main_page():
    # Destroy the info frame
    info_frame.destroy()
    about_frame.destroy()
    # Call the function to create and display the main page widgets
    
    # Function to open the main page
def open_about_page():
    about_frame.pack(fill=BOTH, expand=True)
    title = Label(about_frame, text="About the Data", font=("Arial bold", 32), bg='white')
    title.place(x=(825/1650)*width, y= 75, anchor=CENTER)
    Label(about_frame, text='This tool uses real data from the Dublin Bay area going back to 2007.', font=("Arial", 14), bg='white').place(x=(825/1650)*width, y= 200, anchor=CENTER)
    Label(about_frame, text='Weather data has been taken from the weather station in Dublin Airport.\nYou can access it yourself at', font=("Arial", 14), bg='white').place(x=(825/1650)*width, y= 300, anchor=CENTER)
    met_link = Label(about_frame, text="Met \u00c9ireann", font=("Arial", 14), fg="blue", cursor="hand2", bg='white')
    met_link.place(x=(1050/1650)*width, y= 312, anchor=CENTER)
    met_link.bind("<Button-1>", open_met_link)
    
    Label(about_frame, text='Wave data has been taken from the M2 buoy, 20km off-shore of Dublin. Access it here, from the ', font=("Arial", 14), bg='white').place(x=(825/1650)*width, y= 350, anchor=CENTER)
    m2_link = Label(about_frame, text="Marine Institute Ireland", font=("Arial", 14), fg="blue", cursor="hand2", bg='white')
    m2_link.place(x=(1470/1650)*width, y= 350, anchor=CENTER)
    m2_link.bind("<Button-1>", open_m2_link)
    
    Label(about_frame, text='Actual tidal heights have been taken from the Dublin Bay tidal gauge. Access it here, from the ', font=("Arial", 14), bg='white').place(x=(825/1650)*width, y= 400, anchor=CENTER)
    tide_link = Label(about_frame, text="Marine Institute Ireland", font=("Arial", 14), fg="blue", cursor="hand2", bg='white')
    tide_link.place(x=(1450/1650)*width, y= 400, anchor=CENTER)
    # Bind the label to the open_link function when clicked
    tide_link.bind("<Button-1>", open_tide_link)
    
    Label(about_frame, text='Predicted tidal heights have been taken by calculations done by a researcher at Trinity College Dublin', font=("Arial", 14), bg='white').place(x=(825/1650)*width, y= 450, anchor=CENTER)
    Label(about_frame, text='Storm dates have been taken from Met \u00c9ireann. As the current official naming convension for storms \nbegan in 2015, only storms from then onwards have been included.', font=("Arial", 14), bg='white').place(x=(825/1650)*width, y= 500, anchor=CENTER)
    Label(about_frame, text='In this tool, the \'Tide Height Data\' and \'Tidal Tracker: Storm Events & Data Outliers\' plots show data over a \nspan of time. All other widgets show readings from the hour you are on.', font=("Arial", 14), bg='white').place(x=(825/1650)*width, y= 600, anchor=CENTER)

    
    
    proceed_button = Button(about_frame, text="Start", font=("Arial", 14), command=open_main_page, width=20, height=3)
    proceed_button.place(x=(825/1650)*width, y= 700, anchor=CENTER)
    # Destroy the info frame
    info_frame.destroy()
    # Call the function to create and display the main page widgets
    
    # Function to open the main page
def open_tut_page():
    # Create a frame for tutorial
    tut_frame = Frame(root, bg='white')
    tut_frame.pack(fill=BOTH, expand=True)
    
    info_label = Label(tut_frame, text="Tool Tutorial", font=("Arial", 24), bg='white')
    info_label.pack(pady=20)

    return_button = Button(tut_frame, text="Return", font=("Arial", 14), width=20, height=3, command=lambda:open_main_page(tut_frame))
    return_button.pack()
    # Destroy the info frame
    info_frame.destroy()
    # Call the function to create and display the main page widgets


proceed_button = Button(info_frame, text="Start", font=("Arial", 14), width=20, height=3, command=open_main_page)
proceed_button.pack(pady=10)
    
# Button to proceed to the main page
about_button = Button(info_frame, text="About Data", font=("Arial", 14), width=20, height=3, command=open_about_page)
about_button.pack()

# # Button to proceed to the main page
# tutorial_button = Button(info_frame, text="Tutorial", command=open_tut_page)
# tutorial_button.pack()

def on_closing():
    root.destroy()
    exit()

root.protocol("WM_DELETE_WINDOW", on_closing)
# Create event loop
root.mainloop()



