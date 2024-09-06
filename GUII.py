from tkinter import LabelFrame, Label, Button, StringVar, messagebox
from tkinter import *
import tkinter as tk
from tkinter import LabelFrame, Label, Button, StringVar, messagebox
import main


size = "500x500"
title = "Temperature Checker"

root = Tk()

main_frame = tk.Frame(root)
main_frame.pack(padx=20, pady=20)

def isnum(value):
        
        try:
         
            float(value)

            return True
        except ValueError:
            return False

def ShowTemp(value, scale):
    if value != "e":
        string = "Your temperature is " + str(value) + " degrees " + str(scale)
        messagebox.showinfo("Temperature",  string)
    elif value == "0":
        string = "Your temperature is " + str(value) + " degrees " + str(scale)
        messagebox.showinfo("Temperature",  string)
    else:
        string = "This is not a valid temperature. \nThe text box will now be cleared"
        messagebox.showinfo("Temperature",  string)


class GUII():

    def __init__(self,root):
        self.initUI(root) 

    def initUI(self,root):
        root.geometry(size)
        root.title(title)

    def ToCelsius():


        text = GUII.linkText.get(1.0,"end-1c")
        if isnum(text):
            celsius = (float(text) - 32) * 5/9
            text = round(celsius,3)
            ShowTemp(text, "°C")

        else:
            ShowTemp("e", "error")
            # clear the linktext box
            GUII.linkText.delete(1.0, tk.END)
            GUII.linkText.insert(tk.END, "")


    def ToFahrenheit():
        text = GUII.linkText.get(1.0,"end-1c")
        if isnum(text):
            fahrenheit = (float(text) * 9/5) + 32
            text = round(fahrenheit,3)
            ShowTemp(str(fahrenheit), "°F")
        else:
            ShowTemp("e", "error")
            # clear the linktext box
            GUII.linkText.delete(1.0, tk.END)
            GUII.linkText.insert(tk.END, "")

    def toKelvin():
        text = GUII.linkText.get(1.0,"end-1c")
        if isnum(text):
            kelvin = float(text) + 273.15
            text = round(kelvin,3)
            ShowTemp(str(kelvin), "Kelvin")
        else:
            ShowTemp("e", "error")
            # clear the linktext box
            GUII.linkText.delete(1.0, tk.END)
            GUII.linkText.insert(tk.END, "")
    def toRankine():
        text = GUII.linkText.get(1.0,"end-1c")
        if isnum(text):
            rankine = (float(text) + 491.67) * 9/5
            text = round(rankine,3)
            ShowTemp(str(rankine), "Rankine")
        else:
            ShowTemp("e", "error")
            # clear the linktext box
            GUII.linkText.delete(1.0, tk.END)
            GUII.linkText.insert(tk.END, "")

    text_var = StringVar()
    text_var.set("Temperature Number Converter")

    innerFrame = tk.Frame(main_frame)
    innerFrame.pack()


    label = Label(innerFrame, 
                textvariable=text_var, 
                anchor=tk.CENTER,       
                
                height=3,               
                bd=3,                  
                font=("Arial", 18, "bold")
                )



    label.pack(pady=20)
    

    linkText = Text(innerFrame, height=3, width=10, bd=1, padx=2, pady=2, highlightthickness=0, font=("Arial", 20))
    linkText.pack()

    linkText.insert(END, "")


    # Create button widget from tkinter
    buttonFahrenheit = Button(innerFrame, 
                    text="To Fahrenheit", 
                    command=ToFahrenheit,
                    anchor="center",
                    bd=3,
                    bg="lightgray",
                    cursor="hand2",
                    disabledforeground="gray",
                    fg="black",
                    font=("Arial", 12),
                    height=2,
                    highlightbackground="black",
                    highlightcolor="green",
                    highlightthickness=2,
                    justify="center",
                    overrelief="raised",)

    buttonFahrenheit.pack(padx=20, pady=20, side=tk.LEFT)   

    buttonCelsius = Button(innerFrame, 
                    text="To Celsius",   
                    command=ToCelsius, 
                    anchor="center",
                    bd=3,
                    bg="lightgray",
                    cursor="hand2",
                    disabledforeground="gray",
                    fg="black",
                    font=("Arial", 12),
                    height=2,
                    highlightbackground="black",
                    highlightcolor="green",
                    highlightthickness=2,
                    justify="center",
                    overrelief="raised",)

    buttonCelsius.pack(padx=20, pady=20, side=tk.RIGHT)  

    buttonKelvin = Button(innerFrame, 
                    text="To Kelvin",   
                    command=toKelvin, 
                    anchor="center",
                    bd=3,
                    bg="lightgray",
                    cursor="hand2",
                    disabledforeground="gray",
                    fg="black",
                    font=("Arial", 12),
                    height=2,
                    highlightbackground="black",
                    highlightcolor="green",
                    highlightthickness=2,
                    justify="center",
                    overrelief="raised",)

    buttonKelvin.pack(padx=20, pady=20)  
    btnRankine = Button(innerFrame, 
                    text="To Rankine",   
                    command=toRankine, 
                    anchor="center",
                    bd=3,
                    bg="lightgray",
                    cursor="hand2",
                    disabledforeground="gray",
                    fg="black",
                    font=("Arial", 12),
                    height=2,
                    highlightbackground="black",
                    highlightcolor="green",
                    highlightthickness=2,
                    justify="center",
                    overrelief="raised",)

    btnRankine.pack(padx=20, pady=20)  
