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
    }
}

json_object = json.dumps(defaults, indent=4)

file = open("defaults.json", 'w')
file.write(json_object)
file.close()