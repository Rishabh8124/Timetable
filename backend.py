import json

defaults = {
    "class_list": {
        1:  ['A', 'B', 'C', 'D'],
        2:  ['A', 'B', 'C', 'D'],
        3:  ['A', 'B', 'C', 'D'],
        4:  ['A', 'B', 'C', 'D'],
        5:  ['A', 'B', 'C', 'D'],
        6:  ['A', 'B', 'C', 'D'],
        7:  ['A', 'B', 'C', 'D'],
        8:  ['A', 'B', 'C', 'D'],
        9:  ['A', 'B', 'C', 'D'],
        10: ['A', 'B', 'C', 'D'],
        11: ['A', 'B', 'C'],
        12: ['A', 'B', 'C'],
    }, "subject_list" : ['English', 'Chemistry', 'Chemistry Practicals', 'GS', 'Economics', 'History', 'BS',
     'Accounts', 'Maths', 'CS', 'IP', 'CS Practicals', 'IP Practicals', 'Biology', 'Biology Practicals', 'Science',
     'Work Experience', 'Science Practicals', 'Physics', 'Physics Practicals', 'Sociology', 'Political Science',
     'L2', 'PT', 'L3', 'Social Studies', 'CCA', 'Library',
     'Spoken Sanskrit', 'Value Education', 'Craft', 'EVS', 'Yoga',
     'BV', 'CCA', 'DDMM', 'DMM', 'Tamil', 'Hindi'] + [
        'English', 'Tamil', 'Hindi', 'Spoken Sanskrit', 'L2', 'L3'
        'Physics', 'Chemistry', 'Biology', 'Science',
        'Maths', 'CS', 'IP', 'Social Studies',
        'Physics Practicals', 'Chemistry Practicals', 'Maths Practicals', 'CS Practicals', 'IP Practicals',
        'PT', 'WE', 'CCA', 'DDMM', 'DMM', 'Value Education', 'Craft']
}

json_object = json.dumps(defaults, indent=4)

file = open("defaults.json", 'w')
file.write(json_object)
file.close()