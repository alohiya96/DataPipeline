

import sqlite3, csv


def InsertData():
	connection = sqlite3.connect("Packet.db")   #sqlite3.cnnect() function returns objects that will be used to interact with database 
	cursor = connection.cursor()   #creates cursor object used to SQL statements to a SQLite database using cursor.execute()


	file = open("Packet.csv","r")

	while True:		
		line = file.readline()

		if not line:
			break
	
		cursor.execute("INSERT OR IGNORE INTO New_Packet VALUES (?,?,?,?,?,?,?,?)", line.split(","))
		connection.commit()

	connection.close()

def deleteData():
	connection = sqlite3.connect("Packet.db")
	cursor = connection.cursor()
	cursor.execute("DELETE FROM New_Packet")

InsertData()




	
