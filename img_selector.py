from tkinter import *
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


class CanvasEditor():
    def __init__(self, width, height):
        self.height = height
        self.width = width
        # ### --- Graphics --- ###
        # ## SNIPPET OF CODE IF NEEDED TO RESIZE IMAGES WITHOUT LOSING QUALITY
        # from PIL import Image
        # size = 125, 125
        # # FOR RESCALING IMAGES WITHOUT LOSING RES
        # im = Image.open("graphics/wind/1.png")
        # im.thumbnail(size)
        # im.save("graphics/wind/11.png")

        # im = Image.open("graphics/wind/2.png")
        # im.thumbnail(size)
        # im.save("graphics/wind/21.png")

        # im = Image.open("graphics/wind/3.png")
        # im.thumbnail(size)
        # im.save("graphics/wind/31.png")

        # im = Image.open("graphics/wind/4.png")
        # im.thumbnail(size)
        # im.save("graphics/wind/41.png")

        # im = Image.open("graphics/wind/5.png")
        # im.thumbnail(size)
        # im.save("graphics/wind/51.png")

        # im = Image.open("graphics/wind/6.png")
        # im.thumbnail(size)
        # im.save("graphics/wind/61.png")

        # im = Image.open("graphics/wind/7.png")
        # im.thumbnail(size)
        # im.save("graphics/wind/71.png")

        # im = Image.open("graphics/wind/8.png")
        # im.thumbnail(size)
        # im.save("graphics/wind/81.png")

        # im = Image.open("graphics/wind/9.png")
        # im.thumbnail(size)
        # im.save("graphics/wind/91.png")



        # im = Image.open("graphics/temp/1.png")
        # im.thumbnail(size)
        # im.save("graphics/temp/11.png")

        # im = Image.open("graphics/temp/2.png")
        # im.thumbnail(size)
        # im.save("graphics/temp/21.png")

        # im = Image.open("graphics/temp/3.png")
        # im.thumbnail(size)
        # im.save("graphics/temp/31.png")

        # im = Image.open("graphics/temp/4.png")
        # im.thumbnail(size)
        # im.save("graphics/temp/41.png")

        # im = Image.open("graphics/temp/5.png")
        # im.thumbnail(size)
        # im.save("graphics/temp/51.png")

        # im = Image.open("graphics/temp/6.png")
        # im.thumbnail(size)
        # im.save("graphics/temp/61.png")

        # im = Image.open("graphics/temp/7.png")
        # im.thumbnail(size)
        # im.save("graphics/temp/71.png")

        # im = Image.open("graphics/temp/8.png")
        # im.thumbnail(size)
        # im.save("graphics/temp/81.png")

        # im = Image.open("graphics/temp/9.png")
        # im.thumbnail(size)
        # im.save("graphics/temp/91.png")


        # im = Image.open("graphics/precip/1.png")
        # im.thumbnail(size)
        # im.save("graphics/precip/11.png")

        # im = Image.open("graphics/precip/2.png")
        # im.thumbnail(size)
        # im.save("graphics/precip/21.png")

        # im = Image.open("graphics/precip/3.png")
        # im.thumbnail(size)
        # im.save("graphics/precip/31.png")

        # im = Image.open("graphics/precip/4.png")
        # im.thumbnail(size)
        # im.save("graphics/precip/41.png")

        # im = Image.open("graphics/precip/5.png")
        # im.thumbnail(size)
        # im.save("graphics/precip/51.png")




        # im = Image.open("graphics/press/1.png")
        # im.thumbnail(size)
        # im.save("graphics/press/11.png")

        # im = Image.open("graphics/press/2.png")
        # im.thumbnail(size)
        # im.save("graphics/press/21.png")

        # im = Image.open("graphics/press/3.png")
        # im.thumbnail(size)
        # im.save("graphics/press/31.png")

        # im = Image.open("graphics/press/4.png")
        # im.thumbnail(size)
        # im.save("graphics/press/41.png")

        # im = Image.open("graphics/press/5.png")
        # im.thumbnail(size)
        # im.save("graphics/press/51.png")

        # im = Image.open("graphics/press/6.png")
        # im.thumbnail(size)
        # im.save("graphics/press/61.png")

        # im = Image.open("graphics/press/7.png")
        # im.thumbnail(size)
        # im.save("graphics/press/71.png")

        # im = Image.open("graphics/press/8.png")
        # im.thumbnail(size)
        # im.save("graphics/press/81.png")
        
        
        
        # im = Image.open("graphics/moon/1.png")
        # im.thumbnail(size)
        # im.save("graphics/moon/11.png")

        # im = Image.open("graphics/moon/2.png")
        # im.thumbnail(size)
        # im.save("graphics/moon/21.png")

        # im = Image.open("graphics/moon/3.png")
        # im.thumbnail(size)
        # im.save("graphics/moon/31.png")

        # im = Image.open("graphics/moon/4.png")
        # im.thumbnail(size)
        # im.save("graphics/moon/41.png")

        # im = Image.open("graphics/moon/5.png")
        # im.thumbnail(size)
        # im.save("graphics/moon/51.png")

        # im = Image.open("graphics/moon/6.png")
        # im.thumbnail(size)
        # im.save("graphics/moon/61.png")

        # im = Image.open("graphics/moon/7.png")
        # im.thumbnail(size)
        # im.save("graphics/moon/71.png")

        # im = Image.open("graphics/moon/8.png")
        # im.thumbnail(size)
        # im.save("graphics/moon/81.png")
        
        
        
        
        # Loading in all images once
        # Temperature
        self.unknown_temp_img = PhotoImage(file=resource_path("graphics\\temp\\11.png"))
        self.red_temp_img = PhotoImage(file=resource_path("graphics\\temp\\21.png"))
        self.orange2_temp_img = PhotoImage(file=resource_path("graphics\\temp\\31.png"))
        self.orange1_temp_img = PhotoImage(file=resource_path("graphics\\temp\\41.png"))
        self.yellow_temp_img = PhotoImage(file=resource_path("graphics\\temp\\51.png"))
        self.green2_temp_img = PhotoImage(file=resource_path("graphics\\temp\\61.png"))
        self.green1_temp_img = PhotoImage(file=resource_path("graphics\\temp\\71.png"))
        self.blue2_temp_img = PhotoImage(file=resource_path("graphics\\temp\\81.png"))
        self.blue1_temp_img = PhotoImage(file=resource_path("graphics\\temp\\91.png"))
        # Wind
        self.unknown_wind_img = PhotoImage(file=resource_path("graphics\\wind\\11.png"))
        self.N_wind_img = PhotoImage(file=resource_path("graphics\\wind\\21.png"))
        self.NE_wind_img = PhotoImage(file=resource_path("graphics\\wind\\31.png"))
        self.E_wind_img = PhotoImage(file=resource_path("graphics\\wind\\41.png"))
        self.SE_wind_img = PhotoImage(file=resource_path("graphics\\wind\\51.png"))
        self.S_wind_img = PhotoImage(file=resource_path("graphics\\wind\\61.png"))
        self.SW_wind_img = PhotoImage(file=resource_path("graphics\\wind\\71.png"))
        self.W_wind_img = PhotoImage(file=resource_path("graphics\\wind\\81.png"))
        self.NW_wind_img = PhotoImage(file=resource_path("graphics\\wind\\91.png"))
        # Atmospheric Pressure
        self.unknown_press_img = PhotoImage(file=resource_path("graphics\\press\\11.png"))
        self.press1_img = PhotoImage(file=resource_path("graphics\\press\\21.png"))
        self.press2_img = PhotoImage(file=resource_path("graphics\\press\\31.png"))
        self.press3_img = PhotoImage(file=resource_path("graphics\\press\\41.png"))
        self.press4_img = PhotoImage(file=resource_path("graphics\\press\\51.png"))
        self.press5_img = PhotoImage(file=resource_path("graphics\\press\\61.png"))
        self.press6_img = PhotoImage(file=resource_path("graphics\\press\\71.png"))
        self.press7_img = PhotoImage(file=resource_path("graphics\\press\\81.png"))
        # Moon
        self.full_img = PhotoImage(file=resource_path("graphics\\moon\\11.png"))
        self.waning_gib_img = PhotoImage(file=resource_path("graphics\\moon\\21.png"))
        self.waning_half_img = PhotoImage(file=resource_path("graphics\\moon\\31.png"))
        self.waning_cres_img = PhotoImage(file=resource_path("graphics\\moon\\41.png"))
        self.new_img = PhotoImage(file=resource_path("graphics\\moon\\51.png"))
        self.waxing_cres_img = PhotoImage(file=resource_path("graphics\\moon\\61.png"))
        self.waxing_half_img = PhotoImage(file=resource_path("graphics\\moon\\71.png"))
        self.waxing_gib_img = PhotoImage(file=resource_path("graphics\\moon\\81.png"))
        # Precip
        self.precip1_img = PhotoImage(file=resource_path("graphics\\precip\\11.png"))
        self.precip2_img = PhotoImage(file=resource_path("graphics\\precip\\21.png"))
        self.precip3_img = PhotoImage(file=resource_path("graphics\\precip\\31.png"))
        self.precip4_img = PhotoImage(file=resource_path("graphics\\precip\\41.png"))
        self.precip5_img = PhotoImage(file=resource_path("graphics\\precip\\51.png"))
        
        
        self.betwicons = ((250+45)/1450)*self.height
        self.title=(30/1450)*self.height
        self.imgpos=(120/1450)*self.height
        self.maintxt=(210/1450)*self.height
        
    def temp_image_selector(self, temp):
        # Returns temperature image depending on temperature value
        if (temp != temp):
            return self.unknown_temp_img
        elif (temp < -10.0):                      #cold blue
            return self.blue1_temp_img
        elif ((temp >= -10.0) & (temp < 0.0)):  #blue
            return self.blue2_temp_img
        elif ((temp >= 0.0) & (temp < 6.0)):    #light green
            return self.green1_temp_img
        elif ((temp >= 6.0) & (temp < 12.0)):   #green
            return self.green2_temp_img
        elif ((temp >= 12.0) & (temp < 18.0)):  #yellow
            return self.yellow_temp_img
        elif ((temp >= 18.0) & (temp < 24.0)):  #orange
            return self.orange1_temp_img
        elif ((temp >= 24.0) & (temp < 32.0)):  #dark orange
            return self.orange2_temp_img
        else:                                   # red
            return self.red_temp_img
        
    def wind_image_selector(self, dir):
        # Configures temperature widget image and text depending on temperature value
        if (dir != dir):
            return self.unknown_wind_img, 'Unknown'
        elif ((dir >= 337.5) | (dir < 22.5)):
            return self.S_wind_img, 'N'
        elif ((dir >= 22.5) & (dir < 67.5)):
            return self.SW_wind_img, 'NE'
        elif ((dir >= 67.5) & (dir < 112.5)):
            return self.W_wind_img, 'E'
        elif ((dir >= 112.5) & (dir < 157.5)):
            return self.NW_wind_img, 'SE'
        elif ((dir >= 157.5) & (dir < 202.5)):
            return self.N_wind_img, 'S'
        elif ((dir >= 202.5) & (dir < 247.5)):
            return self.NE_wind_img, 'SW'
        elif ((dir >= 247.5) & (dir < 292.5)):
            return self.E_wind_img, 'W'
        else:      # (dir >= 292.5) & (dir < 337.5)
            return self.SE_wind_img, 'NW'
    
    def press_image_selector(self, press):
        if (press != press):
            return self.unknown_press_img
        elif (press < 1000):
            return self.press1_img
        elif ((press >= 1000) & (press < 1010)):
            return self.press2_img
        elif ((press >= 1010) & (press < 1025)):
            return self.press3_img
        elif ((press >= 1025) & (press < 1035)):
            return self.press4_img
        elif ((press >= 1035) & (press < 1045)):
            return self.press5_img
        elif ((press >= 1045) & (press < 1060)):
            return self.press6_img
        else:
            return self.press7_img

    def moon_image_selector(self, fullness):
        # Configures moon widget image and text depending on moon fullness value
        if ((fullness < 0.025) | (fullness >= 0.975)):
            return self.new_img
        elif ((fullness >= 0.025) & (fullness < 0.1875)):
            return self.waxing_cres_img
        elif ((fullness >= 0.1875) & (fullness < 0.3125)):
            return self.waxing_half_img
        elif ((fullness >= 0.3125) & (fullness < 0.475)):
            return self.waxing_gib_img
        elif ((fullness >= 0.475) & (fullness < 0.525)):
            return self.full_img
        elif ((fullness >= 0.525) & (fullness < 0.6875)):
            return self.waning_gib_img
        elif ((fullness >= 0.6875) & (fullness < 0.8125)):
            return self.waning_half_img
        else:   # 0.8125 <= fullness < 0.975
            return self.waning_cres_img

    def precip_image_selector(self, precip):
        if (precip != precip):
            return self.precip1_img
        elif (precip == 0):
            return self.precip1_img
        elif ((precip > 0) & (precip < 10)):
            return self.precip2_img
        elif ((precip >= 20) & (precip < 50)):
            return self.precip3_img
        elif ((precip >= 50) & (precip < 100)):
            return self.precip4_img
        else:
            return self.precip5_img
        
     
        
    def canvasCreator(self, root, canvas_width, x_coord, y_coord):
        rf = 6
        
        tfont = 'Arial ' + str(18-rf) + ' bold'
        sfont = 'Arial ' + str(16-rf) + ' bold'
        
        self.myCanvas = Canvas(root, width=canvas_width, height=self.height, bg='white')
        self.myCanvas.place(x=x_coord, y=y_coord)
        # self.myCanvas = Canvas(root, width=canvas_width, height=canvas_height, bg='white')
        # self.myCanvas.place(x=x_coord, y=y_coord)
        self.myCanvas.create_text((canvas_width/2, self.title), text='Temperature', font=tfont, fill='black')
        self.temp_img = self.myCanvas.create_image(canvas_width/2, self.imgpos+5, image=self.unknown_temp_img)
        self.temp_text = self.myCanvas.create_text((canvas_width/2, (105/1450)*self.height*2+10), text= u"\u2103", font='Arial 14 bold', fill='black')
        ### --- Wind --- ###
        # self.myCanvas = Canvas(root, width=canvas_width, height=canvas_height, bg='white')
        # self.myCanvas.place(x=x_coord, y=y_coord+canvas_height+45)
        self.myCanvas.create_text((canvas_width/2, self.betwicons+self.title), text='Wind', font=tfont, fill='black')
        self.wind_img = self.myCanvas.create_image(canvas_width/2, self.betwicons+self.imgpos, image=self.unknown_wind_img)
        self.winddir_text = self.myCanvas.create_text((canvas_width/2, self.betwicons+self.maintxt+20), text='', font=tfont, fill='#4A4A4A')
        self.windsp_text = self.myCanvas.create_text(canvas_width/2, self.betwicons+(115/1450)*self.height, text='', font=("Arial 16 bold"), fill='white')
        self.myCanvas.create_text(canvas_width/2, self.betwicons+(135/1450)*self.height, text='km/hr', font=("Arial 14 bold"), fill='white')
        ### --- Atmospheric Pressure --- ###
        # self.myCanvas = Canvas(root, width=canvas_width, height=canvas_height, bg='white')
        # self.myCanvas.place(x=x_coord, y=y_coord+canvas_height*2+45*2)
        self.myCanvas.create_text((canvas_width/2, self.betwicons*2+self.title+5), text='Atmospheric\nPressure', font=tfont, fill='black', justify='center')
        self.press_img = self.myCanvas.create_image(canvas_width/2, self.betwicons*2+self.imgpos, image=self.press_image_selector(0))
        self.press_text =  self.myCanvas.create_text((canvas_width/2, self.betwicons*2+self.maintxt), text='mbar', font='Arial 14 bold', fill='black')
        ### --- Moon Phase --- ###
        # self.myCanvas = Canvas(root, width=canvas_width, height=canvas_height, bg='white')
        # self.myCanvas.place(x=x_coord, y=y_coord+canvas_height*3+45*3)
        self.myCanvas.create_text((canvas_width/2, self.betwicons*3+self.title), text='Moon', font=tfont, fill='black')
        self.moon_img = self.myCanvas.create_image(canvas_width/2, self.betwicons*3+self.imgpos, image=self.moon_image_selector(0))
        self.moon_text =  self.myCanvas.create_text((canvas_width/2, self.betwicons*3+self.maintxt), text='%', font='Arial 14 bold', fill='black')
        ### --- Precipitation --- ###
        # self.myCanvas = Canvas(root, width=canvas_width, height=canvas_height, bg='white')
        # self.myCanvas.place(x=x_coord, y=y_coord+canvas_height*4+45*4)
        self.myCanvas.create_text((canvas_width/2, self.betwicons*4+self.title), text='Precipitation', font=tfont, fill='black')
        self.precip_img = self.myCanvas.create_image(canvas_width/2, self.betwicons*4+self.imgpos, image=self.precip_image_selector(0))
        self.precip_text =  self.myCanvas.create_text((canvas_width/2, self.betwicons*4+self.maintxt), text='mm', font='Arial 14 bold', fill='black')

    def canvasEditor(self, root, temp, wind_dir, wind_sp, press, moon_fullness, precip):
        ### --- Temperature --- ###
        if (temp != temp):
            self.myCanvas.itemconfig(self.temp_text, text='Unknown')
        else:                                   # red
            self.myCanvas.itemconfig(self.temp_text, text=("{:.1f}".format(temp), u"\u2103"))
        self.myCanvas.itemconfig(self.temp_img, image=self.temp_image_selector(temp))
        ### --- Wind --- ###
        img, txt = self.wind_image_selector(wind_dir)
        self.myCanvas.itemconfig(self.winddir_text, text=txt)
        self.myCanvas.itemconfig(self.wind_img, image=img)
        
        if(wind_sp != wind_sp):
            self.myCanvas.itemconfig(self.windsp_text, text='Unknown')
        else:
            self.myCanvas.itemconfig(self.windsp_text, text=("{:.1f}".format(wind_sp)))
        ### --- Atmospheric Pressure --- ###
        if (press != press):
            self.myCanvas.itemconfig(self.press_text, text='Unknown')
        else:
            self.myCanvas.itemconfig(self.press_text, text=("{:.1f}".format(press),'mbar'))
        self.myCanvas.itemconfig(self.press_img, image=self.press_image_selector(press))
        ### --- Moon Phase --- ###
        self.myCanvas.itemconfig(self.moon_img, image=self.moon_image_selector(moon_fullness))
        tmp = (1.0 - abs((moon_fullness - 0.5)*2)) * 100
        mn_txt = "{:.2f}".format(tmp) + '%'
        self.myCanvas.itemconfig(self.moon_text, text=mn_txt)
        ### --- Precipitation --- ###
        self.myCanvas.itemconfig(self.precip_img, image=self.precip_image_selector(precip))
        if (precip != precip):
            self.myCanvas.itemconfig(self.precip_text, text='Unknown')
        else:
            self.myCanvas.itemconfig(self.precip_text, text=(precip,'mm'))













