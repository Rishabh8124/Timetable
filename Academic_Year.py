import os
import json
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Class_confirmation import class_confirmation
from Main_window import main_window

academic_year_temp = os.popen('ls ./Academic_years')
academic_year_list = []
for folder in academic_year_temp:
    academic_year_list.append(folder[:-6].lower())

def Academic_year_window(root) :    

    def choose() :

        def check_option():

            academic_year = choose_academic.get()
            if (academic_year == "Select Academic year"):
                messagebox.showwarning("WARNING", "Choose a valid year")
            else:
                with open("temp.json", 'w') as file:
                    json_object = json.dumps({"academic_year": academic_year}, indent=4)
                    file.write(json_object)
                
                choose_academic.destroy()
                confirm_choose.destroy()
                choose_button.destroy()
                create_button.destroy()

                main_window(root)

        choose_button.grid_forget()
        create_button.grid_forget()

        choose_academic = ttk.Combobox(root, values=["Select Academic year"] + academic_year_list)
        choose_academic.current(0)
        choose_academic.grid(row=0, column=0, columnspan=2)

        confirm_choose = Button(root, text="CONFIRM", command=check_option)
        confirm_choose.grid(row=1, column=1)

    def create():

        def create_year():

            global academic_year

            academic_year = academic_year_entry.get().strip().lower()
            if (academic_year == ""):
                messagebox.showwarning("WARNING", "ACADEMIC YEAR CANNOT BE EMPTY")
            elif (academic_year in academic_year_list):
                messagebox.showwarning("WARNING", "ACADEMIC YEAR ALREADY EXISTS")
            else:
                os.popen('touch ./Academic_years/'+academic_year+".json")

                with open("temp.json", 'w') as file:
                    json_object = json.dumps({"academic_year": academic_year}, indent=4)
                    file.write(json_object)
                    
                academic_year_entry.destroy()
                confirm_button.destroy()
                choose_button.destroy()
                create_button.destroy()

                class_confirmation(root)

        choose_button.grid_forget()
        create_button.grid_forget()

        academic_year_entry = Entry(root)
        academic_year_entry.grid(row=0, column=0)

        confirm_button = Button(root, text="ADD ACADEMIC YEAR", command=create_year)
        confirm_button.grid(row=0, column=1)

    for children in root.winfo_children():
        children.grid_forget()

    choose_button = Button(root, text="CHOOSE ACADEMIC YEAR", command=choose)
    create_button = Button(root, text="CREATE ACADEMIC YEAR", command=create)

    choose_button.grid(row=0, column=0)
    create_button.grid(row=1, column=0)
