import csv
import json
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def view_timetable(root, button1, button2, button3, button4, button5):
    
    root.title("View Timetable")
    
    with open("temp.json") as file:
        json_object = json.load(file)
        academic_year = json_object["academic_year"]
    
    with open("./Academic_years/"+academic_year+".json") as file:
        json_object = json.load(file)
    
    timetable_structure = [
        ["", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""]
    ]
    
    copy_timetable = [
        ["", "1", "2", "3", "4", "5", "6", "7", "8"],
        ["Monday", "", "", "", "", "", "", "", ""],
        ["Tuesday", "", "", "", "", "", "", "", ""],
        ["Wednesday", "", "", "", "", "", "", "", ""],
        ["Thursday", "", "", "", "", "", "", "", ""],
        ["Friday", "", "", "", "", "", "", "", ""],
        ["Saturday", "", "", "", "", "", "", ""]
    ]
    
    def back():
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

    def drop1_selected(self):
        select = dropdown1.get()
        if select in ["Class with Teacher name", "Class without Teacher name"]:
            final = []
            for i in json_object['class_list']:
                final.extend(i)
        
        elif select == "Teacher":
            final = []
            for i in json_object['teacher_list']:
                final.append(i[0]+'-'+i[1])
        
        elif select == "Lab":
            final = json_object['lab_list']
        
        dropdown2.config(values=final)

    def drop2_selected(self):
        select1 = dropdown1.get()
        select = dropdown2.get()
        timetable_details = json_object[select]['timetable']

        if select1 != "Class without Teacher name":
            for i in range(len(timetable_structure)):
                for j in range(len(timetable_structure[i])):
                    if (i and j): timetable_structure[i][j].config(text=str(timetable_details[i-1][j-1]))
        
        else:
            for i in range(len(timetable_structure)):
                for j in range(len(timetable_structure[i])):
                    if (i and j):
                        if '::' not in timetable_details[i-1][j-1]:
                            timetable_structure[i][j].config(text=timetable_details[i-1][j-1])
                        else:
                            timetable_structure[i][j].config(text=timetable_details[i-1][j-1].split('::')[0])
    
    def print_teachers():
        final_list = []
        count = 0
        for i in json_object["teacher_list"]:
            final_list.append(["Name:", i[0]+'-'+i[1]])
            final_list.append(copy_timetable[0].copy())
            
            current_timetable = json_object[i[0]+'-'+i[1]]["timetable"]
            for j in range(len(current_timetable)):
                final_list.append(copy_timetable[j+1].copy())
                for k in range(len(current_timetable[j])):
                    final_list[-1][k+1] = current_timetable[j][k]
            final_list.extend([[], [], []])
            count += 1
            if (count%4 == 0):
                final_list.extend([[], [], []])
        
        with open("Print.csv", "w", newline='') as file:
            csvwriter = csv.writer(file)
            csvwriter.writerows(final_list)
        
        messagebox.showinfo("INFO", "Saved in print.csv")
    
    def print_class():
        final_list = []
        count = 0
        for j in json_object["class_list"]:
            for i in j:
                final_list.append(["Class", i])
                final_list.append(["Class Teacher", json_object[i]["teacher"]])
                final_list.append(copy_timetable[0].copy())
                
                current_timetable = json_object[i]["timetable"]
                for x in range(len(current_timetable)):
                    final_list.append(copy_timetable[x+1].copy())
                    for k in range(len(current_timetable[x])):
                        if current_timetable[x][k]: final_list[-1][k+1] = current_timetable[x][k].split("::")[0]
                final_list.append([])
                final_list.append([])
                count += 1
                if (count%4 == 0):
                    final_list.extend([[], [], []])
        
        with open("Print.csv", "w", newline='') as file:
            csvwriter = csv.writer(file)
            csvwriter.writerows(final_list)
        
        messagebox.showinfo("INFO", "Saved in print.csv")
    
    def print_current():
        select1 = dropdown1.get()
        select = dropdown2.get()
        
        value = (dropdown2.cget("values"))
        if (select not in value):
            messagebox.showwarning("WARNING", "Select a valid option")
            return
        
        current_timetable = json_object[select]['timetable']
        final_list = []
        final_list.append(["Type", select1])
        final_list.append([select])
        for j in range(len(current_timetable)):
            final_list.append(copy_timetable[j+1].copy())
            for k in range(len(current_timetable[j])):
                final_list[-1][k+1] = timetable_structure[j+1][k+1].cget("text")
        
        with open("Print.csv", "w", newline='') as file:
            csvwriter = csv.writer(file)
            csvwriter.writerows(final_list)
        
        messagebox.showinfo("INFO", "Saved in print.csv")
    
    dropdown1 = ttk.Combobox(root, values=["Class with Teacher name", "Class without Teacher name", "Teacher", "Lab"], font=("Arial", 10))
    dropdown1.grid(row=0, column=2, columnspan=5, sticky=W+E, pady=5)
    dropdown1.bind("<<ComboboxSelected>>", drop1_selected)

    dropdown2 = ttk.Combobox(root, font=("Arial", 10))
    dropdown2.grid(row=1, column=2, columnspan=5, sticky=W+E)
    dropdown2.bind("<<ComboboxSelected>>", drop2_selected)

    day = {
        1: "MONDAY",
        2: "TUESDAY",
        3: "WEDNESDAY",
        4: "THURSDAY",
        5: "FRIDAY",
        6: "SATURDAY"
    }

    for i in range(len(timetable_structure)):
        for j in range(len(timetable_structure[i])):
            if (i and j): timetable_structure[i][j] = Label(root, text='', width=18, font=("Arial", 10), highlightthickness=1, highlightbackground = "black", highlightcolor= "black")
            elif (i): timetable_structure[i][j] = Label(root, text=day[i], width=18, padx=30, font=("Arial", 10))
            elif (j): timetable_structure[i][j] = Label(root, text=str(j), width=18, pady=10, font=("Arial", 10))
            
            if (i or j): timetable_structure[i][j].grid(row=i+2, column=j, sticky=W+E, padx=1, pady=1)

    print_button_1 = Button(root, text="Print Teacher timetables".upper(), command=print_teachers, font=("Arial", 11))
    print_button_1.grid(row=9, column=0, columnspan=2, pady=15, sticky=W+E, padx=5)
    
    print_button_2 = Button(root, text="Print Class Timeatables".upper(), command=print_class, font=("Arial", 11))
    print_button_2.grid(row=9, column=2, columnspan=2, sticky=W+E, padx=5)
    
    print_button_3 = Button(root, text="Print Timetable".upper(), command=print_current, font=("Arial", 11))
    print_button_3.grid(row=9, column=4, columnspan=2, sticky=W+E, padx=5)
    
    back_button = Button(root, text="BACK", command=back, font=("Arial", 11))
    back_button.grid(row=9, column=6, columnspan=3, sticky=W+E, padx=5)
    
    temp = Label(root, text=" ", padx=3)
    temp.grid(row=9, column=9)
    
    root.eval('tk::PlaceWindow . center')
