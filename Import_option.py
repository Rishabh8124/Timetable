from tkinter import *
from Import_details import import_details
from Class_confirmation import class_confirmation

def import_option(root):
    def button1_click():
        button1.destroy()
        button2.destroy()

        import_details(root)

    def button2_click():
        button1.destroy()
        button2.destroy()
        
        class_confirmation(root)

    button1 = Button(root, text="Import Details", command=button1_click)
    button2 = Button(root, text="Create Details", command=button2_click)

    button1.grid(row=0, column=0)
    button2.grid(row=1, column=0)
