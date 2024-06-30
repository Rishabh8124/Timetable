import csv
import json
from tkinter import *
from tkinter import messagebox

def print_class_report():
    with open("temp.json") as file:
        json_object = json.load(file)
        academic_year = json_object["academic_year"]
    
    with open("./Academic_years/"+academic_year+".json") as file:
        json_object = json.load(file)
        class_l = json_object["class_list"]
        class_list = []
        for i in class_l:
            class_list.extend(i)
    
    final_list = []
    for class_name in class_list:
        final_list.append(["Class", class_name])
        final_list.append(["Subject name", "Teachers Handling", "Labs", "Total Count"])
        for subjects in json_object[class_name]["subject_teacher_list"]:
            details = json_object[class_name]["subject_teacher_list"][subjects]
            final_list.append([details[0], ", ".join(details[2]), ", ".join(details[3]), details[1]])
        final_list.extend([[], []])
    
    with open("Print.csv", "w", newline='') as file:
        csvwriter = csv.writer(file)
        csvwriter.writerows(final_list)
    
    messagebox.showinfo("INFO", "Saved in print.csv")
