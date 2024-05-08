import json
import os
from tkinter import *
from Academic_Year import *    

root = Tk()

Academic_year_window(root)

root.mainloop()

os.popen('rm -f temp.json')
