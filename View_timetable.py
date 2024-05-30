import json
from tkinter import *
from tkinter import ttk

def view_timetable(root, button1, button2, button3, button4):
    with open("temp.json") as file:
        json_object = json.load(file)
        academic_year = json_object["academic_year"]
    
    with open("./Academic_years/"+academic_year+".json") as file:
        json_object = json.load(file)
    
    timetable_structure = [
        ["", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""]
    ]
    def back():
        for widget in root.winfo_children():
            if widget not in [button1, button2, button3, button4]:
                widget.destroy()

        button1.grid(row=0, column=0)
        button2.grid(row=1, column=0)
        button3.grid(row=2, column=0)
        button4.grid(row=3, column=0)

    def drop1_selected(self):
        select = dropdown1.get()
        if select in ["Class with Teacher name", "Class without Teacher name"]:
            final = []
            for i in json_object['class_list']:
                final.extend(i)
        
        elif select == "Teacher":
            final = []
            for i in json_object['teacher_list']:
                final.append(i[0]+'-'+i[1])
        
        elif select == "Lab":
            final = json_object['lab_list']
        
        dropdown2.config(values=final)

    def drop2_selected(self):
        select1 = dropdown1.get()
        select = dropdown2.get()
        timetable_details = json_object[select]['timetable']

        if select1 != "Class without Teacher name":
            for i in range(len(timetable_structure)):
                for j in range(len(timetable_structure[i])):
                    if (i and j): timetable_structure[i][j].config(text=str(timetable_details[i-1][j-1]))
        
        else:
            for i in range(len(timetable_structure)):
                for j in range(len(timetable_structure[i])):
                    if (i and j):
                        if '::' not in timetable_details[i-1][j-1]:
                            timetable_structure[i][j].config(text=timetable_details[i-1][j-1])
                        else:
                            timetable_structure[i][j].config(text=timetable_details[i-1][j-1].split('::')[0])
    
    dropdown1 = ttk.Combobox(root, values=["Class with Teacher name", "Class without Teacher name", "Teacher", "Lab"])
    dropdown1.grid(row=0, column=0, columnspan=9, sticky=W+E)
    dropdown1.bind("<<ComboboxSelected>>", drop1_selected)

    dropdown2 = ttk.Combobox(root)
    dropdown2.grid(row=1, column=0, columnspan=9, sticky=W+E)
    dropdown2.bind("<<ComboboxSelected>>", drop2_selected)

    day = {
        1: "MONDAY",
        2: "TUESDAY",
        3: "WEDNESDAY",
        4: "THURSDAY",
        5: "FRIDAY",
        6: "SATURDAY"
    }

    for i in range(len(timetable_structure)):
        for j in range(len(timetable_structure[i])):
            if (i and j): timetable_structure[i][j] = Label(root, text='', width=18)
            elif (i): timetable_structure[i][j] = Label(root, text=day[i], width=18)
            elif (j): timetable_structure[i][j] = Label(root, text=str(j), width=18)
            
            if (i or j): timetable_structure[i][j].grid(row=i+2, column=j, sticky=W+E)

    back_button = Button(root, text="BACK", command=back)
    back_button.grid(row=9, column=0, columnspan=8)