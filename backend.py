import json

defaults = {
    "class_list": [
        '1A', '1B', '1C', '1D',
        '2A', '2B', '2C', '2D',
        '3A', '3B', '3C', '3D',
        '4A', '4B', '4C', '4D',
        '5A', '5B', '5C', '5D',
        '6A', '6B', '6C', '6D',
        '7A', '7B', '7C', '7D',
        '8A', '8B', '8C', '8D',
        '9A', '9B', '9C', '9D',
        '10A', '10B', '10C', '10D',
        '11A', '11B', '11C',
        '12A', '12B', '12C'
    ]
}

json_object = json.dumps(defaults, indent=4)

file = open("defaults.json", 'w')
file.write(json_object);
file.close()