import json
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

def find_teacher(root, button1, button2, button3, button4, button5, button6, button7, button8, button9):
    
    root.title('FREE TEACHERS')
    
    with open("temp.json") as file:
        json_object = json.load(file)
        academic_year = json_object["academic_year"]
    
    with open("./Academic_years/"+academic_year+".json") as file:
        json_object = json.load(file)
        teacher_list = json_object["teacher_list"]
        display_teachers = []
        for teacher in teacher_list:
            display_teachers.append('-'.join(teacher))
    
    current_day = 4 #datetime.now().weekday()
    
    day_to_index = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday"
    }
    
    index_to_date = {
        "Monday": 0,
        "Tuesday": 1,
        "Wednesday": 2,
        "Thursday": 3,
        "Friday": 4,
        "Saturday": 5
    }
    
    day_to_period = {
        "Monday": list(range(1, 9)),
        "Tuesday": list(range(1, 9)),
        "Wednesday": list(range(1, 9)),
        "Thursday": list(range(1, 9)),
        "Friday": list(range(1, 9)),
        "Saturday": list(range(1, 8))
    }
    
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
    
    def day_selected(self):
        period_dropdown.config(values=day_to_period.get(day_dropdown.get(), []))
        period_dropdown.set('')
    
    def period_selected(self):
        pass
    
    def find():
        teacher_selected = teacher_dropdown.get()
        if teacher_selected not in display_teachers:
            messagebox.showwarning("WARNING", "Select a valid teacher")
            return
        
        day = day_dropdown.get()
        if day not in list(day_to_period.keys()):
            messagebox.showwarning("WARNING", "Select a valid day")
            return
        
        period = period_dropdown.get()
        if period.isnumeric() == False or int(period) not in day_to_period[day]:
            messagebox.showwarning("WARNING", "Select a valid period")
            return
        period = int(period)
        class_list = json_object[teacher_selected]["timetable"][index_to_date[day]][period-1]
        
        if class_list:
            subject_details = json_object[class_list[0]]["timetable"][index_to_date[day]][period-1].split('::')[0]
            subject_details = json_object[class_list[0]]["subject_teacher_list"][subject_details][3]
            
            if subject_details:
                info_label.config(text="Class: "+", ".join(class_list)+"\n\nLab: "+", ".join(subject_details))
            else:
                info_label.config(text="Class: "+", ".join(class_list))
        
        else:
            info_label.config(text="FREE")
    
    style = ttk.Style(root)
    style.configure('Treeview', font=("Arial", 10))
    style.configure('Treeview.Heading', font=("Arial", 11))
    
    teacher_label = Label(root, text="TEACHER", font=("Arial", 11), padx=30)
    teacher_label.grid(row=0, column=0, pady=7, padx=10)

    teacher_dropdown = ttk.Combobox(root, value=display_teachers, font=("Arial", 11))
    teacher_dropdown.grid(row=0, column=1, sticky=W+E, padx=10)
    
    day_label = Label(root, text="DAY", font=("Arial", 11), padx=30)
    day_label.grid(row=1, column=0, pady=7, padx=10)

    day_dropdown = ttk.Combobox(root, value=list(day_to_index.values()), font=("Arial", 11))
    day_dropdown.grid(row=1, column=1, sticky=W+E, padx=10)
    day_dropdown.bind("<<ComboboxSelected>>", day_selected)

    if current_day<6: day_dropdown.set(day_to_index[current_day])

    period_label = Label(root, text="PERIOD", font=("Arial", 11))
    period_label.grid(row=2, column=0, padx=10)
    
    period_dropdown = ttk.Combobox(root, value=day_to_period.get(day_to_index[current_day], []), font=("Arial", 11))
    period_dropdown.grid(row=2, column=1, sticky=W+E, padx=10, pady=10)
    period_dropdown.bind("<<ComboboxSelected>>", period_selected)
    
    info_label = Label(root, text="Hello", font=("Arial", 13))
    info_label.grid(row=3, column=0, columnspan=2, sticky=W+E, padx=10, pady=5)
    
    find_button = Button(root, text="FIND", command=find, pady=5, font=("Arial", 11))
    find_button.grid(row=4, column=0, sticky=W+E, padx=10, pady=10)
    
    back_button = Button(root, text="BACK", command=back, pady=5, font=("Arial", 11))
    back_button.grid(row=4, column=1, sticky=W+E, padx=10, pady=10)
    
    root.eval('tk::PlaceWindow . center')
    

# root = Tk()
# find_teacher(root, 1, 2, 3, 4, 5, 6, 78, 9,10)
# root.mainloop()