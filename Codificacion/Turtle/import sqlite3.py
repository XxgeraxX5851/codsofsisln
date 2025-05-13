import sqlite3
from DataBaseManager import DataBaseManager

dataBaseManager = DataBaseManager()


con = sqlite3.connect(dataBaseManager.database)
cur =con.cursor()
cur.execute("select * from Materias;")
table_list = cur.fetchall()
for row in table_list:
    print(row[0])
con.close() 

