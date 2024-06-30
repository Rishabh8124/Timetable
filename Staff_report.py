import csv
import json
from tkinter import *
from tkinter import messagebox

def print_staff_report():
    with open("temp.json") as file:
        json_object = json.load(file)
        academic_year = json_object["academic_year"]
    
    with open("./Academic_years/"+academic_year+".json") as file:
        json_object = json.load(file)
        teacher_list = json_object["teacher_list"]
    
    final_list = [["Teacher ID", "Teacher Name", "Subject Handling", "Classes Handling"]]
    for teacher in teacher_list:
        teacher_details = json_object[teacher[0]+'-'+teacher[1]]["class_list"]
        for i in teacher_details:
            class_list = set()
            for j in teacher_details[i]:
                for k in j:
                    class_list.add(k)
            teacher_details[i] = class_list
            final_list.append(teacher+ [i] + [", ".join(sorted(list(class_list)))])
    
    with open("Print.csv", "w", newline='') as file:
        csvwriter = csv.writer(file)
        csvwriter.writerows(final_list)
    
    messagebox.showinfo("INFO", "Saved in print.csv")
