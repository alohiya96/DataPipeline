
import sqlite3  #used to connect to a SQLite database 
import GenerateData as gen      #import GenerateData file to call its function
import InsertIntoDatabase as insert #import this file to acll its functions

def Output():

	count = 2

	while count < 4:
		connection = sqlite3.connect("Packet.db") #creating a connection to the db file
		connection.text_factory = str #Ensures the attributed in the output are prinited out as strings and not as unicode string
		cursor = connection.cursor()

		#.fetchall() will be used at the end of the following queries to fetch all the rows of a query result

		rows = cursor.execute("SELECT* FROM New_Packet").fetchall()  #fetchall() retrieves all the results from the select statement
		connection.commit()

		for line in rows:  #printing out each row in the query line by line
			print(line)

		print(" " + "\n")
	



		new_rows = cursor.execute("SELECT* FROM New_Packet WHERE packet_count > 500000 ").fetchall() #query retrieves rows for which the packetflow count is > than 50000
		connection.commit()

		for data in new_rows:  #printing out each row in the query line by line
			print(data)

		print(" ")
		print(" ")


		cur = connection.cursor()  
		query = cur.execute("SELECT* FROM New_Packet WHERE transport_protocol = 'TCP' ").fetchall() #query retrieves rows for which the transport protocol is TCP
		connection.commit()

		for values in query:
   			print(values)

		print(" " + "\n")

		new_cur = connection.cursor()  #query retrieves rows where the src_address or the dest_address of the packet is 20.1.1.1
		new_query = new_cur.execute(" SELECT* FROM New_Packet WHERE (src_address = '10.1.1.1' OR dest_address = '20.1.1.1') ").fetchall()
		connection.commit()

		for info in new_query: #printing out each row in the query line by line
			print(info)

		print(" " + "\n")
		



		query_one = new_cur.execute("SELECT Node, Interface FROM New_Packet WHERE src_address = '10.1.1.1' OR dest_address = '20.1.1.1'  ").fetchmany(3)
		connection.commit()
		print("The pathway is: ")
		print(query_one)

		for information in query_one: #printing out each row in the query line by line
			print(information)

		print(" " + "\n")


		#Query for the top 5 largest packet flows for Node 3
		query_two= new_cur.execute("SELECT Node, packet_count FROM New_Packet WHERE Node = 'Node3' ORDER BY packet_count DESC LIMIT 5").fetchall()
		
		for i in query_two:
			print(i)
		print(" " + "\n")

		#Query for the top 5 largest packet flows for Node 4
		query_three= new_cur.execute("SELECT Node, packet_count FROM New_Packet WHERE Node = 'Node4' ORDER BY packet_count DESC LIMIT 5").fetchall()
		for x in query_three:
			print(x)
		print(" " + "\n")

		#Query for the top 5 largest packet flows for Node 5
		query_four = new_cur.execute("SELECT Node, packet_count FROM New_Packet WHERE Node = 'Node5' ORDER BY packet_count DESC LIMIT 5").fetchall()
		for j in query_four:
			print(j)
		print(" " + "\n")


		gen.delete_contents() #call delete_contents function in GenerateData file to delete the contents of the csv file
		gen.GenerateData()   #call delete_contents function in GenerateData file to generate new data which will be written in the csv 
		insert.deleteData()  #delete data in the table by calling deleteData function in InserIntoDatabase file
		insert.InsertData()   #call this function in InsertData file to insert new data from csv file in the table
		count += 1

		cur.close()
		new_cur.close()
		cursor.close()

Output()   #call Output function











