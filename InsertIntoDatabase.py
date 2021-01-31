

import sqlite3  #used to connect to a SQLite database 

def InsertData():
	connection = sqlite3.connect("Packet.db")   #sqlite3.cnnect() function returns objects that will be used to interact with database 
	cursor = connection.cursor()   #creates cursor object used to SQL statements to a SQLite database using cursor method


	file = open("Packet.csv","r") 

	while True:		    		#to enter while loop
		line = file.readline()   #read the file by line by line

		if not line:  			 #conditional added so program will break out of while loop after all the lines are read
			break
	
		cursor.execute("INSERT INTO New_Packet VALUES (?,?,?,?,?,?,?,?)", line.split(",")) #Insert values (each string withing a comma is a vlue)
		connection.commit()  

	connection.close()

def deleteData():
	connection = sqlite3.connect("Packet.db")
	cursor = connection.cursor()
	cursor.execute("DELETE FROM New_Packet")  #Delete all the contents of the table without deleting the contents
	connection.commit()
	#db.execSQL("delete from "+ New_Packet);

InsertData() #Calls insert data function 




	
