import os
from tkinter import *
from Academic_Year import *

l = os.listdir()
if "Academic_years" not in l:
    os.mkdir("Academic_years")
    
defaults = {
    "class_list": {
        "1": [
            "A",
            "B",
            "C",
            "D"
        ],
        "2": [
            "A",
            "B",
            "C",
            "D"
        ],
        "3": [
            "A",
            "B",
            "C",
            "D"
        ],
        "4": [
            "A",
            "B",
            "C",
            "D"
        ],
        "5": [
            "A",
            "B",
            "C",
            "D"
        ],
        "6": [
            "A",
            "B",
            "C",
            "D"
        ],
        "7": [
            "A",
            "B",
            "C",
            "D"
        ],
        "8": [
            "A",
            "B",
            "C",
            "D"
        ],
        "9": [
            "A",
            "B",
            "C",
            "D"
        ],
        "10": [
            "A",
            "B",
            "C",
            "D"
        ],
        "11": [
            "A",
            "B",
            "C"
        ],
        "12": [
            "A",
            "B",
            "C"
        ]
    },
    "timetable": [
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", ""]
    ]
}

if 'defaults.json' not in l:
    with open('defaults.json', 'w') as file:
        json_object = json.dumps(defaults, indent=4)
        file.write(json_object)

root = Tk()

Academic_year_window(root)

root.mainloop()
