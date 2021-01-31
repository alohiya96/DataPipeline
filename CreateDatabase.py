

import sqlite3   #used to connect to a SQLite database 

connection = sqlite3.connect("Packet.db")  #open connection with database 
cursor = connection.cursor()   #creates cursor object used to SQL statements to a SQLite database using cursor.execute()
`

#Create Table in the database using the cursor
cursor.execute("CREATE TABLE IF NOT EXISTS New_Packet (local_time TEXT , IP_Protocol TEXT, src_address TEXT, dest_address TEXT,  transport_protocol TEXT, packet_count INTEGER, Node TEXT, Interface TEXT)")
connection.commit()

print("The packets table has been created.") #Confirmation that the database has been created

connection.commit()
connection.close()

