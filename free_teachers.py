import json
from tkinter import *
from tkinter import ttk
from datetime import datetime

def get_free_teachers(root, button1, button2, button3, button4, button5, button6, button7, button8, button9):
    
    root.title('FREE TEACHERS')
    
    with open("temp.json") as file:
        json_object = json.load(file)
        academic_year = json_object["academic_year"]
    
    with open("./Academic_years/"+academic_year+".json") as file:
        json_object = json.load(file)
        teacher_list = json_object["teacher_list"]
    
    current_day = datetime.now().weekday()
    
    day_to_index = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday"
    }
    
    day_to_period = {
        "Monday": list(range(1, 9)),
        "Tuesday": list(range(1, 9)),
        "Wednesday": list(range(1, 9)),
        "Thursday": list(range(1, 9)),
        "Friday": list(range(1, 9)),
        "Saturday": list(range(1, 8)),
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
        
        for child in teacher_list_tree.get_children():
            teacher_list_tree.delete(child)
            
        day = day_dropdown.get()
        i = list(day_to_period.keys()).index(day)
        j = int(period_dropdown.get())
        for teacher in teacher_list:
            teacher_label = teacher[0]+'-'+teacher[1]
            if json_object[teacher_label]['timetable'][i][j] == '':
                teacher_list_tree.insert(parent='', text='', index=END, iid=teacher[0], values=teacher)
    
    style = ttk.Style(root)
    style.configure('Treeview', font=("Arial", 10))
    style.configure('Treeview.Heading', font=("Arial", 11))
    
    day_label = Label(root, text="DAY", font=("Arial", 11), padx=30)
    day_label.grid(row=0, column=0, pady=7, padx=10)

    day_dropdown = ttk.Combobox(root, value=list(day_to_index.values()), font=("Arial", 11))
    day_dropdown.grid(row=0, column=1, sticky=W+E, padx=10)
    day_dropdown.bind("<<ComboboxSelected>>", day_selected)

    if current_day<6: day_dropdown.set(day_to_index[current_day])

    period_label = Label(root, text="PERIOD", font=("Arial", 11))
    period_label.grid(row=1, column=0, padx=10)
    
    period_dropdown = ttk.Combobox(root, value=day_to_period.get(day_to_index[current_day], []), font=("Arial", 11))
    period_dropdown.grid(row=1, column=1, sticky=W+E, padx=10, pady=10)
    period_dropdown.bind("<<ComboboxSelected>>", period_selected)
    
    list_frame = Frame(root)
    list_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    list_scroll = Scrollbar(list_frame, orient=VERTICAL)
    list_scroll.pack(side=RIGHT, fill='y')

    teacher_list_tree = ttk.Treeview(list_frame, height=5, yscrollcommand=list_scroll.set)
    teacher_list_tree.pack()

    list_scroll.config(command=teacher_list_tree.yview)

    teacher_list_tree["columns"] = ("ID", "TEACHER")

    teacher_list_tree.column("#0", width=0, stretch=NO)

    teacher_list_tree.column("ID", width=150, anchor=CENTER)
    teacher_list_tree.heading("ID", text="ID", anchor=CENTER)

    teacher_list_tree.column("TEACHER", width=150, anchor=CENTER)
    teacher_list_tree.heading("TEACHER", text="TEACHER NAME", anchor=CENTER)
    
    back_button = Button(root, text="BACK", command=back, pady=5, font=("Arial", 11))
    back_button.grid(row=3, column=0, columnspan=2, sticky=W+E, padx=10, pady=10)
    
    root.eval('tk::PlaceWindow . center')
    

# root = Tk()
# get_free_teachers(root)
# root.mainloop()