"""
write_to_db.py
It writes the data stored in scrapped_data folder directly into sqlite database.

Tesfatsion Shiferaw
2022 G.C
"""
from turtle import position
from utility import read_json_file, clean_name
import sqlite3

def add_to_db(file_path=r'web_crawler\scrapped_data\all_scraped_data.json', drop_existing=True):
    """ read in the scrapped data from
    Args:
    file_path: raw string, relative path of the json file to read and write into the database. Make 
    sure to enter the path with r in front. For ex: r'web_crawler\scrapped_data\technology.json'
    drop_existing: bool, drop existing table
    Returns:
    writes the data into SCRAPPED_DATA table of bennington_store.db
    """
    scrapped_data = read_json_file(file_path)
    # Add bennington data to SQLite database
    # define a connection
    conn = sqlite3.connect('bennington_store.db')
    cursor = conn.cursor()
    # make sure to drop all the pre-existing tables as needed
    drop_table = """DROP TABLE IF EXISTS SCRAPPED_DATA"""
    cursor.execute(drop_table)
    # create a scrapped data table
    create_table1 = """CREATE TABLE IF NOT EXISTS
    SCRAPPED_DATA(employee_id INTEGER PRIMARY KEY, name TEXT, img_src TEXT, 
    office TEXT, position TEXT, location TEXT)"""
    cursor.execute(create_table1)
    # add data to the table
    employee_id = 0 # should be self-incrementing
    
    for each_idx in range(len(scrapped_data)):
        # AIs:Auto-increment
        name, img_src, office = clean_name(scrapped_data[each_idx]['name']), scrapped_data[each_idx]['img_src'], scrapped_data[each_idx]['page']
        position = scrapped_data[each_idx]['position']
        try: # error managmemt for some missing values
            location = scrapped_data[each_idx]['location']
        except:
            location = 'N/A'
        cursor.execute(f"INSERT INTO SCRAPPED_DATA VALUES ('{employee_id}', '{name}', '{img_src}', '{office}', '{position}', '{location}')")
        conn.commit()
        employee_id+=1
    # name, img_src, office (page), position, location
    conn.close()
#print(name, img_src, office, position, location)
if __name__ == '__main__':
    add_to_db()
    print('complete!')