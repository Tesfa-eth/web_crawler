"""
utility.py

Tesfatsion Shiferaw
2022 G.C
"""
import json

def write_json(data, file_name, indent=4):
    """writes json to a file
    Args:
    data: the data to write
    file_name: name to save the file with
    """
    path = 'web_crawler/scrapped_data/' + file_name + '.json'
    print('writing to', path)
    with open(path, 'w') as outfile:
        json.dump(data, outfile, indent=indent)