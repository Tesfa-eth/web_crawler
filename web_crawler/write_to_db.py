"""
write_to_db.py
It writes the data stored in scrapped_data folder directly into sqlite database.

Tesfatsion Shiferaw
2022 G.C
"""
from turtle import position
from utility import read_json_file
import sqlite3

# read in the scrapped data
# make sure to enter the path with r in front. For ex: r'web_crawler\scrapped_data\technology.json'
scrapped_data = read_json_file(r'web_crawler\scrapped_data\all_scraped_data.json')
# Add bennington data to SQLite database

# define a connection
conn = sqlite3.connect('bennington_store.db')
cursor = conn.cursor()
# create a scrapped data table
# ?? make sure to drop all the pre-existing tables as needed
create_table1 = """CREATE TABLE IF NOT EXISTS
SCRAPPED_DATA(employee_id INTEGER PRIMARY KEY, name TEXT, img_src TEXT, office TEXT, position TEXT, location TEXT)"""
cursor.execute(create_table1)
# add data to the table

employee_id = 0 # should be self-incrementing
#cursor.execute("INSERT INTO SCRAPPED_DATA VALUES (0, 'Tester', 'img_src', 'test_office', 'position', 'location')")
#conn.commit()
#cursor.execute("SELECT * FROM SCRAPPED_DATA")
#result = cursor.fetchall()
#print(result)

for each_idx in range(len(scrapped_data)):
    name, img_src, office = scrapped_data[each_idx]['name'], scrapped_data[each_idx]['img_src'], scrapped_data[each_idx]['page']
    position = scrapped_data[each_idx]['position']
    try: # error managmemt for some missing values
        location = scrapped_data[each_idx]['location']
    except:
        location = 'N/A'
    cursor.execute(f"INSERT INTO SCRAPPED_DATA VALUES ('{employee_id}', '{name}', '{img_src}', '{office}', '{position}', '{location}')")
    conn.commit()
    employee_id+=1
# name, img_src, office (page), position, location

#print(name, img_src, office, position, location)
print('complete!')