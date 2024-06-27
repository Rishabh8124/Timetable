from tkinter import *
from Timetable import timetable
from View_timetable import view_timetable
from Teacher_List_Confirmation import Teacher_Confirmation
from Subject_teacher_assignment import subject_teacher_assignment
from Class_teachers import class_teacher

def main_window(root):
    for widget in root.winfo_children():
        widget.destory()

    def add_teacher():
        add_teacher_button.grid_forget()
        subject_registration_button.grid_forget()
        timetable_button.grid_forget()
        view_timetable_button.grid_forget()
        assign_class_teacher_button.grid_forget()

        Teacher_Confirmation(root, add_teacher_button, subject_registration_button, timetable_button, view_timetable_button, assign_class_teacher_button)

    def assign_teacher():
        add_teacher_button.grid_forget()
        subject_registration_button.grid_forget()
        timetable_button.grid_forget()
        view_timetable_button.grid_forget()
        assign_class_teacher_button.grid_forget()
        
        class_teacher(root, add_teacher_button, subject_registration_button, timetable_button, view_timetable_button, assign_class_teacher_button)
    
    def subject_registration():
        add_teacher_button.grid_forget()
        subject_registration_button.grid_forget()
        timetable_button.grid_forget()
        view_timetable_button.grid_forget()
        assign_class_teacher_button.grid_forget()

        subject_teacher_assignment(root, add_teacher_button, subject_registration_button, timetable_button, view_timetable_button, assign_class_teacher_button)

    def timetable_button_function():
        add_teacher_button.grid_forget()
        subject_registration_button.grid_forget()
        timetable_button.grid_forget()
        view_timetable_button.grid_forget()
        assign_class_teacher_button.grid_forget()

        timetable(root, add_teacher_button, subject_registration_button, timetable_button, view_timetable_button, assign_class_teacher_button)

    def view_timetable_function():
        add_teacher_button.grid_forget()
        subject_registration_button.grid_forget()
        timetable_button.grid_forget()
        view_timetable_button.grid_forget()
        assign_class_teacher_button.grid_forget()

        view_timetable(root, add_teacher_button, subject_registration_button, timetable_button, view_timetable_button, assign_class_teacher_button)

    add_teacher_button = Button(root, text="ADD TEACHER", command=add_teacher)
    add_teacher_button.grid(row=0, column=0)
    
    assign_class_teacher_button = Button(root, text="ASSIGN CLASS TEACHER", command=assign_teacher)
    assign_class_teacher_button.grid(row=1, column=0)

    subject_registration_button = Button(root, text="SUBJECT REGISTRATION", command=subject_registration)
    subject_registration_button.grid(row=2, column=0)

    timetable_button = Button(root, text="ASSIGN TIMETABLE", command=timetable_button_function)
    timetable_button.grid(row=3, column=0)

    view_timetable_button = Button(root, text="VIEW TIMETABLE", command=view_timetable_function)
    view_timetable_button.grid(row=4, column=0)
