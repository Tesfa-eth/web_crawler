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

    issue:
    currently writing as a txt file rather than json
    """
    path = 'web_crawler/scrapped_data/' + file_name + '.json'
    #print('writing to', path)
    with open(path, 'w') as outfile:
        json.dump(data, outfile, indent=indent)

def read_json_file(path=r'web_crawler\scrapped_data\all_scraped_data.json'):
    """reads Json file
    Args:
    path: the path to the json file
    """
    with open(path, 'r') as data_file:  
        return json.load(data_file)



#print(read_json_file())