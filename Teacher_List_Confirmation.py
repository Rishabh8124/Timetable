import json
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def Teacher_Confirmation(root):

    def add():
        id = Id_entry.get()
        name = name_entry.get()

        if (not id):
            messagebox.showwarning("WARNING", "TEACHER OD CANNOT BE EMPTY")
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

        file = open("./Academic_years/"+academic_year+"/Teacher_list.json", 'w')
        file.write(json.dumps({
            "teacher_list": teacher_list
        }))
        file.close()

        Id_entry.delete(0, END)
        name_entry.delete(0, END)

    def delete():
        selection = teacher_list_tree.focus()

        if not selection:
            messagebox.showwarning("WARNING", "SELECT A TEACHER TO SELECT")
            return
        
        selected = list(teacher_list_tree.item(selection, 'values'))
        teacher_list.remove(selected)
        teacher_list_tree.delete(selection)

        file = open("./Academic_years/"+academic_year+"/Teacher_list.json", 'w')
        file.write(json.dumps({
            "teacher_list": teacher_list
        }))
        file.close()

    with open('temp.json', 'r') as file:
        json_object = json.load(file)
        academic_year = json_object['academic_year']

    file = open("./Academic_years/"+academic_year+"/Teacher_list.json", 'r')
    teacher_list = json.load(file)["teacher_list"]
    file.close()

    for widget in root.winfo_children():
        widget.grid_forget()

    list_frame = Frame(root)
    list_frame.grid(row=0, column=0, columnspan=2)

    list_scroll = Scrollbar(list_frame, orient=VERTICAL)
    list_scroll.pack(side=RIGHT, fill='y')

    teacher_list_tree = ttk.Treeview(list_frame, height=5, yscrollcommand=list_scroll.set)
    teacher_list_tree.pack()

    list_scroll.config(command=teacher_list_tree.yview)

    teacher_list_tree["columns"] = ("TEACHER ID", "NAME")

    teacher_list_tree.column("#0", width=0, stretch=NO)

    teacher_list_tree.column("TEACHER ID", width=100, anchor=CENTER)
    teacher_list_tree.heading("TEACHER ID", text="TEACHER ID", anchor=CENTER)

    teacher_list_tree.column("NAME", width=150, anchor=CENTER)
    teacher_list_tree.heading("NAME", text="NAME", anchor=CENTER)

    for teacher in teacher_list:
        teacher_list_tree.insert(parent='', index=END, iid=teacher[0], text='', value=teacher)
    
    delete_button = Button(root, text="DELETE", command=delete)
    delete_button.grid(row=1, column=0, columnspan=2, sticky=W+E)

    Id_Label = Label(root, text="TEACHER ID: ")
    Id_Label.grid(row=2, column=0)
    
    Id_entry = Entry(root)
    Id_entry.grid(row=2, column=1)

    name_label = Label(root, text="NAME: ")
    name_label.grid(row=3, column=0)

    name_entry = Entry(root)
    name_entry.grid(row=3, column=1)
    
    add_button = Button(root, text="ADD", command=add)
    add_button.grid(row=4, column=0, columnspan=2, sticky=W+E)

root = Tk()
Teacher_Confirmation(root)
root.mainloop()