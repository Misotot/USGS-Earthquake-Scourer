# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 10:27:34 2020
@author: Stephen Wren
"""
import sqlite3
import pymongo

uri = "mongodb+srv://dbUser:dbUser1@cluster0.1zhzd.mongodb.net/<dbname>?retryWrites=true&w=majority"
client = pymongo.MongoClient(uri)
db = client['earthquakedb']
collection_earthquakes = db['collection_earthquakes'] 

con = sqlite3.connect('index.sqlite')
cur = con.cursor()
cur.executescript('''DROP TABLE IF EXISTS quake;
CREATE TABLE quake (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    magnitude  INTEGER, 
    time    INTEGER,    
    depth INTEGER,
    place    TEXT,
    title    TEXT, 
    felt  INTEGER,
    region TEXT
    );
''')

cursor = collection_earthquakes.find()
for f in cursor:
   
    depth = f["geometry"]["coordinates"][2]
    magnitude = f["properties"]["mag"]
    time = f["properties"]["time"]
    felt = f["properties"]["felt"]
    title = f['properties']["title"]
    place = f["properties"]["place"]
    region = f["properties"]["place"]
    cur.execute('''INSERT OR REPLACE INTO quake
        (magnitude, time, depth, place, title, felt, region) 
        VALUES ( ?, ?, ?, ?, ?, ?, ?)''', 
        (magnitude, time, depth, place, title, felt, region)  )
    cur.execute('SELECT DISTINCT region from quake ORDER BY region')
    con.commit()
#print(cur.fetchall())
print("Done")
cur.close()
con.close()




    

