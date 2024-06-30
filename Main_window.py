from tkinter import *
from Timetable import timetable
from View_timetable import view_timetable
from Teacher_List_Confirmation import Teacher_Confirmation
from Subject_teacher_assignment import subject_teacher_assignment
from Class_teachers import class_teacher
from Staff_report import print_staff_report
from free_teachers import get_free_teachers
from find_teacher import find_teacher

def main_window(root):
    root.title("TIMETABLE")
    
    for widget in root.winfo_children():
        widget.destory()

    def add_teacher():
        add_teacher_button.grid_forget()
        assign_class_teacher_button.grid_forget()
        subject_registration_button.grid_forget()
        timetable_button.grid_forget()
        view_timetable_button.grid_forget()
        free_teacher_button.grid_forget()
        find_teacher_button.grid_forget()
        class_report_button.grid_forget()
        staff_report_button.grid_forget()

        Teacher_Confirmation(root, add_teacher_button, assign_class_teacher_button, subject_registration_button, timetable_button, view_timetable_button, free_teacher_button, find_teacher_button, class_report_button, staff_report_button)

    def assign_teacher():
        add_teacher_button.grid_forget()
        assign_class_teacher_button.grid_forget()
        subject_registration_button.grid_forget()
        timetable_button.grid_forget()
        view_timetable_button.grid_forget()
        free_teacher_button.grid_forget()
        find_teacher_button.grid_forget()
        class_report_button.grid_forget()
        staff_report_button.grid_forget()
        
        class_teacher(root, add_teacher_button, assign_class_teacher_button, subject_registration_button, timetable_button, view_timetable_button, free_teacher_button, find_teacher_button, class_report_button, staff_report_button)
    
    def subject_registration():
        add_teacher_button.grid_forget()
        assign_class_teacher_button.grid_forget()
        subject_registration_button.grid_forget()
        timetable_button.grid_forget()
        view_timetable_button.grid_forget()
        free_teacher_button.grid_forget()
        find_teacher_button.grid_forget()
        class_report_button.grid_forget()
        staff_report_button.grid_forget()

        subject_teacher_assignment(root, add_teacher_button, assign_class_teacher_button, subject_registration_button, timetable_button, view_timetable_button, free_teacher_button, find_teacher_button, class_report_button, staff_report_button)

    def timetable_button_function():
        add_teacher_button.grid_forget()
        assign_class_teacher_button.grid_forget()
        subject_registration_button.grid_forget()
        timetable_button.grid_forget()
        view_timetable_button.grid_forget()
        free_teacher_button.grid_forget()
        find_teacher_button.grid_forget()
        class_report_button.grid_forget()
        staff_report_button.grid_forget()

        timetable(root, add_teacher_button, assign_class_teacher_button, subject_registration_button, timetable_button, view_timetable_button, free_teacher_button, find_teacher_button, class_report_button, staff_report_button)

    def view_timetable_function():
        add_teacher_button.grid_forget()
        assign_class_teacher_button.grid_forget()
        subject_registration_button.grid_forget()
        timetable_button.grid_forget()
        view_timetable_button.grid_forget()
        free_teacher_button.grid_forget()
        find_teacher_button.grid_forget()
        class_report_button.grid_forget()
        staff_report_button.grid_forget()

        view_timetable(root, add_teacher_button, assign_class_teacher_button, subject_registration_button, timetable_button, view_timetable_button, free_teacher_button, find_teacher_button, class_report_button, staff_report_button)

    def free_teacher_list():
        add_teacher_button.grid_forget()
        assign_class_teacher_button.grid_forget()
        subject_registration_button.grid_forget()
        timetable_button.grid_forget()
        view_timetable_button.grid_forget()
        free_teacher_button.grid_forget()
        find_teacher_button.grid_forget()
        class_report_button.grid_forget()
        staff_report_button.grid_forget()

        get_free_teachers(root, add_teacher_button, assign_class_teacher_button, subject_registration_button, timetable_button, view_timetable_button, free_teacher_button, find_teacher_button, class_report_button, staff_report_button)
    
    def find_teacher_function():
        add_teacher_button.grid_forget()
        assign_class_teacher_button.grid_forget()
        subject_registration_button.grid_forget()
        timetable_button.grid_forget()
        view_timetable_button.grid_forget()
        free_teacher_button.grid_forget()
        find_teacher_button.grid_forget()
        class_report_button.grid_forget()
        staff_report_button.grid_forget()

        find_teacher(root, add_teacher_button, assign_class_teacher_button, subject_registration_button, timetable_button, view_timetable_button, free_teacher_button, find_teacher_button, class_report_button, staff_report_button)        
    
    add_teacher_button = Button(root, text="ADD TEACHER", command=add_teacher, font=("Arial", 13))
    add_teacher_button.grid(row=0, column=0, padx=20, pady=12)
    
    assign_class_teacher_button = Button(root, text="ASSIGN CLASS TEACHER", command=assign_teacher, font=("Arial", 13))
    assign_class_teacher_button.grid(row=0, column=1, padx=20)

    subject_registration_button = Button(root, text="SUBJECT REGISTRATION", command=subject_registration, font=("Arial", 13))
    subject_registration_button.grid(row=1, column=0, columnspan=2, padx=20)

    timetable_button = Button(root, text="ASSIGN TIMETABLE", command=timetable_button_function, font=("Arial", 13))
    timetable_button.grid(row=2, column=0, padx=20, pady=12)

    view_timetable_button = Button(root, text="VIEW TIMETABLE", command=view_timetable_function, font=("Arial", 13))
    view_timetable_button.grid(row=2, column=1, padx=20)
    
    free_teacher_button = Button(root, text="FREE TEACHER LIST", command=free_teacher_list, font=("Arial", 13))
    free_teacher_button.grid(row=3, column=0, padx=20)
    
    find_teacher_button = Button(root, text="FIND TEACHER", command=find_teacher_function, font=("Arial", 13))
    find_teacher_button.grid(row=3, column=1, padx=20)
    
    class_report_button = Button(root, text="PRINT CLASS REPORT", font=("Arial", 13))
    class_report_button.grid(row=4, column=0, padx=20, pady=12)
    
    staff_report_button = Button(root, text="PRINT STAFF REPORT", command=print_staff_report, font=("Arial", 13))
    staff_report_button.grid(row=4, column=1, padx=20)
    
    root.eval('tk::PlaceWindow . center')

root = Tk()
main_window(root)
root.mainloop()