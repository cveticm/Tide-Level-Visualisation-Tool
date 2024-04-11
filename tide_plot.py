from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg) 

class TidePlot():
    def __init__(self, root, width, height):
        # Initialising data into self.data for easier access
        # Creating plot
        self.fig = plt.figure(figsize = ((8/1650)*width, (8/1450)*height), dpi = 100)
        self.plot_canvas = FigureCanvasTkAgg(self.fig, master=root)   
        self.plot_canvas.draw()
        self.plot_canvas.get_tk_widget().place(x=(170/1650)*width, y=0) 
        self.ax1 = self.fig.add_subplot()
        self.ax1.grid(True)
        # Second axis is used to allow for display of hover pop-up for both actual and predicted data at seperate times.
        self.ax2 = self.ax1.twinx()
        self.ax2.tick_params(axis='y', labelcolor='white') # QUICK FIX to hide ax2 ticks

    def update_plot(self, time, act, pred, middle):
        self.ax1.clear()
        self.ax1.axvline(x=middle, color='k', alpha=0.5, linestyle='--', linewidth=2) #marking date we are currently on
        self.line1, = self.ax1.plot(time, act, markevery=[middle], marker='.', markerfacecolor='k', markersize=15, label='Actual Tide')
        self.ax1.grid(True)
        self.line2, = self.ax1.plot(time, pred, color='red', label='Predicted Tide')
        self.line2.set_linestyle('dashed')
        
        self.ax1.set_title('Tidal Height Data', fontsize=24)
        self.ax1.set_ylabel('Height (m)', fontsize=16)
        self.ax1.set_xlabel('Time', fontsize=16)
        self.ax1.legend(loc="upper right", markerscale=0, fontsize=14) # markerscale rescales the marker thats present on the lines. =0 to remove marker from legend.
        self.ax1.set_ylim(-3,3)
        self.ax1.set_xticks([len(time)//5, middle, len(time)-len(time)//5])
        self.ax1.set_xticklabels([time[len(time)//5], time[middle], time[len(time)-len(time)//5]], fontsize=6)
        self.ax1.fill_between(time, act, -3)
        self.plot_canvas.draw()
        
        self.annots = []
        for ax in [self.ax1, self.ax2]:
            annot = self.ax1.annotate("", xy=(0,0), xytext=(-20,20),textcoords="offset points",
                                bbox=dict(boxstyle="round", fc="w", alpha=0.4),
                                arrowprops=dict(arrowstyle="->"))
            annot.set_visible(False)
            self.annots.append(annot)

        self.annot_dic = dict(zip([self.ax1, self.ax2], self.annots))
        self.line_dic = dict(zip([self.ax1, self.ax2], [self.line1, self.line2]))
        
        
        self.id = self.fig.canvas.mpl_connect("motion_notify_event", self.hover)
        return

    def update_annot(self, line, annot, ind):
        x,y = line.get_data()
        annot.xy = (x[ind["ind"][0]], y[ind["ind"][0]])
        text = "Date = {}\nTide Height= {:.2f}m".format((x[ind["ind"][0]]), y[ind["ind"][0]])
        annot.set_text(text)

    def hover(self, event):
        if event.inaxes in [self.ax1, self.ax2]:
            for ax in [self.ax1, self.ax2]:
                cont, ind = self.line_dic[ax].contains(event)
                annot = self.annot_dic[ax]
                if cont:
                    self.update_annot(self.line_dic[ax], annot, ind)
                    annot.set_visible(True)
                    self.fig.canvas.draw_idle()
                else:
                    if annot.get_visible():
                        annot.set_visible(False)
                        self.fig.canvas.draw_idle()