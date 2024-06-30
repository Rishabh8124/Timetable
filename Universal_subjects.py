import json
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Main_window import main_window

def universal_subjects(root):
    
    root.title("COMMON SUBJECTS")
    
    class_dict = {
        "Primary": [1, 2, 3, 4, 5],
        "Secondary": [6, 7, 8, 9, 10],
        "Higher Secondary": [11, 12]
    }
    
    subject_list = {}
    
    for i in class_dict:
        for j in class_dict[i]:
            subject_list[j] = []
    
    def div_selected(self):
        div_select = div_dropdown.get()
        class_dropdown.set("")
        class_dropdown.config(values=class_dict[div_select])
    
    def class_selected(self):
        for subject_added in subject_list_tree.get_children():
            subject_list_tree.delete(subject_added)
        
        class_name = int(class_dropdown.get())
        
        for subject_added in subject_list[class_name]:
            subject_list_tree.insert(parent='', index=END, iid=subject_added[0], text='', value=subject_added)
    
    def delete_subject():
        if not div_dropdown.get() or not class_dropdown.get():
            messagebox.showwarning("WARNING", "Select valid class")
            return
        
        subject_selected = subject_list_tree.focus()
        
        if not subject_selected:
            messagebox.showwarning("WARNING", "Select a valid subject to edit")
            return

        subject_list_tree.delete(subject_selected)
        for i in subject_list[int(class_dropdown.get())]:
            if (i[0] == subject_selected):
                subject_list[int(class_dropdown.get())].remove(i)
                return
    
    def edit_subject():
        if not div_dropdown.get() or not class_dropdown.get():
            messagebox.showwarning("WARNING", "Select valid class")
            return
        
        subject_selected = subject_list_tree.focus()
        
        if not subject_selected:
            messagebox.showwarning("WARNING", "Select a valid subject to edit")
            return
        
        subject_entry.delete(0, END)
        subject_entry.insert(0, subject_selected)
        for i in subject_list[int(class_dropdown.get())]:
            if (i[0] == subject_selected):
                count_entry.delete(0, END)
                count_entry.insert(0, i[1])
                return
    
    def add_subject():
        if not div_dropdown.get() or not class_dropdown.get():
            messagebox.showwarning("WARNING", "Select valid class")
            return
        
        subject_name = subject_entry.get().upper()
        count = count_entry.get()
        
        if count.isnumeric() == False:
            messagebox.showwarning("Warning", "Enter a valid count")
            return

        count = int(count)
        
        if not subject_name:
            messagebox.showwarning("Warning", "Enter a valid subject name")
            return

        for i in subject_list[int(class_dropdown.get())]:
            if (i[0] == subject_name and i[1] == count):
                messagebox.showinfo("INFO", "Subject already exists")
                subject_entry.delete(0, END)
                count_entry.delete(0, END)
                return
            elif (i[0] == subject_name):
                option = messagebox.askyesno("Change", "Subject already exists. Do you want to change count?")
                if option:
                    i[1] = count
                    subject_list_tree.item(subject_name, values=[subject_name, count])
                subject_entry.delete(0, END)
                count_entry.delete(0, END)
                return
        
        subject_list_tree.insert(parent='', text='', index=END, iid=subject_name, values=[subject_name, count])
        subject_list[int(class_dropdown.get())].append([subject_name, count])
        subject_entry.delete(0, END)
        count_entry.delete(0, END)
        return
    
    def finalize():
        index_dict = {
            0: "Primary",
            1: "Secondary",
            2: "Higher Secondary"
        }
        
        for i in index_dict:
            for j in class_dict[index_dict[i]]:
                for k in class_list[i]:
                    if str(j) in k:
                        for subjects in subject_list[j]:
                            json_object[k]["subject_teacher_list"][subjects[0]] = [subjects[0], subjects[1], [], [], [k], 0, [1, 1, 1, 1, 1, int(not (i == 0))], 1, 0, 0]
        
        with open("./Academic_years/"+academic_year+".json", 'w') as file:
            object = json.dumps(json_object, indent=4)
            file.write(object)
            
        for children in root.winfo_children():
            children.destroy()
        
        main_window(root)        
    
    with open("temp.json") as file:
        json_object = json.load(file)
        academic_year = json_object["academic_year"]
    
    with open("./Academic_years/"+academic_year+".json") as file:
        json_object = json.load(file)
        class_list = json_object["class_list"]
    
    style = ttk.Style(root)
    style.configure('Treeview', font=("Arial", 10))
    style.configure('Treeview.Heading', font=("Arial", 11))
    
    div_label = Label(root, text="DIVISION", font=("Arial", 11), padx=30)
    div_label.grid(row=0, column=0, pady=7, padx=10)

    div_dropdown = ttk.Combobox(root, value=list(class_dict.keys()), font=("Arial", 11))
    div_dropdown.grid(row=0, column=1, sticky=W+E, padx=10)
    div_dropdown.bind("<<ComboboxSelected>>", div_selected)

    class_label = Label(root, text="CLASS", font=("Arial", 11))
    class_label.grid(row=1, column=0, padx=10)
    
    class_dropdown = ttk.Combobox(root, value=[], font=("Arial", 11))
    class_dropdown.grid(row=1, column=1, sticky=W+E, padx=10, pady=10)
    class_dropdown.bind("<<ComboboxSelected>>", class_selected)
    
    list_frame = Frame(root)
    list_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    list_scroll = Scrollbar(list_frame, orient=VERTICAL)
    list_scroll.pack(side=RIGHT, fill='y')

    subject_list_tree = ttk.Treeview(list_frame, height=5, yscrollcommand=list_scroll.set)
    subject_list_tree.pack()

    list_scroll.config(command=subject_list_tree.yview)

    subject_list_tree["columns"] = ("SUBJECT", "COUNT")

    subject_list_tree.column("#0", width=0, stretch=NO)

    subject_list_tree.column("SUBJECT", width=150, anchor=CENTER)
    subject_list_tree.heading("SUBJECT", text="SUBJECT", anchor=CENTER)

    subject_list_tree.column("COUNT", width=150, anchor=CENTER)
    subject_list_tree.heading("COUNT", text="COUNT", anchor=CENTER)
    
    edit_button = Button(root, text="EDIT", font=("Arial", 11), padx=70, command=edit_subject)
    edit_button.grid(row=3, column=0, columnspan=1, pady=10, padx=10, sticky=W+E)
    
    delete_button = Button(root, text="DELETE", font=("Arial", 11), command=delete_subject)
    delete_button.grid(row=3, column=1, columnspan=1, pady=10, padx=10, sticky=W+E)
    
    subject_label = Label(root, text="SUBJECT", font=("Arial", 11))
    subject_label.grid(row=4, column=0, padx=10, pady=10)
    
    subject_entry = Entry(root, font=("Arial", 10))
    subject_entry.grid(row=4, column=1, padx=10, pady=10, sticky=W+E)
    
    count_label = Label(root, text="COUNT", font=("Arial", 11))
    count_label.grid(row=5, column=0, padx=10, pady=10)
    
    count_entry = Entry(root, font=("Arial", 10))
    count_entry.grid(row=5, column=1, padx=10, pady=10, sticky=W+E)
    
    add_button = Button(root, text="ADD", font=("Arial", 11), command=add_subject)
    add_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, sticky=W+E)
    
    finalize_button = Button(root, text="FINALIZE", font=("Arial", 11), command=finalize)
    finalize_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10, sticky=W+E)
    
    root.eval('tk::PlaceWindow . center')
