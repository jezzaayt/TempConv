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
size = "850x550"
title = "Show Data from file"


def plot():
    unitColors = {"Celsius":"Blue",
"Fahrenheit":"Orange",
"Kelvin":"Red",
"Rankine":"Cyan",}
    


    df = pl.read_json('temperature_data.json')
    
    fig = Figure(figsize=(10  , 4), dpi=100)
    ax = fig.add_subplot()
    
    df = df.with_columns([
    pl.col('Units').map_dict(unitColors).alias('Color'),
])

    print(type(df["Temperature"][0]))
    y = df["Temperature"]
    x = df["Original Value"]


    
    # Plot data
    ax.scatter(x, y, c=df["Color"])
    ax.set_title('Temperatures')
    ax.set_xlabel('Original Value')
    ax.set_ylabel('Converted Temperature')
    
    handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10, linestyle='dashdot') 
           for color in unitColors.values()]
    labels = unitColors.keys()
    ax.legend(handles, labels, title="Units")
    # Create a FigureCanvasTkAgg object and embed it in the Tkinter window
    canvas = FigureCanvasTkAgg(fig)
    canvas.draw()
    canvas.get_tk_widget().pack( expand=3)

    canvas.get_tk_widget().pack(expand=True)


def DataScreen():
    # Create a new window
    dataScreen = Tk()  # Use Tk() to create a new main window

    dataScreen.title(title)
    dataScreen.geometry(size)
    


    # Add some widgets to the second window
    label = Label(dataScreen, text="Original Value is a numeric value which was originally entered\nSo the value could be any numeric value to change it to another temperature output")
    label.pack(pady=20)
    
    plot()

    close_button = Button(dataScreen, text="Close", command=dataScreen.destroy)
    close_button.pack(pady=10)


    dataScreen.mainloop()



if __name__ == "__main__":
    DataScreen()
