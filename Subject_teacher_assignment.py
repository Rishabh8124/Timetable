import json
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def subject_teacher_assignment(root):

    def back_window(frame):
        frame.destroy()

        add_teacher_button.grid(row=9, column=1)
        delete_teacher_button.grid(row=9, column=2)

    def back_window_2(frame):
        frame.destroy()

        add_class_button.grid(row=12, column=1)
        delete_class_button.grid(row=12, column=2)

    def add_teacher_window(dropdown, frame):
        teacher_selected = dropdown.get()
        if (teacher_selected):
            selected_teacher_list.append(teacher_selected)
            if (checkbutton_3_var.get() == 0 and checkbutton_5_var.get() == 0):
                add_teacher_button.config(state=DISABLED)

            teachers_list_tree.insert(parent='', index=END, iid=teacher_selected.split('-')[0], text='', value=teacher_selected)

            frame.destroy()

            add_teacher_button.grid(row=9, column=1)
            delete_teacher_button.grid(row=9, column=2)

        elif teacher_selected:
            messagebox.showwarning("WARNING", "TEACHER HAS BEEN ASSIGNED")
        else:
            messagebox.showwarning("WARNING", "SELECT A TEACHER")

    def add_teacher():
        add_teacher_button.grid_forget()
        delete_teacher_button.grid_forget()

        with open("./Academic_years/"+academic_year+"/Teacher_list.json", 'r') as file:
            json_object = json.load(file)
            teacher_list = [i[0]+'-'+i[1] for i in json_object["teacher_list"]]
            for j in selected_teacher_list:
                teacher_list.remove(j)

        add_teacher_frame = Frame(root)
        add_teacher_frame.grid(row=9, column=0, columnspan=3)

        teacher_list_dropdown = ttk.Combobox(add_teacher_frame, value=teacher_list)
        teacher_list_dropdown.grid(row=0, column=0)

        add_button = Button(add_teacher_frame, text="ADD TEACHER", command=lambda: add_teacher_window(teacher_list_dropdown, add_teacher_frame))
        add_button.grid(row=0, column=1)

        back_button = Button(add_teacher_frame, text="BACK", command=lambda: back_window(add_teacher_frame))
        back_button.grid(row=0, column=2)

    def delete_teacher():
        teacher_selected = teachers_list_tree.focus()
        if teacher_selected:
            value = list(teachers_list_tree.item(teacher_selected, 'values'))
            selected_teacher_list.remove(value[0])
            teachers_list_tree.delete(teacher_selected)
            add_teacher_button.config(state=NORMAL)
        else:
            messagebox.showwarning("WARNING", "SELECT A TEACHER TO DELETE")

    def add_class_window(dropdown, frame):
        class_selected = dropdown.get()
        if class_selected:
            selected_class_list.append(class_selected)
            classes_list_tree.insert(parent='', index=END, iid=class_selected, text='', value=class_selected)
            frame.destroy()

            add_class_button.grid(row=12, column=1)
            delete_class_button.grid(row=12, column=2)
            delete_class_button.config(state=NORMAL)

        else:
            messagebox.showwarning("WARNING", "SELECT A CLASS")

    def add_class():
        add_class_button.grid_forget()
        delete_class_button.grid_forget()

        new_class_list = class_list_combined.copy()
        for j in selected_class_list:
            new_class_list.remove(j)

        add_class_frame = Frame(root)
        add_class_frame.grid(row=12, column=0, columnspan=3)

        class_list_dropdown = ttk.Combobox(add_class_frame, value=new_class_list)
        class_list_dropdown.grid(row=0, column=0)

        add_button = Button(add_class_frame, text="ADD CLASS", command=lambda: add_class_window(class_list_dropdown, add_class_frame))
        add_button.grid(row=0, column=1)

        back_button = Button(add_class_frame, text="BACK", command=lambda: back_window_2(add_class_frame))
        back_button.grid(row=0, column=2)

    def delete_class():
        class_selected = classes_list_tree.focus()

        if class_selected != class_dropdown.get():
            selected_class_list.remove(class_selected)
            classes_list_tree.delete(class_selected)
            if len(selected_class_list) == 1:
                delete_class_button.config(state=DISABLED)

        elif class_selected:
            messagebox.showwarning("WARNING", "PRIMARY CLASS CANNOT BE DELETED FROM LIST")

        else:
            messagebox.showwarning("WARNING", "SELECT A CLASS TO DELETE")

    def lab_entry():
        if checkbutton_1_var.get() == 1:
            lab_entry_box.config(state=NORMAL)
        else:
            lab_entry_box.config(state=DISABLED)

    def combined_teacher_check():
        if (checkbutton_3_var.get() == 0):
            if (len(selected_teacher_list) == 0):
                add_teacher_button.config(state=NORMAL)
            elif (len(selected_teacher_list) > 1):
                messagebox.showwarning("WARNING", "MULTIPLIE TEACHERS SELECTED. DELETE ADDITIONAL TEACHERS TO SWITCH OPTION")
                checkbutton_3.select()
            else:
                add_teacher_button.config(state=DISABLED)
        else:
            if checkbutton_5_var.get() == 1:
                messagebox.showwarning("WARNING", "TOGGLING OPTION FROM SEPERATE TEACHERS TO COMBINED TEACHERS")
                checkbutton_5.deselect()
            else:
                add_teacher_button.config(state=NORMAL)
    
    def combined_class_check():
        if checkbutton_2_var.get():
            if len(selected_class_list):
                add_class_button.config(state=NORMAL)
        else:
            if len(selected_class_list) == 1:
                add_class_button.config(state=DISABLED)
            elif len(selected_class_list) > 1:
                option = messagebox.askyesno("CONFIRM", "DO YOU WANT TO REMOVE OTHER CLASSES?")
                if option:
                    for class_added in selected_class_list[1:]:
                        selected_class_list.remove(class_added)
                        classes_list_tree.delete(class_added)
                    delete_class_button.config(state=DISABLED)
                    add_class_button.config(state=DISABLED)
                else:
                    checkbutton_2.select()
            else:
                add_class_button.config(state=DISABLED)

    
    def seperate_teachers_check():
        if checkbutton_5_var.get():
            if checkbutton_3_var.get() == 0:
                add_teacher_button.config(state=NORMAL)
            else:
                messagebox.showwarning("WARNING", "TOGGLING OPTION FROM COMBINED TEACHERS TO SEPERATE TEACHERS")
                checkbutton_3.deselect()
        else:
            if len(selected_teacher_list) == 1:
                add_teacher_button.config(state=DISABLED)
            elif len(selected_teacher_list) == 0:
                pass
            else:
                messagebox.showwarning("WARNING", "MULTIPLIE TEACHERS SELECTED. DELETE ADDITIONAL TEACHERS TO SWITCH OPTION")
                checkbutton_5.select()
    
    def consecutive_periods_check():
        if checkbutton_4_var.get():
            consecutive_periods_entry.config(state=NORMAL)
            consecutive_periods_entry.delete(0, END)
            consecutive_periods_entry.insert(0, "1")
        else:
            consecutive_periods_entry.delete(0, END)
            consecutive_periods_entry.config(state=DISABLED)

    def div_selected(self):
        div_select = div_dropdown.get()
        class_dropdown.config(values=class_list[class_division[div_select]])

    def class_selected(self):
        class_name = class_dropdown.get()
        selected_class_list.clear()
        selected_class_list.append(class_name)

        for class_added in classes_list_tree.get_children():
            classes_list_tree.delete(class_added)
        
        classes_list_tree.insert(parent='', index=END, iid=class_name, text='', value=class_name)

        file = open('./Academic_years/'+academic_year+'/Class/'+class_name+".json", 'r')
        json_object = json.load(file)
        file.close()

        subject_list_1 = json_object["subject_teacher_list"]

        for subject in subject_registered.get_children():
            subject_registered.delete(subject)

        for subject in subject_list_1:
            subject_registered.insert(parent='', index=END, iid=subject, text='', value=subject_list_1[subject])
        
        checkbutton_1.deselect()
        checkbutton_2.deselect()
        checkbutton_3.deselect()
        checkbutton_4.deselect()
        checkbutton_5.deselect()

        lab_entry_box.config(state=DISABLED)
        lab_entry_box.set("")

        subject_name_entry.delete(0, END)
        count_entry.delete(0, END)

        for teacher in teachers_list_tree.get_children():
            teachers_list_tree.delete(teacher)

        selected_teacher_list.clear()
        add_teacher_button.config(state=NORMAL)
        add_class_button.config(state=DISABLED)
        delete_class_button.config(state=DISABLED)

        consecutive_periods_entry.delete(0, END)
        consecutive_periods_entry.config(state=DISABLED)

        save_button.config(state=NORMAL)
    
    def save_details():
        subject = subject_name_entry.get()
        count = count_entry.get()
        lab_name = ""
        if (checkbutton_1_var.get()): 
            lab_name = lab_entry_box.get()
        consecutive_periods = 1
        if (checkbutton_4_var.get()):
            consecutive_periods = consecutive_periods_entry.get()
        
        if subject == '':
            messagebox.showwarning("WARNING", "SUBJECT NAME IS EMPTY")
            return
        if count.isnumeric() == False:
            messagebox.showwarning("WARNING", "COUNT SHOULD BE AN INTEGER")
            return
        if checkbutton_1_var.get() and lab_name == '':
            messagebox.showwarning("WARNING", "LAB NAME IS EMPTY")
            return
        if checkbutton_4_var.get() and consecutive_periods.isnumeric() == False:
            messagebox.showwarning("WARNING", "CONSECUTIVE PERIODS SHOULD BE AN INTEGER")
            return
        
        details = [subject, count, selected_teacher_list, lab_name, selected_class_list, consecutive_periods, 1*checkbutton_3_var.get()+2*checkbutton_5_var.get()]
        for i in subject_registered.get_children():
            if subject == i:
                confirm = messagebox.askyesno("WARNING", "SAVE CHANGES")
                if not confirm:
                    return
                else:
                    subject_registered.delete(subject)
        
        subject_registered.insert(parent='', text='', index=END, iid=subject, value=details)

        class_name = class_dropdown.get()

        for class_added in classes_list_tree.get_children():
            classes_list_tree.delete(class_added)
        
        classes_list_tree.insert(parent='', index=END, iid=class_name, text='', value=class_name)

        file = open('./Academic_years/'+academic_year+'/Class/'+class_name+".json", 'r')
        json_object = json.load(file)
        file.close()

        json_object["subject_teacher_list"][subject] = details

        with open('./Academic_years/'+academic_year+'/Class/'+class_name+".json", 'w') as file:
            file.write(json.dumps(json_object))

        checkbutton_1.deselect()
        checkbutton_2.deselect()
        checkbutton_3.deselect()
        checkbutton_4.deselect()
        checkbutton_5.deselect()

        subject_name_entry.delete(0, END)
        count_entry.delete(0, END)

        lab_entry_box.set("")
        lab_entry_box.config(state=DISABLED)

        for teacher in teachers_list_tree.get_children():
            teachers_list_tree.delete(teacher)

        selected_teacher_list.clear()
        selected_class_list.clear()
        selected_class_list.append(class_name)
        add_teacher_button.config(state=NORMAL)
        add_class_button.config(state=DISABLED)
        delete_class_button.config(state=DISABLED)
        consecutive_periods_entry.delete(0, END)
        consecutive_periods_entry.config(state=DISABLED)
    
    def edit_details():
        class_name = class_dropdown.get()

        with open('./Academic_years/'+academic_year+'/Class/'+class_name+".json", 'r') as file:
            subject_list = json.load(file)["subject_teacher_list"]

        checkbutton_1.deselect()
        checkbutton_2.deselect()
        checkbutton_3.deselect()
        checkbutton_4.deselect()
        checkbutton_5.deselect()

        subject_name_entry.delete(0, END)
        count_entry.delete(0, END)

        for teacher in teachers_list_tree.get_children():
            teachers_list_tree.delete(teacher)
        selected_teacher_list.clear()
        add_teacher_button.config(state=NORMAL)
        add_class_button.config(state=DISABLED)
        delete_class_button.config(state=DISABLED)
        consecutive_periods_entry.delete(0, END)
        consecutive_periods_entry.config(state=DISABLED)

        selected_subject = subject_registered.focus()
        if not selected_subject:
            return

        selected_list = subject_list[selected_subject]
        subject_name_entry.insert(0, selected_list[0])
        count_entry.insert(0, selected_list[1])

        for teacher in selected_list[2]:
            selected_teacher_list.append(teacher)
            teachers_list_tree.insert(parent='', index=END, iid=teacher.split('-')[0], text='', value=teacher)

        if selected_list[3]:
            checkbutton_1.select()
            lab_entry_box.config(state=NORMAL)
            lab_entry_box.current(lab_list.index(selected_list[3]))
        else:
            lab_entry_box.set("")
            lab_entry_box.config(state=DISABLED)
        
        if len(selected_list[4]) > 1:
            checkbutton_2.select()
            delete_class_button.config(state=NORMAL)
            add_class_button.config(state=NORMAL)
            for class_selected in selected_list[4][1:]:
                selected_class_list.append(class_selected)
                classes_list_tree.insert(parent='', index=END, iid=class_selected, text='', value=class_selected)
        else:
            delete_class_button.config(state=DISABLED)
            add_class_button.config(state=DISABLED)
        
        if selected_list[5] != 1:
            checkbutton_4.select()
            consecutive_periods_entry.config(state=NORMAL)
            consecutive_periods_entry.insert(0, selected_list[5])
        
        if selected_list[6] == 1:
            checkbutton_3.select()
            add_teacher_button.config(state=NORMAL)
        elif selected_list[6] == 2:
            checkbutton_5.select()
            add_teacher_button.config(state=NORMAL)
        else:
            add_teacher_button.config(state=DISABLED)

    def clear_details():
        selected_subject = subject_registered.focus()
        if not selected_subject:
            messagebox.showwarning("WARNING", "SELECT SUBJECT TO CLEAR")
            return

        subject_registered.delete(selected_subject)
        class_name = class_dropdown.get()

        with open('./Academic_years/'+academic_year+'/Class/'+class_name+".json", 'r') as file:
            json_object = json.load(file)
        
        json_object["subject_teacher_list"].pop(selected_subject)

        with open('./Academic_years/'+academic_year+'/Class/'+class_name+".json", 'w') as file:
            file.write(json.dumps(json_object))

    selected_teacher_list = []
    selected_class_list = []
    
    with open("temp.json") as file:
        json_object = json.load(file)
        academic_year = json_object["academic_year"]
    
    with open("./Academic_years/"+academic_year+"/Class_list.json") as file:
        json_object = json.load(file)
        class_list = json_object["class_list"]
        class_list_combined = []

        for i in class_list:
            class_list_combined.extend(i)

    with open("./Academic_years/"+academic_year+"/Lab_list.json") as file:
        json_object = json.load(file)
        lab_list = json_object["lab_list"]
   
    class_division = {"Primary": 0, "Secondary": 1, "Higher Secondary": 2}

    div_dropdown = ttk.Combobox(root, value=list(class_division.keys()))
    div_dropdown.grid(row=0, column=0, columnspan=3, sticky=W+E)
    div_dropdown.bind("<<ComboboxSelected>>", div_selected)

    class_dropdown = ttk.Combobox(root, value=class_list[0])
    class_dropdown.grid(row=1, column=0, columnspan=3, sticky=W+E)
    class_dropdown.bind("<<ComboboxSelected>>", class_selected)

    subject_frame = Frame(root)
    subject_frame.grid(row=2, column=0, columnspan=3)

    scroll = Scrollbar(subject_frame, orient=VERTICAL)
    scroll.pack(side=RIGHT, fill='y')

    subject_registered = ttk.Treeview(subject_frame, height=9, yscrollcommand=scroll.set)
    subject_registered.pack()

    scroll.config(command=subject_registered.yview)

    subject_registered["columns"] = ("SUBJECT", "COUNT", "TEACHERS", "LAB", "COMBINED CLASS")

    subject_registered.column("#0", width=0, stretch=NO)

    subject_registered.column("SUBJECT", anchor=CENTER)
    subject_registered.heading("SUBJECT", text="SUBJECT", anchor=CENTER)

    subject_registered.column("TEACHERS", anchor=CENTER)
    subject_registered.heading("TEACHERS", text="TEACHERS", anchor=CENTER)

    subject_registered.column("LAB", width=120, anchor=CENTER)
    subject_registered.heading("LAB", text="LAB", anchor=CENTER)

    subject_registered.column("COMBINED CLASS", width=150, anchor=CENTER)
    subject_registered.heading("COMBINED CLASS", text="CLASSES COMBINED", anchor=CENTER)

    subject_registered.column("COUNT", width=80, anchor=CENTER)
    subject_registered.heading("COUNT", text="COUNT", anchor=CENTER)

    edit_button = Button(root, text="EDIT DETAILS", command=edit_details)
    edit_button.grid(row=3, column=0, columnspan=2)

    clear_button = Button(root, text="CLEAR DETAILS", command=clear_details)
    clear_button.grid(row=3, column=2)

    subject_name_label =  Label(root, text="SUBJECT NAME: ")
    subject_name_label.grid(row=4, column=0)

    subject_name_entry = Entry(root)
    subject_name_entry.grid(row=4, column=1, columnspan=2)

    count_label =  Label(root, text="COUNT: ")
    count_label.grid(row=5, column=0)

    count_entry = Entry(root)
    count_entry.grid(row=5, column=1, columnspan=2)

    teachers_label = Label(root, text="TEACHERS HANDLING: ")
    teachers_label.grid(row=6, column=0)

    checkbutton_3_var = IntVar()
    checkbutton_3 = Checkbutton(root, text="COMBINED TEACHERS", variable=checkbutton_3_var, onvalue=1, offvalue=0, command=combined_teacher_check)
    checkbutton_3.grid(row=7, column=0)

    checkbutton_5_var = IntVar()
    checkbutton_5 = Checkbutton(root, text="MULTIPLE AND SEPERATE TEACHERS", onvalue=1, offvalue=0, variable=checkbutton_5_var, command=seperate_teachers_check)
    checkbutton_5.grid(row=8, column=0)

    teachers_frame = Frame(root)
    teachers_frame.grid(row=6, column=1, columnspan=2, rowspan=3)

    teachers_scroll = Scrollbar(teachers_frame, orient=VERTICAL)
    teachers_scroll.pack(side=RIGHT, fill='y')

    teachers_list_tree = ttk.Treeview(teachers_frame, height=5, yscrollcommand=teachers_scroll.set)
    teachers_list_tree.pack()

    teachers_scroll.config(command=teachers_list_tree.yview)

    teachers_list_tree["columns"] = ("TEACHERS")

    teachers_list_tree.column("#0", width=0, stretch=NO)

    teachers_list_tree.column("TEACHERS", anchor=CENTER)
    teachers_list_tree.heading("TEACHERS", text="TEACHERS", anchor=CENTER)

    add_teacher_button = Button(root, text="ADD TEACHER", command=add_teacher)
    add_teacher_button.grid(row=9, column=1)

    delete_teacher_button = Button(root, text="DELETE TEACHER", command=delete_teacher)
    delete_teacher_button.grid(row=9, column=2)

    checkbutton_1_var = IntVar()
    checkbutton_1 = Checkbutton(root, text="LAB", variable=checkbutton_1_var, onvalue=1, offvalue=0, command=lab_entry)
    checkbutton_1.grid(row=10, column=0)

    lab_entry_box = ttk.Combobox(root, value=lab_list, state=DISABLED)
    lab_entry_box.grid(row=10, column=1, columnspan=2)

    checkbutton_2_var = IntVar()
    checkbutton_2 = Checkbutton(root, text="COMBINED CLASS", onvalue=1, offvalue=0, variable=checkbutton_2_var, command=combined_class_check)
    checkbutton_2.grid(row=11, column=0)

    classes_frame = Frame(root)
    classes_frame.grid(row=11, column=1, columnspan=2)

    classes_scroll = Scrollbar(classes_frame, orient=VERTICAL)
    classes_scroll.pack(side=RIGHT, fill='y')

    classes_list_tree = ttk.Treeview(classes_frame, height=5, yscrollcommand=classes_scroll.set)
    classes_list_tree.pack()

    classes_scroll.config(command=classes_list_tree.yview)

    classes_list_tree["columns"] = ("CLASSES")

    classes_list_tree.column("#0", width=0, stretch=NO)

    classes_list_tree.column("CLASSES", anchor=CENTER)
    classes_list_tree.heading("CLASSES", text="CLASSES", anchor=CENTER)

    add_class_button = Button(root, text="ADD CLASS", command=add_class, state=DISABLED)
    add_class_button.grid(row=12, column=1)

    delete_class_button = Button(root, text="DELETE CLASS", command=delete_class, state=DISABLED)
    delete_class_button.grid(row=12, column=2)

    checkbutton_4_var = IntVar()
    checkbutton_4 = Checkbutton(root, text="CONSECUTIVE PERIODS", onvalue=1, offvalue=0, variable=checkbutton_4_var, command=consecutive_periods_check)
    checkbutton_4.grid(row=13, column=0)

    consecutive_periods_entry = Entry(root, state=DISABLED)
    consecutive_periods_entry.grid(row=13, column=1, columnspan=2)

    save_button = Button(root, text="SAVE DETAILS", command=save_details, state=DISABLED)
    save_button.grid(row=14, column=0, columnspan=3)

root = Tk()
subject_teacher_assignment(root)
root.mainloop()