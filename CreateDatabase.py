

import sqlite3

connection = sqlite3.connect("Packet.db")   #sqlite3.cnnect() function returns objects that will be used to interact with database 
cursor = connection.cursor()   #creates cursor object used to SQL statements to a SQLite database using cursor.execute()



cursor.execute("CREATE TABLE IF NOT EXISTS New_Packet (local_time TEXT , IP_Protocol TEXT, src_address TEXT, dest_address TEXT,  transport_protocol TEXT, packet_count INTEGER, Node TEXT, Interface TEXT)")
connection.commit()

print("The packets table has been created.") #Confirmation that the database has been created

connection.commit()
connection.close()

