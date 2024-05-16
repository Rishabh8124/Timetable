import json
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def Subject_Registration(root):

    def div_selected(self):
        div_select = div_dropdown.get()
        class_dropdown.config(values=class_list[class_division[div_select]])

    def class_selected(self):
        class_name = class_dropdown.get()
        file = open('./Academic_years/'+academic_year+'/Class/'+class_name+".json", 'r')
        json_object = json.load(file)
        file.close()

        subject_list = json_object["subject_list"]

        for subject in subject_registered.get_children():
            subject_registered.delete(subject)

        for subject in subject_list:
            subject_registered.insert(parent='', index=END, iid=subject[0], text='', value=subject)
    
    def delete():
        class_name = class_dropdown.get()
        file = open('./Academic_years/'+academic_year+'/Class/'+class_name+".json", 'r')
        json_object = json.load(file)
        file.close()
        subject_list = json_object['subject_list']

        selected_subject = subject_registered.focus()

        if (selected_subject == '') :
            messagebox.showwarning("WARNING", 'CHOOSE A SUBJECT TO DELETE')
            return

        selection = list(subject_registered.item(selected_subject, 'values'))
        selection[1] = int(selection[1])

        subject_registered.delete(selected_subject)
        subject_list.remove(selection)

        json_object["subject_list"] = subject_list
        file = open('./Academic_years/'+academic_year+'/Class/'+class_name+".json", 'w')
        file.write(json.dumps(json_object))
        file.close()

    def add():
        class_name = class_dropdown.get()
        file = open('./Academic_years/'+academic_year+'/Class/'+class_name+".json", 'r')
        json_object = json.load(file)
        file.close()
        subject_list = json_object['subject_list']

        if class_name == "":
            messagebox.showwarning("WARNING", "CHOOSE A CLASS")
            return

        subject_name = subject_name_entry.get()
        count = count_entry.get()

        condition = False
        total_count = 0

        if (count.isnumeric() == False):
            condition = True
        else:
            count = int(count)
        
        if subject_name == '':
            condition = True

        for subject in subject_list:
            total_count += int(subject[1])
            if (subject[0] == subject_name):
                condition = True
                messagebox.showwarning("WARNING", "SUBJECT ALREADY EXISTS")
        
        if condition == False and (total_count + count > 47):
            condition = True
            messagebox.showwarning("WARNING", "NO OF PERIODS COUNT EXCEEDS MAXIMUM LIMIT")
        
        if (condition == False):
            subject_registered.insert(parent='', index=END, iid=subject_name, text='', value=[subject_name, count])

            subject_list.append([subject_name, count])
            json_object["subject_list"] = subject_list
            file = open('./Academic_years/'+academic_year+'/Class/'+class_name+".json", 'w')
            file.write(json.dumps(json_object))
            file.close()

    with open("temp.json") as file:
        json_object = json.load(file)
        academic_year = json_object["academic_year"]
    
    with open("./Academic_years/"+academic_year+"/Class_list.json") as file:
        json_object = json.load(file)
        class_list = json_object["class_list"]

    class_list = [[""]]+class_list    
    class_division = {"": 0, "Primary": 1, "Secondary": 2, "Higher Secondary": 3}

    div_dropdown = ttk.Combobox(root, value=list(class_division.keys()))
    div_dropdown.grid(row=0, column=0, columnspan=2, sticky=W+E)
    div_dropdown.bind("<<ComboboxSelected>>", div_selected)

    class_dropdown = ttk.Combobox(root, value=class_list[0])
    class_dropdown.grid(row=1, column=0, columnspan=2, sticky=W+E)
    class_dropdown.bind("<<ComboboxSelected>>", class_selected)

    subject_frame = Frame(root)
    subject_frame.grid(row=2, column=0, columnspan=2)

    scroll = Scrollbar(subject_frame, orient=VERTICAL)
    scroll.pack(side=RIGHT, fill='y')

    subject_registered = ttk.Treeview(subject_frame, height=5, yscrollcommand=scroll.set)
    subject_registered.pack()

    scroll.config(command=subject_registered.yview)

    subject_registered["columns"] = ("SUBJECT", "NO OF PERIODS")

    subject_registered.column("#0", width=0, stretch=NO)

    subject_registered.column("SUBJECT", anchor=CENTER)
    subject_registered.heading("SUBJECT", text="SUBJECT", anchor=CENTER)

    subject_registered.column("NO OF PERIODS", anchor=CENTER)
    subject_registered.heading("NO OF PERIODS", text="NO OF PERIODS", anchor=CENTER)

    subject_name_label =  Label(root, text="SUBJECT NAME: ")
    subject_name_label.grid(row=4, column=0)

    count_label = Label(root, text="NO OF PERIODS: ")
    count_label.grid(row=5, column=0)

    subject_name_entry = Entry(root)
    subject_name_entry.grid(row=4, column=1)

    count_entry = Entry(root)
    count_entry.grid(row=5, column=1)

    add_button = Button(root, text="ADD SUBJECT", command=add)
    add_button.grid(row=6, column=0, columnspan=2)

    delete_button = Button(root, text="DELETE SUBJECT", command=delete)
    delete_button.grid(row=3, column=0, columnspan=2)

root = Tk()
Subject_Registration(root)
root.mainloop()