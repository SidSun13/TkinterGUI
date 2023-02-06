#Tkinter GUI Pdf App
#Siddharth Sundar, Period 1, AP CSP
#Credits to Python Simplified on YouTube for the base-line code to work with, as well as the pdf opening system using PyPDF2
#Description: This app utilizes the Tkinter library integrated into Python. By importing this library, various image and 
#window options are used to modify the graphical output of the display on the screen. The app incorporates a simple pdf upload
#button, which upon being filled will output text from that pdf into a text box interface for the user to see. 

#Imports
from tkinter import *
import tkinter as tk
from tkinter.filedialog import askopenfile
from PIL import ImageTk,Image
import PyPDF2
from tkinter import messagebox as mb

#Open loop
root = Tk()

#create canvas
canvas = tk.Canvas(root, width=900, height=500)
canvas.grid(columnspan=3, rowspan=3)

#Displays logo to the screen
display = Image.open('logo.png')
display = display.resize((400,300))
display = ImageTk.PhotoImage(display)
display_label = tk.Label(image=display)
display_label.image = display
display_label.grid(column=1, row=0)

#Instructions displayed to the user
instructions = tk.Label(root, text="Select a PDF file to extract its text!", font="Verdana")
instructions.grid(columnspan=3, column=0, row=1)

#Create function opening files using PyPDF2
def open_file():
    browse_text.set("Opening...")
    file = askopenfile(parent=root, mode='rb', title="Choose a PDF file", filetypes=[("Pdf file", "*.pdf")])
    if file:
        #Reads pdf and saves text
        read_pdf = PyPDF2.PdfReader(file)
        page = read_pdf.pages[0]
        page_content = page.extract_text()
        #Resizes and creates textbox
        text_box = tk.Text(root, height=10, width=100, padx=15, pady=15)
        text_box.insert(1.0, page_content)
        text_box.tag_configure("center", justify="center")
        text_box.tag_add("center", 1.0, "end")
        text_box.grid(column=1, row=2)
        #Resets the text to show complete
        browse_text.set("Browse")

        #creates another image to thank the user for using the program, deleting the previous logo
        thankyou = Image.open('thanks.png')
        thankyou = thankyou.resize((400,300))
        thankyou = ImageTk.PhotoImage(thankyou)
        thanks_label = tk.Label(image=thankyou)
        thanks_label.image = thankyou
        thanks_label.grid(column=1, row=0)
        display_label.destroy()


#Browse button opening files and button to close the program
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda:open_file(), font="Verdana", bg="cyan", fg="black", height=2, width=15)
browse_text.set("Browse")
browse_btn.grid(column=1, row=3)

#Creates a popup function that will run when the help button is clicked
def popup():
    help_text.set("Help")
    mb.showinfo("Help", "To use the program, click on the buttons shown on the screen to locate a PDF on your computer and to close the window.")
    help_text.set("Thank you!")

#Creates the visual button for "Help"
help_text = tk.StringVar()
help_button = tk.Button(root, textvariable=help_text, bd = '5', command = popup, font="Verdana", bg="cyan", fg="black", height=2, width=15)
help_text.set("Help")
help_button.grid(column=1, row=4)



root.mainloop() 
           

