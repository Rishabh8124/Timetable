import json
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def subject_teacher_assignment(root, button1, button2, button3, button4):

    def back():
        for widget in root.winfo_children():
            if widget not in [button1, button2, button3, button4]:
                widget.destroy()

        button1.grid(row=0, column=0)
        button2.grid(row=1, column=0)
        button3.grid(row=2, column=0)
        button4.grid(row=3, column=0)

    def back_window(frame):
        frame.destroy()

        add_teacher_button.grid(row=9, column=1)
        delete_teacher_button.grid(row=9, column=2)

    def back_window_1(frame):
        frame.destroy()

        add_labs_button.grid(row=11, column=1)
        delete_labs_button.grid(row=11, column=2)

    def back_window_2(frame):
        frame.destroy()

        add_class_button.grid(row=13, column=1)
        delete_class_button.grid(row=13, column=2)

    def add_teacher_window(dropdown, frame):
        teacher_selected = dropdown.get()
        if (teacher_selected):
            selected_teacher_list.append(teacher_selected)
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

        with open("./Academic_years/"+academic_year+".json", 'r') as file:
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

    def add_labs_window(dropdown, frame):
        lab_selected = dropdown.get()
        if (lab_selected):
            selected_lab_list.append(lab_selected)

            labs_list_tree.insert(parent='', index=END, iid=lab_selected, text='', value=[lab_selected])

            frame.destroy()

            add_labs_button.grid(row=11, column=1)
            delete_labs_button.grid(row=11, column=2)

        elif lab_selected:
            messagebox.showwarning("WARNING", "TEACHER HAS BEEN ASSIGNED")
        else:
            messagebox.showwarning("WARNING", "SELECT A TEACHER")

    def add_lab():
        add_labs_button.grid_forget()
        delete_labs_button.grid_forget()

        with open("./Academic_years/"+academic_year+".json", 'r') as file:
            json_object = json.load(file)
            lab_list = json_object["lab_list"]
            for j in selected_lab_list:
                lab_list.remove(j)

        add_lab_frame = Frame(root)
        add_lab_frame.grid(row=11, column=0, columnspan=3)

        lab_list_dropdown = ttk.Combobox(add_lab_frame, value=lab_list)
        lab_list_dropdown.grid(row=0, column=0)

        add_button = Button(add_lab_frame, text="ADD LAB", command=lambda: add_labs_window(lab_list_dropdown, add_lab_frame))
        add_button.grid(row=0, column=1)

        back_button = Button(add_lab_frame, text="BACK", command=lambda: back_window_1(add_lab_frame))
        back_button.grid(row=0, column=2)

    def delete_lab():
        lab_selected = labs_list_tree.focus()
        if lab_selected:
            selected_lab_list.remove(lab_selected)
            labs_list_tree.delete(lab_selected)
        else:
            messagebox.showwarning("WARNING", "SELECT A LAB TO DELETE")

    def add_class_window(dropdown, frame):
        class_selected = dropdown.get()
        if class_selected:
            selected_class_list.append(class_selected)
            classes_list_tree.insert(parent='', index=END, iid=class_selected, text='', value=class_selected)
            frame.destroy()

            add_class_button.grid(row=13, column=1)
            delete_class_button.grid(row=13, column=2)
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
        add_class_frame.grid(row=13, column=0, columnspan=3)

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
            add_labs_button.config(state=NORMAL)
        else:
            if len(selected_lab_list):
                for i in selected_lab_list:
                    labs_list_tree.delete(i)
                selected_lab_list.clear()
            
            add_labs_button.config(state=DISABLED)

    def combined_teacher_check():
        pass
    
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

        file = open('./Academic_years/'+academic_year+".json", 'r')
        json_object = json.load(file)
        file.close()

        subject_list_1 = json_object[class_name]["subject_teacher_list"]

        for subject in subject_registered.get_children():
            subject_registered.delete(subject)

        for subject in subject_list_1:
            subject_registered.insert(parent='', index=END, iid=subject, text='', value=subject_list_1[subject])
        
        checkbutton_1.deselect()
        checkbutton_2.deselect()
        checkbutton_3.deselect()
        checkbutton_4.deselect()

        add_labs_button.config(state=DISABLED)
        for lab in selected_lab_list:
            labs_list_tree.delete(lab)
        selected_lab_list.clear()

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

        file = open('./Academic_years/'+academic_year+".json", 'r')
        json_object = json.load(file)
        file.close()

        subject = subject_name_entry.get()
        count = count_entry.get()
        consecutive_periods = 1
        if (checkbutton_4_var.get()):
            consecutive_periods = consecutive_periods_entry.get()
        
        if subject == '':
            messagebox.showwarning("WARNING", "SUBJECT NAME IS EMPTY")
            return
        if count.isnumeric() == False:
            messagebox.showwarning("WARNING", "COUNT SHOULD BE AN INTEGER")
            return
        if checkbutton_1_var.get() and selected_lab_list == []:
            messagebox.showwarning("WARNING", "LAB NAME IS EMPTY")
            return
        if checkbutton_4_var.get() and consecutive_periods.isnumeric() == False:
            messagebox.showwarning("WARNING", "CONSECUTIVE PERIODS SHOULD BE AN INTEGER")
            return
        
        for class_added in selected_class_list:
            if json_object[class_added]["subject_teacher_list"].get(subject, False):
                confirm = messagebox.askyesno("CONFIRM", "CLASS "+class_added+" HAS THIS SUBJECT REGISTERED. DO YOU WANT TO SAVE CHANGES?")
                if not confirm:
                    return
        
        class_name = class_dropdown.get()
        details = [subject, count, selected_teacher_list, selected_lab_list, selected_class_list, consecutive_periods, checkbutton_3_var.get(), 0]

        if subject in subject_registered.get_children():
            old_details = json_object[class_name]["subject_teacher_list"][subject]
            details[-1] = old_details[-1]

            if old_details[-1]:
                if int(old_details[-1] > int(count)):
                    messagebox.showwarning("WARNING", "Timetable slots have been assigned for this subject. New limit exceeds the current alloted slots")
                    return

                if old_details[3] != selected_lab_list:
                    if sorted(old_details[3]) != sorted(selected_lab_list):
                        messagebox.showwarning("WARNING", "Timetable slots have been assigned for this subject. Lab list cannot be modified")
                        return
                
                if old_details[4] != selected_class_list:
                    if sorted(old_details[4]) != sorted(selected_class_list):
                        messagebox.showwarning("WARNING", "Timetable slots have been assigned for this subject. Class list cannot be modified")
                        return

                teacher_condition = checkbutton_3_var.get()

                if old_details[-2] != teacher_condition:
                    messagebox.showwarning("WARNING", "Timetable slots have been assigned for this subject. Teacher assignment type cannot be changed")
                    return
                
                elif sorted(old_details[2]) != sorted(selected_teacher_list):
                    if old_details[-2] == 0:
                        if old_details[2]:
                            if selected_teacher_list == []:
                                current_timetable = json_object[class_name]["timetable"]
                                for i in range(len(current_timetable)):
                                    for j in range(len(current_timetable[i])):
                                        if current_timetable[i][j] and current_timetable[i][j].split('::')[0] == subject:
                                            json_object[current_timetable[i][j].split('::')[1]]["timetable"][i][j] = ""
                                            current_timetable[i][j] = subject

                            else:
                                current_timetable = json_object[class_name]["timetable"]

                                for i in range(len(current_timetable)):
                                    for j in range(len(current_timetable[i])):
                                        if current_timetable[i][j] and current_timetable[i][j].split('::')[0] == subject:
                                            if current_timetable[i][j].split('::')[1] in old_details[2] and current_timetable[i][j].split('::')[1] not in selected_teacher_list:
                                                messagebox.showwarning("WARNING", current_timetable[i][j].split('::')[1]+" has assigned slots for this subject.")
                                                return

                        else:
                            if (len(selected_teacher_list) > 1):
                                messagebox.showwarning("WARNING", "Ambiguity in assigning subject slots to teachers")
                                return
                            else:
                                current_timetable = json_object[class_name]["timetable"]

                                for i in range(len(current_timetable)):
                                    for j in range(len(current_timetable[i])):
                                        if current_timetable[i][j] == subject:
                                            current_timetable[i][j] = subject+'::'+selected_teacher_list[0]
                                            json_object[selected_teacher_list[0]]["timetable"][i][j] = selected_class_list

                    else:
                        current_timetable = json_object[class_name]["timetable"]

                        for i in range(len(current_timetable)):
                            for j in range(len(current_timetable[i])):
                                if current_timetable[i][j] == subject:
                                    for teachers in selected_teacher_list:
                                        if teachers not in old_details[2] and json_object[teachers]["timetable"][i][j]:
                                            messagebox.showwarning("WARNING", teachers+' has class aloted in slots of the subject')
                                            return
                        
                        for i in range(len(current_timetable)):
                            for j in range(len(current_timetable[i])):
                                if current_timetable[i][j] == subject:
                                    for teachers in old_details[2]:
                                        json_object[teachers]["timetable"][i][j] = ''
                                    for teachers in selected_teacher_list:
                                        json_object[teachers]["timetable"][i][j] = selected_class_list

            for class_added in old_details[4]:
                json_object[class_added]["subject_teacher_list"].pop(subject)
            
            for teachers in old_details[2]:
                json_object[teachers]['class_list'].get(subject, 0).remove(old_details[4])

            for labs in old_details[3]:
                json_object[labs]['class_list'][subject].remove(old_details[4])
        
            subject_registered.delete(subject)

        subject_registered.insert(parent='', text='', index=END, iid=subject, value=details)

        for class_added in classes_list_tree.get_children():
            classes_list_tree.delete(class_added)
        classes_list_tree.insert(parent='', index=END, iid=class_name, text='', value=class_name)
        
        for teachers in selected_teacher_list:
            subject_list = json_object[teachers]['class_list'].get(subject, [])
            subject_list.append(selected_class_list)
            json_object[teachers]["class_list"][subject] = subject_list
        
        for labs in selected_lab_list:
            subject_list = json_object[labs]['class_list'].get(subject, [])
            subject_list.append(selected_class_list)
            json_object[labs]["class_list"][subject] = subject_list
        
        for class_added in selected_class_list:
            json_object[class_added]["subject_teacher_list"][subject] = details

        with open('./Academic_years/'+academic_year+".json", 'w') as file:
            file.write(json.dumps(json_object, indent=4))

        checkbutton_1.deselect()
        checkbutton_2.deselect()
        checkbutton_3.deselect()
        checkbutton_4.deselect()

        subject_name_entry.delete(0, END)
        count_entry.delete(0, END)

        for lab in selected_lab_list:
            labs_list_tree.delete(lab)

        for teacher in teachers_list_tree.get_children():
            teachers_list_tree.delete(teacher)

        selected_teacher_list.clear()
        selected_lab_list.clear()
        selected_class_list.clear()

        selected_class_list.append(class_name)

        add_teacher_button.config(state=NORMAL)
        add_class_button.config(state=DISABLED)
        delete_class_button.config(state=DISABLED)
        consecutive_periods_entry.delete(0, END)
        consecutive_periods_entry.config(state=DISABLED)
    
    def edit_details():
        class_name = class_dropdown.get()

        with open('./Academic_years/'+academic_year+".json", 'r') as file:
            subject_list = json.load(file)[class_name]["subject_teacher_list"]

        checkbutton_1.deselect()
        checkbutton_2.deselect()
        checkbutton_3.deselect()
        checkbutton_4.deselect()

        subject_name_entry.delete(0, END)
        count_entry.delete(0, END)

        for teacher in teachers_list_tree.get_children():
            teachers_list_tree.delete(teacher)
        
        for class_added in selected_class_list:
            if (class_added != class_name): classes_list_tree.delete(class_added)
        selected_class_list.clear()
        selected_class_list.append(class_name)

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

        for lab in selected_lab_list:
            labs_list_tree.delete(lab)
        selected_lab_list.clear()

        if selected_list[3]:
            checkbutton_1.select()
            add_labs_button.config(state=NORMAL)
            for lab in selected_list[3]:
                selected_lab_list.append(lab)
                labs_list_tree.insert(parent='', text='', index=END, iid=lab, value=[lab])
        else:
            pass
        
        if len(selected_list[4]) > 1:
            checkbutton_2.select()
            delete_class_button.config(state=NORMAL)
            add_class_button.config(state=NORMAL)
            for class_selected in selected_list[4]:
                if class_selected != class_name:
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

    def clear_details():
        selected_subject = subject_registered.focus()
        if not selected_subject:
            messagebox.showwarning("WARNING", "SELECT SUBJECT TO CLEAR")
            return

        class_name = class_dropdown.get()

        with open('./Academic_years/'+academic_year+".json", 'r') as file:
            json_object = json.load(file)
        
        if json_object[class_name]["subject_teacher_list"][selected_subject][-1]:
            messagebox.showwarning("WARNING", "Slots have been assigned for this subject")
            return
        
        subject_registered.delete(selected_subject)
        classes = json_object[class_name]["subject_teacher_list"][selected_subject][4]
        teachers = json_object[class_name]["subject_teacher_list"][selected_subject][2]
        labs = json_object[class_name]["subject_teacher_list"][selected_subject][3]

        for class_added in classes:
            json_object[class_added]["subject_teacher_list"].pop(selected_subject)
        
        for teacher in teachers:
            json_object[teacher]["class_list"].get(selected_subject).remove(classes)

        for lab in labs:
            json_object[lab]["class_list"].get(selected_subject).remove(classes)

        with open('./Academic_years/'+academic_year+".json", 'w') as file:
            file.write(json.dumps(json_object, indent=4))

    selected_teacher_list = []
    selected_class_list = []
    selected_lab_list = []
    
    with open("temp.json") as file:
        json_object = json.load(file)
        academic_year = json_object["academic_year"]
    
    with open("./Academic_years/"+academic_year+".json") as file:
        json_object = json.load(file)
        class_list = json_object["class_list"]
        class_list_combined = []

        for i in class_list:
            class_list_combined.extend(i)

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

    subject_registered.column("LAB", width=200, anchor=CENTER)
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
    checkbutton_1.grid(row=10, column=0, rowspan=2)

    labs_frame = Frame(root)
    labs_frame.grid(row=10, column=1, columnspan=2)

    labs_scroll = Scrollbar(labs_frame, orient=VERTICAL)
    labs_scroll.pack(side=RIGHT, fill='y')

    labs_list_tree = ttk.Treeview(labs_frame, height=5, yscrollcommand=labs_scroll.set)
    labs_list_tree.pack()

    labs_scroll.config(command=labs_list_tree.yview)

    labs_list_tree["columns"] = ("LABS")

    labs_list_tree.column("#0", width=0, stretch=NO)

    labs_list_tree.column("LABS", anchor=CENTER)
    labs_list_tree.heading("LABS", text="LABS", anchor=CENTER)

    add_labs_button = Button(root, text="ADD LAB", command=add_lab, state=DISABLED)
    add_labs_button.grid(row=11, column=1)

    delete_labs_button = Button(root, text="DELETE LAB", command=delete_lab)
    delete_labs_button.grid(row=11, column=2)

    checkbutton_2_var = IntVar()
    checkbutton_2 = Checkbutton(root, text="COMBINED CLASS", onvalue=1, offvalue=0, variable=checkbutton_2_var, command=combined_class_check)
    checkbutton_2.grid(row=12, column=0)

    classes_frame = Frame(root)
    classes_frame.grid(row=12, column=1, columnspan=2)

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
    add_class_button.grid(row=13, column=1)

    delete_class_button = Button(root, text="DELETE CLASS", command=delete_class, state=DISABLED)
    delete_class_button.grid(row=13, column=2)

    checkbutton_4_var = IntVar()
    checkbutton_4 = Checkbutton(root, text="CONSECUTIVE PERIODS", onvalue=1, offvalue=0, variable=checkbutton_4_var, command=consecutive_periods_check)
    checkbutton_4.grid(row=14, column=0)

    consecutive_periods_entry = Entry(root, state=DISABLED)
    consecutive_periods_entry.grid(row=14, column=1, columnspan=2)

    save_button = Button(root, text="SAVE DETAILS", command=save_details, state=DISABLED)
    save_button.grid(row=15, column=0, columnspan=3)

    back_button = Button(root, text="BACK", command=back)
    back_button.grid(row=16, column=0, columnspan=3)
