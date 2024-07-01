import os
import json
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Lab_list_confirmation import lab_confirmation

def class_confirmation(root, import_option):

    root.title("Class List")
    
    def confirm():
        academic_year_dictionary = {}
        final_class_list = []
        timetable = [
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", ""]
        ]
        
        for item in class_list:
            final_class_list.append(item)            
            for cl in item:
                academic_year_dictionary[cl] = {
                    "subject_teacher_list": {},
                    "timetable": timetable,
                    "teacher": ""
                }

        academic_year_dictionary["class_list"] = final_class_list
        academic_year_dictionary["teacher_list"] = []
        academic_year_dictionary["lab_list"] = []
        academic_year_dictionary["class_teachers"] = []

        file = open("./Academic_years/"+academic_year+".json", 'w')
        file.write(json.dumps(academic_year_dictionary, indent=4))
        file.close()

        for widgets in root.winfo_children():
            widgets.destroy()
        
        lab_confirmation(root)

    def delete_command(index):
        current = classes[index].selection()
        for i in current:
            classes[index].delete(i)
            class_list[index].remove(i)

    def add_command(index):
        if index==0 :
            c = [1, 2, 3, 4, 5]
        elif index==1:
            c = [6, 7, 8, 9, 10]
        else:
            c = [11, 12]
        
        def add():
            cl_number = dropdown.get()
            cl_sec = section_entry.get()

            if (cl_number == "Choose Class" or cl_sec == ""):
                messagebox.showwarning("WARNING", "Fill all fields")
            elif cl_number+cl_sec in class_list[index]:
                messagebox.showwarning("WARNING", "Class already exists")
            else:
                for item in classes[index].get_children():
                    classes[index].delete(item)

                class_list[index].append(cl_number+cl_sec)
                class_list[index].sort()

                for item in class_list[index]:
                    classes[index].insert(parent='', index=END, iid=item, text='', value=[item])
                
                n_root.destroy()

        def back():
            n_root.destroy()

        n_root = Tk()
        n_root.title("ADD CLASS")
        
        class_label = Label(n_root, text="CLASS", font=("Arial", 11))
        class_label.grid(row=0, column=0, padx=70, pady=15)

        dropdown = ttk.Combobox(n_root, values=["Choose Class"]+c, font=("Arial", 11))
        dropdown.grid(row=0, column=1, padx=10)
        
        sec_label = Label(n_root, text="SECTION", font=("Arial", 11))
        sec_label.grid(row=1, column=0)

        section_entry = Entry(n_root, font=("Arial", 11))
        section_entry.grid(row=1, column=1)

        but1 = Button(n_root, text="ADD", command=add, font=("Arial", 12))
        but1.grid(row=2, column=0, sticky=W+E, padx=10, pady=15)

        but2 = Button(n_root, text="BACK", command=back, font=("Arial", 12))
        but2.grid(row=2, column=1, sticky=W+E, padx=10, pady=10)
        
        n_root.eval('tk::PlaceWindow . center')

        n_root.mainloop()

    def back():
        for widgets in root.winfo_children():
            widgets.destroy()
        
        import_option(root)
    
    with open('temp.json', 'r') as file:
        json_object = json.load(file)
        academic_year = json_object['academic_year']
    
    class_list = [[], [], []]
    frames = [None, None, None]
    scrolls = [None, None, None]
    classes = [None, None, None]
    delete = [None, None, None]
    add = [None, None, None]

    with open('defaults.json', 'r') as file:
        json_object = json.load(file)
        for i in json_object["class_list"]:
            for j in json_object["class_list"][i]:
                class_list[(int(i) > 5) + (int(i) > 10)].append(i+j)

    class_list_label = Label(root, text="CLASS LIST", font=("Arial", 13))
    class_list_label.grid(row=0, column=0, columnspan=3, pady=8)
    
    style = ttk.Style(root)
    style.configure('Treeview', font=("Arial", 10))
    style.configure('Treeview.Heading', font=("Arial", 11))

    for i in range(3):

        frames[i] = Frame(root)
        frames[i].grid(row=2, column=i, padx=10)

        scrolls[i] = Scrollbar(frames[i], orient=VERTICAL)
        scrolls[i].pack(side=RIGHT, fill='y')

        classes[i] = ttk.Treeview(frames[i], height=4, yscrollcommand=scrolls[i].set)
        classes[i].pack()

        scrolls[i].config(command=classes[i].yview)

        classes[i]['columns'] = ("Class")

        classes[i].column("#0", width=0, stretch=NO)

        classes[i].column("Class", width=70, anchor=CENTER)
        classes[i].heading("Class", text="CLASS", anchor=CENTER)

        for class_name in class_list[i]:
            classes[i].insert(parent='', index=END, iid=class_name, text='', value=[class_name])
        
        if (i == 0): add[i] = Button(root, text="ADD", command= lambda: add_command(0), font=("Arial", 10))
        elif (i == 1): add[i] = Button(root, text="ADD", command= lambda: add_command(1), font=("Arial", 10))
        elif (i == 2): add[i] = Button(root, text="ADD", command= lambda: add_command(2), font=("Arial", 10))
        add[i].grid(row=3, column=i, sticky=W+E, padx=10, pady=8)
        
        if (i == 0): delete[i] = Button(root, text="DELETE", command= lambda: delete_command(0), font=("Arial", 10))
        elif (i == 1): delete[i] = Button(root, text="DELETE", command= lambda: delete_command(1), font=("Arial", 10))
        elif (i == 2): delete[i] = Button(root, text="DELETE", command= lambda: delete_command(2), font=("Arial", 10))
        delete[i].grid(row=4, column=i, sticky=W+E, padx=10)
    
    confirm_button = Button(root, text="CONFIRM CLASSES", command=confirm, font=("Arial", 11))
    confirm_button.grid(row=5, column=0, columnspan=2, pady=8, padx=10, sticky=W+E)
    
    confirm_button = Button(root, text="BACK", command=back, font=("Arial", 11))
    confirm_button.grid(row=5, column=2, pady=8, padx=10, sticky=W+E)
    
    root.eval('tk::PlaceWindow . center')

# root = Tk()
# class_confirmation(root, 1)
# root.mainloop()
