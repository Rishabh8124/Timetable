import os
from tkinter import *
from Academic_Year import *

l = os.listdir()
if "Academic_years" not in l:
    os.mkdir("Academic_years")

root = Tk()

Academic_year_window(root)

root.mainloop()
