import json

def read_from_json(filename:str):
    try:
        with open(filename, 'r') as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        return []

def write_in_json(filename: str, data: list):    
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)  # `indent` for pretty printing

