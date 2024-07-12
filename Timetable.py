import json
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def timetable(root, button1, button2, button3, button4, button5, button6, button7, button8, button9):
    
    root.title("Timetable")

    def back():
        for widget in root.winfo_children():
            if widget not in [button1, button2, button3, button4, button5, button6, button7, button8, button9]:
                widget.destroy()

        button1.grid(row=0, column=0, padx=20, pady=12)
        button2.grid(row=0, column=1, padx=20, pady=12)
        button3.grid(row=1, column=0, columnspan=2, padx=20)
        button4.grid(row=2, column=0, padx=20, pady=12)
        button5.grid(row=2, column=1, padx=20, pady=12)
        button6.grid(row=3, column=0, padx=20)
        button7.grid(row=3, column=1, padx=20)
        button8.grid(row=4, column=0, padx=20, pady=12)
        button9.grid(row=4, column=1, padx=20, pady=12)
        
        root.title("TIMETABLE")
        root.eval('tk::PlaceWindow . center')

    def div_selected(self):
        div_select = div_dropdown.get()
        class_dropdown.config(values=class_list[class_division[div_select]])

    def class_selected(self):
        div_select = div_dropdown.get()
        
        if div_select == "Primary": 
            for i in dropdowns_list[-1][1:]:
                i.set("")
                i.config(state=DISABLED)
        else: 
            for i in dropdowns_list[-1][1:]:
                i.set("")
                i.config(state=NORMAL)
        
        class_name = class_dropdown.get()

        file = open('./Academic_years/'+academic_year+".json", 'r')
        json_object = json.load(file)
        file.close()

        class_details = json_object[class_name]
        subject_details = class_details["subject_teacher_list"]
        class_timetable = class_details["timetable"]
        
        registered = 0
        assigned = 0
        
        for i in subject_details:
            registered += int(subject_details[i][1])
            
        teacher_label.config(text=("Class teacher: "+class_details["teacher"]).upper()+"\n\nNO OF PERIODS REGISTERED: "+str(registered))

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
                if (i and j):
                    dropdowns_list[i][j].config(value=final_subject_list)
                    dropdowns_list[i][j].current(final_subject_list.index(class_timetable[i-1][j-1]))
    
    def slot_selected(self, i, j):
        
        def check(subject_details, subject_chosen, json_object, t):                
            condition = True
            
            subject = subject_chosen.split('::')[0]
            teacher_selected = ""
            if '::' in subject_chosen:
                teacher_selected = subject_chosen.split('::')[1]

            subject_chosen_details = subject_details[subject]
            
            if subject_chosen_details[6][i] == 0:
                if t: messagebox.showwarning("WARNING", "Selected subject cannot be handled on the specified day")
                condition = False
            
            if subject_chosen_details[5] == 1:
                c = 0
                for y in json_object[subject_chosen_details[4][0]]["timetable"][i]:
                    if y and y.split("::")[0] == subject: c += 1
                if c:
                    if t: messagebox.showwarning("WARNING", "Selected subject cannot have 2 classes on the same day")
                    condition = False
            
            if int(subject_chosen_details[-3])+j > len(json_object[subject_chosen_details[4][0]]["timetable"][i]):
                if t: messagebox.showwarning("WARNING", "Number of periods available is less than alloted count")
                condition = False
                
            for k in range(int(subject_chosen_details[-3])):
                if condition == False: break
                
                if teacher_selected == '':
                    for teacher in subject_chosen_details[2]:
                        if not json_object[teacher]["timetable"][i][j+k] == "":
                            if t: messagebox.showwarning("WARNING", teacher+" has "+str(json_object[teacher]["timetable"][i][j])+" during the selected slot")
                            condition = False
                            break
                    if condition == False: break
                else:
                    if not json_object[teacher_selected]["timetable"][i][j+k] == "":
                        if t: messagebox.showwarning("WARNING", teacher_selected+" has "+str(json_object[teacher_selected]["timetable"][i][j])+" during the selected slot")
                        condition = False
                        break

                for classes in subject_chosen_details[4]:
                    if json_object[classes]["timetable"][i][j+k]:
                        if t: messagebox.showwarning("WARNING", classes+" has "+json_object[classes]["timetable"][i][j]+" during the selected slot")
                        condition = False
                        break
                if condition == False: break

                for lab in subject_chosen_details[3]:
                    if json_object[lab]["timetable"][i][j+k]:
                        if t: messagebox.showwarning("WARNING", lab+" has "+str(json_object[lab]["timetable"][i][j])+" during the selected slot")
                        condition = False
                        break
                if condition == False: break
            
            if condition and int(subject_chosen_details[-3])+int(subject_chosen_details[-1]) > int(subject_chosen_details[1]):
                if t: messagebox.showwarning("WARNING", "The number of classes per week has exceeded the limit")
                condition = False
            
            if condition and t:
                for teacher in subject_chosen_details[2]:
                    j2 = j-1
                    count = int(subject_chosen_details[-3])
                    while(j2>=0 and json_object[teacher]["timetable"][i][j2]):
                        j2 -= 1
                        count += 1
                    j2 = j+k
                    while(j2 < len(json_object[teacher]["timetable"][i]) and json_object[teacher]["timetable"][i][j2]):
                        j2 += 1
                        count += 1
                    
                    if count > 4:
                        condition = messagebox.askyesno("LIMIT", "Assigning this subject makes "+str(count)+" periods consecutively for "+teacher+"\nDo you want to assign?")
                        if not condition: break
            
            return condition
        
        class_name = class_dropdown.get()

        file = open('./Academic_years/'+academic_year+".json", 'r')
        json_object = json.load(file)
        file.close()

        class_details = json_object[class_name]
        subject_details = class_details["subject_teacher_list"]
        class_timetable = class_details["timetable"]

        subject_chosen = dropdowns_list[i+1][j+1].get()
        old_subject_chosen = class_timetable[i][j]
        
        j1 = j

        if old_subject_chosen:
            teacher_selected = ''
            if '::' in old_subject_chosen: 
                teacher_selected = old_subject_chosen.split('::')[1]
            
            old_subject = old_subject_chosen.split('::')[0]
            subject_chosen_details = subject_details[old_subject]

            for classes in subject_chosen_details[4]:
                json_object[classes]["subject_teacher_list"][old_subject][-1] -= subject_chosen_details[-3]
                
            old_c = int(subject_chosen_details[-3])
            
            if old_c > 1:
                while (j1>=0 and json_object[class_name]["timetable"][i][j1] and json_object[class_name]["timetable"][i][j1].split('::')[0] == old_subject): j1 -= 1
                j1+=1
                while (j1+old_c <= j): j1 += old_c
                
            for k in range(old_c):
                if teacher_selected == '':
                    for teacher in subject_chosen_details[2]:
                        json_object[teacher]["timetable"][i][j1+k] = ''
                else:
                    json_object[teacher_selected]["timetable"][i][j1+k] = ''

                dropdowns_list[i+1][j1+k+1].current(0)
                for classes in subject_chosen_details[4]:
                    json_object[classes]["timetable"][i][j1+k] = ''

                for lab in subject_chosen_details[3]:
                    json_object[lab]["timetable"][i][j1+k] = ''

        condition = True
        
        if subject_chosen:
            subject = subject_chosen.split('::')[0]
            teacher_selected = ""
            if '::' in subject_chosen:
                teacher_selected = subject_chosen.split('::')[1]

            subject_chosen_details = subject_details[subject]
            
            condition = check(subject_details, subject_chosen, json_object, True)
            
            if condition:
                pass
            elif old_subject_chosen:
                subject_chosen = old_subject_chosen
                subject = old_subject_chosen.split("::")[0]
                subject_chosen_details = json_object[class_name]["subject_teacher_list"][subject]
                teacher_selected = ''
                if '::' in subject_chosen:
                    teacher_selected = old_subject_chosen.split("::")[1]
                j = j1
            else:
                dropdowns_list[i+1][j+1].current(0)
                
                # Possible options
                possible_list = []
                teachers_list = dropdowns_list[i+1][j+1].cget("values")[1:]
                for subject_option in teachers_list:
                    c1 = check(subject_details, subject_option, json_object, False)
                    if c1:
                        possible_list.append(subject_option)
                
                if possible_list:
                    messagebox.showinfo("POSSIBLE OPTIONS", "Possible Options:\n".upper()+"\n".join(possible_list))
                return

            for classes in subject_chosen_details[4]:
                json_object[classes]["subject_teacher_list"][subject][-1] += int(subject_chosen_details[-3])
            
            for k in range(int(subject_chosen_details[-3])):
                if teacher_selected == '':
                    for teacher in subject_chosen_details[2]:
                        json_object[teacher]["timetable"][i][j+k] = subject_chosen_details[4]
                else:
                    json_object[teacher_selected]["timetable"][i][j+k] = subject_chosen_details[4]
                
                dropdowns_list[i+1][j+1+k].current(dropdowns_list[i+1][j+1+k]['values'].index(subject_chosen))
                for classes in subject_chosen_details[4]:
                    dropdowns_list[i+1][j+k+1].current(dropdowns_list[i+1][j+1+k]['values'].index(subject_chosen))
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
    
    style = ttk.Style(root)
    style.configure('Treeview', font=("Arial", 10))
    style.configure('Treeview.Heading', font=("Arial", 11))
    
    class_division = {"Primary": 0, "Secondary": 1, "Higher Secondary": 2}

    div_label = Label(root, text="DIVISION", font=("Arial", 10))
    div_label.grid(row=0, column=2, pady=7)

    div_dropdown = ttk.Combobox(root, value=list(class_division.keys()), font=("Arial", 10))
    div_dropdown.grid(row=0, column=3, columnspan=4, sticky=W+E)
    div_dropdown.bind("<<ComboboxSelected>>", div_selected)

    class_label = Label(root, text="CLASS", font=("Arial", 10))
    class_label.grid(row=1, column=2)
    
    class_dropdown = ttk.Combobox(root, value=[], font=("Arial", 10))
    class_dropdown.grid(row=1, column=3, columnspan=4, sticky=W+E)
    class_dropdown.bind("<<ComboboxSelected>>", class_selected)
    
    teacher_label = Label(root, text="Class teacher: ".upper(), font=("Arial", 11), pady=10)
    teacher_label.grid(row=2, column=0, columnspan=9)

    dropdowns_list = [
        ["", "1", "2", "3", "4", "5", "6", "7", "8"],
        ["Monday", "", "", "", "", "", "", "", ""],
        ["Tuesday", "", "", "", "", "", "", "", ""],
        ["Wednesday", "", "", "", "", "", "", "", ""],
        ["Thursday", "", "", "", "", "", "", "", ""],
        ["Friday", "", "", "", "", "", "", "", ""],
        ["Saturday", "", "", "", "", "", "", ""]
    ]

    for i in range(len(dropdowns_list)):
        for j in range(len(dropdowns_list[i])):
            if i and j:
                dropdowns_list[i][j] = ttk.Combobox(root, value=[], font=("Arial", 10))
                dropdowns_list[i][j].grid(row=i+3, column=j, padx=1, pady=1)
                dropdowns_list[i][j].bind("<<ComboboxSelected>>", lambda event, i=i-1, j=j-1: slot_selected(event, i, j))
            
            else:
                dropdowns_list[i][j] = Label(root, text=dropdowns_list[i][j].upper(), font=("Arial", 10))
                dropdowns_list[i][j].grid(row=i+3, column=j, padx=20, pady=1)

    subject_frame = Frame(root)
    subject_frame.grid(row=10, column=0, columnspan=8, pady=20)

    scroll = Scrollbar(subject_frame, orient=VERTICAL)
    scroll.pack(side=RIGHT, fill='y')

    subject_registered = ttk.Treeview(subject_frame, height=6, yscrollcommand=scroll.set)
    subject_registered.pack()

    scroll.config(command=subject_registered.yview)

    subject_registered["columns"] = ("SUBJECT", "COUNT")

    subject_registered.column("#0", width=0, stretch=NO)

    subject_registered.column("SUBJECT", anchor=CENTER)
    subject_registered.heading("SUBJECT", text="SUBJECT", anchor=CENTER)

    subject_registered.column("COUNT", anchor=CENTER)
    subject_registered.heading("COUNT", text="COUNT", anchor=CENTER)
    
    back_button = Button(root, text="BACK", command=back, pady=5, font=("Arial", 10))
    back_button.grid(row=10, column=8, sticky=W+E)
    
    temp = Label(root, text="")
    temp.grid(row=10, column=9, padx=3)

    root.eval('tk::PlaceWindow . center')

# root = Tk()
# timetable(root, 1, 2, 3,4, 5, 6, 7, 8, 9)
# root.mainloop()