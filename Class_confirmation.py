import os
import json
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def class_confirmation(root):

    def confirm():
        os.popen('mkdir ./Academic_years/'+academic_year+'/Class')

        final_class_list = []
        subject_list = {
            "subject_list": []
        }
        json_object = json.dumps(subject_list, indent=4)
        
        for item in class_list:
            final_class_list.append(item)
            for cl in item:
                os.popen("touch ./Academic_years/"+academic_year+"/Class/"+cl+".json")
            
            for cl in item:
                file = open("./Academic_years/"+academic_year+"/Class/"+cl+".json", 'w')
                file.write(json_object)
                file.close()
        
        file = open("./Academic_years/"+academic_year+"/Class_list.json", 'w')
        class_json = {
            "class_list": final_class_list
        }
        json_object = json.dumps(class_json, indent=4)
        file.write(json_object)
        file.close()

        file = open("./Academic_years/"+academic_year+"/Teacher_list.json", 'w')
        class_json = {
            "teacher_list": []
        }
        json_object = json.dumps(class_json, indent=4)
        file.write(json_object)
        file.close()

        file = open("./Academic_years/"+academic_year+"/Lab_list.json", 'w')
        class_json = {
            "lab_list": []
        }
        json_object = json.dumps(class_json, indent=4)
        file.write(json_object)
        file.close()

        for widgets in root.winfo_children():
            widgets.destroy()

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

        dropdown = ttk.Combobox(n_root, values=["Choose Class"]+c)
        dropdown.grid(row=0, column=0)

        section_entry = Entry(n_root)
        section_entry.grid(row=0, column=1)

        but1 = Button(n_root, text="ADD", command=add)
        but1.grid(row=1, column=0)

        but2 = Button(n_root, text="BACK", command=back)
        but2.grid(row=1, column=1)

        n_root.mainloop()

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

    class_list_label = Label(root, text="CLASS LIST")
    class_list_label.grid(row=0, column=0, columnspan=3)

    for i in range(3):

        frames[i] = Frame(root)
        frames[i].grid(row=2, column=i)

        scrolls[i] = Scrollbar(frames[i], orient=VERTICAL)
        scrolls[i].pack(side=RIGHT, fill='y')

        classes[i] = ttk.Treeview(frames[i], height=5, yscrollcommand=scrolls[i].set)
        classes[i].pack()

        scrolls[i].config(command=classes[i].yview)

        classes[i]['columns'] = ("Class")

        classes[i].column("#0", width=0, stretch=NO)

        classes[i].column("Class", width=50, anchor=CENTER)
        classes[i].heading("Class", text="CLASS", anchor=CENTER)

        for class_name in class_list[i]:
            classes[i].insert(parent='', index=END, iid=class_name, text='', value=[class_name])
        
        if (i == 0): add[i] = Button(root, text="Add", command= lambda: add_command(0))
        elif (i == 1): add[i] = Button(root, text="Add", command= lambda: add_command(1))
        elif (i == 2): add[i] = Button(root, text="Add", command= lambda: add_command(2))
        add[i].grid(row=3, column=i)
        
        if (i == 0): delete[i] = Button(root, text="Delete", command= lambda: delete_command(0))
        elif (i == 1): delete[i] = Button(root, text="Delete", command= lambda: delete_command(1))
        elif (i == 2): delete[i] = Button(root, text="Delete", command= lambda: delete_command(2))
        delete[i].grid(row=4, column=i)
    
    confirm_button = Button(root, text="CONFIRM CLASSES", command=confirm)
    confirm_button.grid(row=5, column=0, columnspan=3)
