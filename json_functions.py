import json
from collections import ChainMap

def read_full(filename: str) -> json:
    with open(filename, 'r') as file:
        data = json.load(file)
    return data 


def write_to(filename: str, data: dict) -> bool:
    try:
        with open(filename, 'r+') as file:
            file_data = json.load(file)
            file_data['chats'].insert(0, data)            
            file.seek(0)
            json.dump(file_data, file, indent = 4)
        return True
    except:
        return False


def get_by_id(filename: str, id: str):
    try:
        return dict(ChainMap(*read_full(filename)['chats']))[id]
    except:
        return []

