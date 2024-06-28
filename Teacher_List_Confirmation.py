import json
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def Teacher_Confirmation(root, button1, button2, button3, button4, button5):
    
    root.title("Teacher List")

    def back_1():
        Id_Label.config(text="TEACHER ID")
        name_label.config(text="NAME")
        add_button.config(text="ADD", command=add)

        back_button_1.grid_forget()
        add_button.grid_forget()
        add_button.grid(row=4, column=0, columnspan=2, sticky=W+E, padx=10)

    def confirm():
        for widget in root.winfo_children():
            if widget not in [button1, button2, button3, button4, button5]:
                widget.destroy()

        button1.grid(row=0, column=0, padx=20, pady=12)
        button2.grid(row=2, column=0, padx=20, pady=12)
        button3.grid(row=3, column=0, padx=20)
        button4.grid(row=4, column=0, padx=20, pady=12)
        button5.grid(row=1, column=0, padx=20)
        root.title("TIMETABLE")
        root.eval('tk::PlaceWindow . center')

    def add():
        id = Id_entry.get()
        name = name_entry.get()

        if (not id):
            messagebox.showwarning("WARNING", "TEACHER ID CANNOT BE EMPTY")
            return
        
        if (not name):
            messagebox.showwarning("WARNING", "NAME CANNOT BE EMPTY")
            return
        
        for teacher in teacher_list:
            if teacher[0] == id and teacher[1].lower() == name.lower():
                Id_entry.delete(0, END)
                name_entry.delete(0, END)
                messagebox.showinfo("DUPLICATE", "TEACHER HAS ALREADY BEEN ADDED")
                return
            elif teacher[0] == id:
                messagebox.showwarning("WARNING", "TEACHER ID FOUND FOR DIFFERENT TEACHER")
                return
            elif teacher[0] != id and teacher[1].lower() == name.lower():
                ans = messagebox.askyesno("CONFIRM", "TEACHER NAME EXISTS WITH DIFFERENT ID\nADD NEW TEACHER?")
                if not ans:
                    Id_entry.delete(0, END)
                    name_entry.delete(0, END)
                    return
        
        teacher_list.append([id, name])
        teacher_list_tree.insert(parent='', index=END, iid=id, value=[id, name], text='')

        file = open("./Academic_years/"+academic_year+".json", 'r')
        file_data = json.load(file)
        file.close()

        file_data["teacher_list"] = teacher_list
        file_data[id+"-"+name] = {
            "timetable" : [
                ["", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", ""]
            ], "class_list" : {}
        }
        
        file = open("./Academic_years/"+academic_year+".json", 'w')
        file.write(json.dumps(file_data, indent=4))
        file.close()

        Id_entry.delete(0, END)
        name_entry.delete(0, END)

    def delete():
        selection = teacher_list_tree.focus()

        if not selection:
            messagebox.showwarning("WARNING", "SELECT A TEACHER TO DELETE")
            return
        
        selected = list(teacher_list_tree.item(selection, 'values'))
        
        teacher_timetable = json_object[selected[0]+"-"+selected[1]]['timetable']
        for i in range(len(teacher_timetable)):
            for j in range(len(teacher_timetable[i])):
                if teacher_timetable[i][j]:
                    messagebox.showwarning("WARNING", "Teacher has assigned slots")
                    return

        classes_handling = json_object[selected[0]+"-"+selected[1]]['class_list']
        for subjects in classes_handling:
            for classes_list in classes_handling[subjects]:
                for classes in classes_list:
                    json_object[classes]["subject_teacher_list"][subjects][2].remove(selected[0]+"-"+selected[1])
        
        teacher_list.remove(selected)
        teacher_list_tree.delete(selection)

        json_object["teacher_list"] = teacher_list
        json_object.pop(selected[0]+"-"+selected[1])
        
        file = open("./Academic_years/"+academic_year+".json", 'w')
        file.write(json.dumps(json_object, indent=4))
        file.close()

        file.close()

    def edit_replace():
        selection = teacher_list_tree.focus()

        if not selection:
            messagebox.showwarning("WARNING", "SELECT A TEACHER TO EDIT")
            return
        
        selected = list(teacher_list_tree.item(selection, 'values'))

        Id_Label.config(text=selected[0])
        name_label.config(text=selected[1])
        add_button.config(text="SAVE", command=save)

        add_button.grid_forget()
        add_button.grid(row=4, column=0, sticky=W+E, padx=10)
        back_button_1.grid(row=4, column=1, sticky=W+E, padx=10)

    def save():
        id = Id_entry.get()
        name = name_entry.get()

        old_id = Id_Label.cget("text")
        old_name = name_label.cget("text")

        if (not id):
            messagebox.showwarning("WARNING", "TEACHER ID CANNOT BE EMPTY")
            return
        
        if (not name):
            messagebox.showwarning("WARNING", "NAME CANNOT BE EMPTY")
            return
        
        if id == old_id:
            if old_name == name:
                back_1()
                return
            else:
                for teacher in teacher_list:
                    if teacher[0] != id and teacher[1].lower() == name.lower():
                        ans = messagebox.askyesno("CONFIRM", "TEACHER NAME EXISTS WITH DIFFERENT ID\nADD NEW TEACHER?")
                        if not ans:
                            back_1()
                            return

        else:        
            for teacher in teacher_list:
                if teacher[0] == id and teacher[1].lower() == name.lower():
                    Id_entry.delete(0, END)
                    name_entry.delete(0, END)
                    messagebox.showinfo("DUPLICATE", "TEACHER HAS ALREADY BEEN ADDED")
                    return
                elif teacher[0] == id:
                    messagebox.showwarning("WARNING", "TEACHER ID FOUND FOR DIFFERENT TEACHER")
                    return
                elif teacher[0] != id and teacher[1].lower() == name.lower():
                    ans = messagebox.askyesno("CONFIRM", "TEACHER NAME EXISTS WITH DIFFERENT ID\nADD NEW TEACHER?")
                    if not ans:
                        Id_entry.delete(0, END)
                        name_entry.delete(0, END)
                        return
        
        index = json_object["teacher_list"].index([old_id, old_name])
        json_object["teacher_list"][index] = [id, name]

        json_object[id+"-"+name] = json_object[old_id+"-"+old_name]
        json_object.pop(old_id+"-"+old_name)

        current_timetable = json_object[id+'-'+name]['timetable']
        for i in range(len(current_timetable)):
            for j in range(len(current_timetable[i])):
                if current_timetable[i][j]:
                    for classes in current_timetable[i][j]:
                        if '::' in json_object[classes]['timetable'][i][j] and json_object[classes]['timetable'][i][j].split('::')[1] == old_id+'-'+old_name:
                            json_object[classes]['timetable'][i][j] = json_object[classes]['timetable'][i][j].split('::')[0]+'::'+id+'-'+name

        for subject in json_object[id+'-'+name]['class_list']:
            for class_set in json_object[id+'-'+name]['class_list'][subject]:
                for classes in class_set:
                    index = json_object[classes]['subject_teacher_list'][subject][2].index(old_id+'-'+old_name)
                    json_object[classes]['subject_teacher_list'][subject][2][index] = id+'-'+name

        teacher_list_tree.delete(old_id)
        teacher_list_tree.insert(parent='', index=END, iid=id, text='', value=[id, name])

        Id_Label.config(text="TEACHER ID")
        name_label.config(text="NAME")
        add_button.config(text="ADD", command=add)

        back_button_1.grid_forget()
        add_button.grid_forget()
        add_button.grid(row=4, column=0, columnspan=2, sticky=W+E, padx=10)

        file = open("./Academic_years/"+academic_year+".json", 'w')
        file.write(json.dumps(json_object, indent=4))
        file.close()

        Id_entry.delete(0, END)
        name_entry.delete(0, END)

    with open('temp.json', 'r') as file:
        json_object = json.load(file)
        academic_year = json_object['academic_year']

    style = ttk.Style(root)
    style.configure('Treeview', font=("Arial", 10))
    style.configure('Treeview.Heading', font=("Arial", 11))
    
    file = open("./Academic_years/"+academic_year+".json", 'r')
    json_object = json.load(file)
    teacher_list = json_object["teacher_list"]
    file.close()

    list_frame = Frame(root)
    list_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    list_scroll = Scrollbar(list_frame, orient=VERTICAL)
    list_scroll.pack(side=RIGHT, fill='y')

    teacher_list_tree = ttk.Treeview(list_frame, height=5, yscrollcommand=list_scroll.set)
    teacher_list_tree.pack()

    list_scroll.config(command=teacher_list_tree.yview)

    teacher_list_tree["columns"] = ("TEACHER ID", "NAME")

    teacher_list_tree.column("#0", width=0, stretch=NO)

    teacher_list_tree.column("TEACHER ID", width=150, anchor=CENTER)
    teacher_list_tree.heading("TEACHER ID", text="TEACHER ID", anchor=CENTER)

    teacher_list_tree.column("NAME", width=150, anchor=CENTER)
    teacher_list_tree.heading("NAME", text="NAME", anchor=CENTER)

    for teacher in teacher_list:
        teacher_list_tree.insert(parent='', index=END, iid=teacher[0], text='', value=teacher)
    
    edit_button = Button(root, text="EDIT", command=edit_replace, font=("Arial", 11))
    edit_button.grid(row=1, column=0, sticky=W+E, padx=10, pady=5)

    delete_button = Button(root, text="DELETE", command=delete, font=("Arial", 11))
    delete_button.grid(row=1, column=1, sticky=W+E, padx=10, pady=5)

    Id_Label = Label(root, text="TEACHER ID: ", font=("Arial", 11))
    Id_Label.grid(row=2, column=0, pady=5)
    
    Id_entry = Entry(root, font=("Arial", 11))
    Id_entry.grid(row=2, column=1, pady=5)

    name_label = Label(root, text="NAME: ", font=("Arial", 11))
    name_label.grid(row=3, column=0, pady=5)

    name_entry = Entry(root, font=("Arial", 11))
    name_entry.grid(row=3, column=1, pady=5)
    
    add_button = Button(root, text="ADD", command=add, font=("Arial", 11))
    add_button.grid(row=4, column=0, columnspan=2, sticky=W+E, pady=5, padx=10)

    back_button_1 = Button(root, text="CANCEL", command=back_1, font=("Arial", 11))

    back_button = Button(root, text="BACK", command=confirm, font=("Arial", 11))
    back_button.grid(row=5, column=0, columnspan=2, sticky=W+E, pady=5, padx=10)
    
    root.eval('tk::PlaceWindow . center')

