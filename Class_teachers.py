import json
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def class_teacher(root, button1, button2, button3, button4, button5, button6, button7, button8, button9):
    root.title("Class teacher")
    
    def back():
        for widget in root.winfo_children():
            if widget not in [button1, button2, button3, button4, button5, button6, button7, button8, button9]:
                widget.destroy()

        button1.grid(row=0, column=0, padx=20, pady=12)
        button2.grid(row=0, column=1, padx=20, pady=12)
        button3.grid(row=1, column=0, columnspan=2, padx=20)
        button4.grid(row=2, column=0, padx=20, pady=12)
        button5.grid(row=2, column=1, padx=20, pady=12)
        button6.grid(row=3, column=0, padx=20)
        button7.grid(row=3, column=1, padx=20)
        button8.grid(row=4, column=0, padx=20, pady=12)
        button9.grid(row=4, column=1, padx=20, pady=12)
        
        root.title("TIMETABLE")
        root.eval('tk::PlaceWindow . center')
        
    def div_selected(self):
        div_select = div_dropdown.get()
        class_dropdown.config(values=class_list[class_division[div_select]])
    
    def class_selected(self):
        class_name = class_dropdown.get()
        teacher_dropdown.set(json_object[class_name]['teacher'])
        
        if current.cget("text"):
            teacher_list.remove(current.cget("text"))
            
        if json_object[class_name]['teacher']:
            teacher_list.append(json_object[class_name]['teacher'])
        
        current.config(text=json_object[class_name]['teacher'])
        teacher_dropdown.config(values=teacher_list)

    def assign():
        class_name = class_dropdown.get()
        if class_name == '':
            messagebox.showwarning("WARNING", "Select a valid Class")
            return
        
        if json_object[class_name]['teacher']:
            json_object['class_teachers'].remove(json_object[class_name]['teacher'])
            
        json_object['class_teachers'].append(teacher_dropdown.get())
        json_object[class_name]['teacher'] = teacher_dropdown.get()
        current.config(text=teacher_dropdown.get())
        
        file = open("./Academic_years/"+academic_year+".json", 'w')
        file.write(json.dumps(json_object, indent=4))
        file.close()
    
    with open("temp.json") as file:
        json_object = json.load(file)
        academic_year = json_object["academic_year"]
    
    with open("./Academic_years/"+academic_year+".json") as file:
        json_object = json.load(file)
        class_list = json_object["class_list"]
        class_list_combined = []
        
        teacher_list_1 = json_object["teacher_list"]
        class_teacher_list = json_object["class_teachers"]
        
        teacher_list = []
        for i in teacher_list_1:
            if i[0]+'-'+i[1] not in class_teacher_list:
                teacher_list.append(i[0]+'-'+i[1])

        for i in class_list:
            class_list_combined.extend(i)
    
    class_division = {"Primary": 0, "Secondary": 1, "Higher Secondary": 2}
    current = Label(root, text="")

    division_label = Label(root, text="DIVISION", font=("Arial", 11))
    division_label.grid(row=0, column=0, pady=10, padx=10)

    div_dropdown = ttk.Combobox(root, value=list(class_division.keys()), font=("Arial", 11))
    div_dropdown.grid(row=0, column=1, pady=10, padx=10)
    div_dropdown.bind("<<ComboboxSelected>>", div_selected)

    class_label = Label(root, text="CLASS", font=("Arial", 11))
    class_label.grid(row=1, column=0, padx=80, pady=10)
    
    class_dropdown = ttk.Combobox(root, value=class_list[0], font=("Arial", 11))
    class_dropdown.grid(row=1, column=1, pady=10, padx=10)
    class_dropdown.bind("<<ComboboxSelected>>", class_selected)
    
    teacher_label = Label(root, text="TEACHER", font=("Arial", 11))
    teacher_label.grid(row=2, column=0, pady=10, padx=10)
    
    teacher_dropdown = ttk.Combobox(root, value=teacher_list, font=("Arial", 11))
    teacher_dropdown.grid(row=2, column=1, pady=10, padx=10)
    
    assign_button = Button(root, text="ASSIGN", command=assign, font=("Arial", 11))
    assign_button.grid(row=3, column=0, sticky=W+E, pady=10, padx=10)
    
    back_button = Button(root, text='BACK', command=back, font=("Arial", 11))
    back_button.grid(row=3, column=1, sticky=W+E, pady=10, padx=10)
    
    root.eval('tk::PlaceWindow . center')
