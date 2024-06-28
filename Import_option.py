import os
from tkinter import *
from Import_details import import_details
from Class_confirmation import class_confirmation

def import_option(root):
    root.title("Import")
    
    def button1_click():
        button1.destroy()
        button2.destroy()

        import_details(root)

    def button2_click():
        button1.destroy()
        button2.destroy()
        
        class_confirmation(root)

    ft = ("Arial", 12)
    
    button1 = Button(root, text="Import Details".upper(), command=button1_click, padx=5, pady=5, font=ft)
    button2 = Button(root, text="Create Details".upper(), command=button2_click, padx=5, pady=5, font=ft)
    
    l = os.listdir("./Academic_years")
    if (len(l) < 2):
        button1.config(state=DISABLED)

    button1.grid(row=0, column=0, padx=20, pady=5)
    button2.grid(row=1, column=0, padx=20, pady=20)
    
    root.eval('tk::PlaceWindow . center')
