# Import necessary modules
from tkinter import Label, Button, Tk
import matplotlib as mlp
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
import polars  as pl
import matplotlib.patches as patches
# read data from the json file


# Window settings
size = "500x500"
title = "Show Data from file"


def plot():
    unitColors = {"Celsius":"Blue",
"Fahrenheit":"Orange",
"Kelvin":"Yellow",
"Rankine":"Cyan",}
    


    df = pl.read_json('temperature_data.json')
    
    fig = Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)
    
    df = df.with_columns([
    pl.col('Units').map_dict(unitColors).alias('Color')
])

    
    y = df["Temperature"]
    x = df["Original Value"]

    cmap = plt.get_cmap('viridis')
    
    # Plot data
    ax.scatter(x, y, c=df["Color"], cmap=cmap)
    ax.set_title('Temperature Loaded')
    ax.set_xlabel('Original Value')
    ax.set_ylabel('Converted Temperature')
    
    handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10, linestyle='') 
           for color in unitColors.values()]
    labels = unitColors.keys()
    ax.legend(handles, labels, title="Units")
    # Create a FigureCanvasTkAgg object and embed it in the Tkinter window
    canvas = FigureCanvasTkAgg(fig)
    canvas.draw()
    canvas.get_tk_widget().pack( expand=1)

    canvas.get_tk_widget().pack(expand=True)


def DataScreen():
    # Create a new window
    dataScreen = Tk()  # Use Tk() to create a new main window

    dataScreen.title(title)
    dataScreen.geometry("500x500")
    


    # Add some widgets to the second window
    label = Label(dataScreen, text="This is the second window")
    label.pack(pady=20)
    
    plot()

    close_button = Button(dataScreen, text="Close", command=dataScreen.destroy)
    close_button.pack(pady=10)


    dataScreen.mainloop()



if __name__ == "__main__":
    DataScreen()
