import os
import json
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Main_window import main_window

def import_details(root):
    academic_year_temp = os.popen('ls ./Academic_years')
    academic_year_list = []
    for folder in academic_year_temp:
        academic_year_list.append(folder[:-6].lower())

    with open("temp.json") as file:
        json_object = json.load(file)
        academic_year = json_object["academic_year"]
    
    academic_year_list.remove(academic_year)

    def checkbutton_1_function():
        option = checkbutton1_variable.get()
        if option:
            checkbutton2.config(state=NORMAL)
        else:
            checkbutton2.deselect()
            checkbutton3.deselect()

            checkbutton2.config(state=DISABLED)
            checkbutton3.config(state=DISABLED)

    def checkbutton_2_function():
        option = checkbutton2_variable.get()
        if option:
            checkbutton3.config(state=NORMAL)
        else:
            checkbutton3.deselect()
            checkbutton3.config(state=DISABLED)

    def checkbutton_3_function():
        pass

    def import_function():
        selected_year = dropdown.get()
        option1 = checkbutton1_variable.get()
        option2 = checkbutton2_variable.get()
        option3 = checkbutton3_variable.get()

        if selected_year not in academic_year_list:
            messagebox.showwarning("WARNING", "Select valid year")
            return

        with open("./Academic_years/"+selected_year+".json") as file:
            old_json = json.load(file)
        
        json_object = {}

        details = {
            "timetable" : [
                ["", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", ""]
            ], "class_list" : {}
        }

        timetable_structure = [
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", ""]
        ]

        if option1:
            if option2:
                if option3:
                    for i in old_json:
                        json_object[i] = old_json[i]

                else:
                    for i in old_json:
                        json_object[i] = old_json[i]
                        if (i not in ["class_list", "lab_list", "teacher_list"]):
                            json_object[i]["timetable"] = timetable_structure
                    
                    for j in json_object['class_list']:
                        for i in j:
                            for k in json_object[i]["subject_teacher_list"]:
                                json_object[i]["subject_teacher_list"][k][-1] = 0

            else:
                json_object['class_list'] = old_json['class_list']
                json_object['lab_list'] = old_json['lab_list']
                json_object['teacher_list'] = old_json['teacher_list']

                for j in json_object['class_list']:
                    for i in j:
                        json_object[i] = {
                            "timetable": timetable_structure,
                            "subject_teacher_list": {}
                        }
                
                for i in json_object['lab_list']:
                    json_object[i] = details

                for i in json_object['teacher_list']:
                    json_object[i[0]+'-'+i[1]] = details

        else:
            json_object['class_list'] = old_json['class_list']
            json_object['lab_list'] = old_json['lab_list']
            json_object['teacher_list'] = []

            for i in json_object['class_list']:
                for j in i:
                     json_object[i] = {
                        "timetable": timetable_structure,
                        "subject_teacher_list": {}
                    }
                
            for i in json_object['lab_list']:
                json_object[i] = details
        
        file = open("./Academic_years/"+academic_year+".json", 'w')
        file.write(json.dumps(json_object, indent=4))
        file.close()

        dropdown.destroy()
        checkbutton1.destroy()
        checkbutton2.destroy()
        checkbutton3.destroy()
        import_button.destroy()

        main_window(root)

    dropdown = ttk.Combobox(root, values=academic_year_list)
    dropdown.grid(row=0, column=0)
    dropdown.set("Select Academic Year")

    checkbutton1_variable = IntVar()
    checkbutton1 = Checkbutton(root, text='TEACHER LIST', variable=checkbutton1_variable, onvalue=1, offvalue=0, command=checkbutton_1_function) # command
    checkbutton1.grid(row=1, column=0)

    checkbutton2_variable = IntVar()
    checkbutton2 = Checkbutton(root, text='CLASS - SUBJECT - TEACHER ASSIGNMENT', variable=checkbutton2_variable, onvalue=1, offvalue=0, state=DISABLED, command=checkbutton_2_function)
    checkbutton2.grid(row=2, column=0)

    checkbutton3_variable = IntVar()
    checkbutton3 = Checkbutton(root, text='TIMETABLE', variable=checkbutton3_variable, onvalue=1, offvalue=0, state=DISABLED, command=checkbutton_3_function)
    checkbutton3.grid(row=3, column=0)

    import_button = Button(root, text="IMPORT", command=import_function)
    import_button.grid(row=4, column=0)

# root = Tk()
# import_details(root)
# root.mainloop()