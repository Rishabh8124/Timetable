import json
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def timetable(root, button1, button2, button3, button4):

    def back():
        for widget in root.winfo_children():
            if widget not in [button1, button2, button3, button4]:
                widget.destroy()

        button1.grid(row=0, column=0)
        button2.grid(row=1, column=0)
        button3.grid(row=2, column=0)
        button4.grid(row=3, column=0)

    def div_selected(self):
        div_select = div_dropdown.get()
        class_dropdown.config(values=class_list[class_division[div_select]])

    def class_selected(self):
        class_name = class_dropdown.get()

        file = open('./Academic_years/'+academic_year+".json", 'r')
        json_object = json.load(file)
        file.close()

        class_details = json_object[class_name]
        subject_details = class_details["subject_teacher_list"]
        class_timetable = class_details["timetable"]

        final_subject_list = ['']
        for children in subject_registered.get_children():
            subject_registered.delete(children)

        for i in subject_details.values():
            subject_registered.insert(parent='', text='', index=END, iid=i[0], value=[i[0], str(i[-1])+'/'+str(i[1])])
            if (i[-2] == 1 or i[2] == []):
                final_subject_list.append(i[0])
            else:
                for j in i[2]:
                    final_subject_list.append(i[0]+"::"+j)
        
        for i in range(len(dropdowns_list)):
            for j in range(len(dropdowns_list[i])):
                dropdowns_list[i][j].config(value=final_subject_list)
                dropdowns_list[i][j].current(final_subject_list.index(class_timetable[i][j]))
    
    def slot_selected(self, i, j):
        class_name = class_dropdown.get()

        file = open('./Academic_years/'+academic_year+".json", 'r')
        json_object = json.load(file)
        file.close()

        class_details = json_object[class_name]
        subject_details = class_details["subject_teacher_list"]
        class_timetable = class_details["timetable"]

        subject_chosen = dropdowns_list[i][j].get()
        old_subject_chosen = class_timetable[i][j]

        if old_subject_chosen:
            teacher_selected = ''
            if '::' in old_subject_chosen: 
                teacher_selected = old_subject_chosen.split('::')[1]
            
            old_subject = old_subject_chosen.split('::')[0]
            subject_chosen_details = subject_details[old_subject]

            for classes in subject_chosen_details[4]:
                json_object[classes]["subject_teacher_list"][old_subject][-1] -= subject_chosen_details[-3]

            for k in range(subject_chosen_details[-3]):
                if teacher_selected == '':
                    for teacher in subject_chosen_details[2]:
                        json_object[teacher]["timetable"][i][j+k] = ''
                else:
                    json_object[teacher_selected]["timetable"][i][j+k] = ''

                dropdowns_list[i][j+k].current(0)
                for classes in subject_chosen_details[4]:
                    json_object[classes]["timetable"][i][j+k] = ''

                for lab in subject_chosen_details[3]:
                    json_object[lab]["timetable"][i][j+k] = ''

        condition = True
        
        if subject_chosen:
            subject = subject_chosen.split('::')[0]
            teacher_selected = ""
            if '::' in subject_chosen:
                teacher_selected = subject_chosen.split('::')[1]

            subject_chosen_details = subject_details[subject]
            
            for k in range(subject_chosen_details[-3]):
                if teacher_selected == '':
                    for teacher in subject_chosen_details[2]:
                        if json_object[teacher]["timetable"][i][j+k]:
                            messagebox.showwarning("WARNING", teacher+" has "+str(json_object[teacher]["timetable"][i][j])+" during the selected slot")
                            condition = False
                else:
                    if json_object[teacher_selected]["timetable"][i][j+k]:
                        messagebox.showwarning("WARNING", teacher_selected+" has "+str(json_object[teacher_selected]["timetable"][i][j])+" during the selected slot")
                        condition = False

                for classes in subject_chosen_details[4]:
                    if json_object[classes]["timetable"][i][j+k]:
                        messagebox.showwarning("WARNING", classes+" has "+json_object[classes]["timetable"][i][j]+" during the selected slot")
                        condition = False

                for lab in subject_chosen_details[3]:
                    if json_object[lab]["timetable"][i][j+k]:
                        messagebox.showwarning("WARNING", lab+" has "+json_object[lab]["timetable"][i][j]+" during the selected slot")
                        condition = False
            
            if int(subject_chosen_details[-3])+int(subject_chosen_details[-1]) > int(subject_chosen_details[1]):
                messagebox.showwarning("WARNING", "The number of classes per week has exceeded the limit")
                condition = False
            
            if j<2 and int(subject_chosen_details[-2])+j > 2 or 5>j>=2 and int(subject_chosen_details[-2])+j > 5 or j>=5 and int(subject_chosen_details[-2])+j > 8:
                messagebox.showwarning("WARNING", "Consecutive periods cannot have break in between")
                condition = False
            
            if condition:
                pass
            elif old_subject_chosen:
                subject_chosen = old_subject_chosen
                subject = old_subject_chosen.split("::")[0]
                subject_chosen_details = json_object[class_name]["subject_teacher_list"][subject]
                teacher_selected = ''
                if '::' in subject_chosen:
                    teacher_selected = old_subject_chosen.split("::")[1]
            else:
                dropdowns_list[i][j].current(0)
                return

            for classes in subject_chosen_details[4]:
                json_object[classes]["subject_teacher_list"][subject][-1] += int(subject_chosen_details[-3])
            
            for k in range(subject_chosen_details[-3]):
                if teacher_selected == '':
                    for teacher in subject_chosen_details[2]:
                        json_object[teacher]["timetable"][i][j+k] = subject_chosen_details[4]
                else:
                    json_object[teacher_selected]["timetable"][i][j+k] = subject_chosen_details[4]
                
                dropdowns_list[i][j+k].current(dropdowns_list[i][j+k]['values'].index(subject_chosen))
                for classes in subject_chosen_details[4]:
                    dropdowns_list[i][j+k].current(dropdowns_list[i][j+k]['values'].index(subject_chosen))
                    json_object[classes]["timetable"][i][j+k] = subject_chosen

                for lab in subject_chosen_details[3]:
                    json_object[lab]["timetable"][i][j+k] = subject_chosen_details[4]
        
        with open("./Academic_years/"+academic_year+".json", 'w') as file:
            file.write(json.dumps(json_object, indent=4))

        for children in subject_registered.get_children():
            subject_registered.delete(children)
        
        for i in json_object[class_name]["subject_teacher_list"].values():
            subject_registered.insert(parent='', text='', index=END, iid=i[0], value=[i[0], str(i[-1])+'/'+str(i[1])])
                
    
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
    div_dropdown.grid(row=0, column=0, columnspan=9, sticky=W+E)
    div_dropdown.bind("<<ComboboxSelected>>", div_selected)

    class_dropdown = ttk.Combobox(root, value=[])
    class_dropdown.grid(row=1, column=0, columnspan=9, sticky=W+E)
    class_dropdown.bind("<<ComboboxSelected>>", class_selected)

    dropdowns_list = [
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", ""]
    ]

    for i in range(5):
        for j in range(8):
            dropdowns_list[i][j] = ttk.Combobox(root, value=["Hello", "End"])
            dropdowns_list[i][j].grid(row=i+2, column=j)
            dropdowns_list[i][j].bind("<<ComboboxSelected>>", lambda event, i=i, j=j: slot_selected(event, i, j))
    
    for j in range(7):
        dropdowns_list[5][j] = ttk.Combobox(root)
        dropdowns_list[5][j].grid(row=7, column=j)
        dropdowns_list[5][j].bind("<<ComboboxSelected>>", lambda event, i=5, j=j: slot_selected(event, i, j))

    subject_frame = Frame(root)
    subject_frame.grid(row=2, column=8, rowspan=6)

    scroll = Scrollbar(subject_frame, orient=VERTICAL)
    scroll.pack(side=RIGHT, fill='y')

    subject_registered = ttk.Treeview(subject_frame, height=6, yscrollcommand=scroll.set)
    subject_registered.pack()

    scroll.config(command=subject_registered.yview)

    subject_registered["columns"] = ("SUBJECT", "COUNT")

    subject_registered.column("#0", width=0, stretch=NO)

    subject_registered.column("SUBJECT", anchor=CENTER)
    subject_registered.heading("SUBJECT", text="SUBJECT", anchor=CENTER)

    subject_registered.column("COUNT", width=80, anchor=CENTER)
    subject_registered.heading("COUNT", text="COUNT", anchor=CENTER)
    
    back_button = Button(root, text="BACK", command=back)
    back_button.grid(row=8, column=0, columnspan=8)
