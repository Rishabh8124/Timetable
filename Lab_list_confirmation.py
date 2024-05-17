import os
import json
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def lab_confirmation(root):
    def add():
        name = name_entry.get()
        
        if (not name):
            messagebox.showwarning("WARNING", "NAME CANNOT BE EMPTY")
            return
        
        for lab in lab_list:
            if lab == name:
                messagebox.showinfo("DUPLICATE", "LAB HAS ALREADY BEEN ADDED")
                return
        
        lab_list.append(name)
        lab_list_tree.insert(parent='', index=END, iid=name, value=[name], text='')

        file = open("./Academic_years/"+academic_year+".json", 'r')
        file_data = json.load(file)
        file.close()

        file_data["lab_list"] = lab_list
        file_data[name] = {}

        file = open("./Academic_years/"+academic_year+".json", 'w')
        file.write(json.dumps(file_data, indent=4))
        file.close()

        name_entry.delete(0, END)

    def delete():
        selection = lab_list_tree.focus()

        if not selection:
            messagebox.showwarning("WARNING", "SELECT A LAB TO SELECT")
            return
        
        lab_list.remove(selection)
        lab_list_tree.delete(selection)

        file = open("./Academic_years/"+academic_year+".json", 'r')
        file_data = json.load(file)
        file.close()

        file_data["lab_list"] = lab_list
        file_data.pop(selection)

        file = open("./Academic_years/"+academic_year+".json", 'w')
        file.write(json.dumps(file_data, indent=4))
        file.close()

    def finalize():
        
        for widget in root.winfo_children():
            widget.destroy()

    with open('temp.json', 'r') as file:
        json_object = json.load(file)
        academic_year = json_object['academic_year']

    file = open("./Academic_years/"+academic_year+".json", 'r')
    lab_list = json.load(file)["lab_list"]
    file.close()

    for widget in root.winfo_children():
        widget.grid_forget()

    list_frame = Frame(root)
    list_frame.grid(row=0, column=0, columnspan=2, sticky=W+E)

    list_scroll = Scrollbar(list_frame, orient=VERTICAL)
    list_scroll.pack(side=RIGHT, fill='y')

    lab_list_tree = ttk.Treeview(list_frame, height=5, yscrollcommand=list_scroll.set)
    lab_list_tree.pack()

    list_scroll.config(command=lab_list_tree.yview)

    lab_list_tree["columns"] = ("NAME")

    lab_list_tree.column("#0", width=0, stretch=NO)

    lab_list_tree.column("NAME", anchor=CENTER)
    lab_list_tree.heading("NAME", text="LAB NAME", anchor=CENTER)
    
    delete_button = Button(root, text="DELETE", command=delete)
    delete_button.grid(row=1, column=0, columnspan=2, sticky=W+E)

    name_label = Label(root, text="LAB NAME: ")
    name_label.grid(row=3, column=0)

    name_entry = Entry(root)
    name_entry.grid(row=3, column=1)
    
    add_button = Button(root, text="ADD", command=add)
    add_button.grid(row=4, column=0, columnspan=2, sticky=W+E)

    finalize_button = Button(root, text="FINALIZE", command=finalize)
    finalize_button.grid(row=5, column=0, columnspan=2, sticky=W+E)
