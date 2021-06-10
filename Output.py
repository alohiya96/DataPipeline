
import sqlite3, csv, GenerateData
import GenerateData as gen
import InsertIntoDatabase as insert

def Output():

	count = 2

	while count < 4:
		connection = sqlite3.connect("Packet.db")
		connection.text_factory = str
		cursor = connection.cursor()


		rows = cursor.execute("SELECT* FROM New_Packet").fetchall()  #fetchall() retrieves all the results from the select statement
		connection.commit()

		for line in rows:
			print(line)

		print("  ")
		print("  ")



		new_rows = cursor.execute("SELECT* FROM New_Packet WHERE packet_count > 500000 ").fetchall()
		#print(new_rows)
		connection.commit()

		for data in new_rows:
			print(data)

		print("  ")
		print("  ")


		cur = connection.cursor()
		query = cur.execute("SELECT* FROM New_Packet WHERE transport_protocol = 'TCP' ").fetchall()
		connection.commit()

		for values in query:
   			print(values)

		print(" ")
		print("  ")

		new_cur = connection.cursor()
		new_query = new_cur.execute(" SELECT* FROM New_Packet WHERE (src_address = '10.1.1.1' OR dest_address = '20.1.1.1') ").fetchall()
		connection.commit()

		for info in new_query:
			print(info)

		print(" ")
		print("  ")



		query_two = new_cur.execute("SELECT Node, Interface FROM New_Packet WHERE src_address = '10.1.1.1' OR dest_address = '20.1.1.1'  ").fetchmany(3)
		connection.commit()
		print("The pathway is: ")
		print(query_two)

		for information in query_two:
			print(information)

		print("query_three")





		query_three = new_cur.execute(" SELECT Node, MAX(packet_count) FROM New_Packet WHERE Node = 'Node3' ").fetchall()
		query_four = new_cur.execute(" SELECT Node, MAX(packet_count) FROM New_Packet WHERE Node = 'Node3' AND packet_count NOT IN (SELECT MAX(packet_count) FROM New_Packet WHERE Node = 'Node3') ").fetchall()
	#query_five = new_cur.execute("SELECT Node, MAX(packet_count) FROM ((SELECT* from Employee ORDER BY 'packet_count' DESC limit 5 ) AS T) ORDER BY T.`packet_count ASC limit 1;")
		query_five = new_cur.execute("SELECT Node, packet_count FROM New_Packet WHERE Node = 'Node3' ORDER BY packet_count DESC LIMIT 1 OFFSET 2").fetchall()
		query_six = new_cur.execute(" SELECT Node, packet_count FROM New_Packet WHERE Node = 'Node3' ORDER BY packet_count DESC LIMIT 1 OFFSET 3").fetchall()
		query_seven = new_cur.execute(" SELECT Node, packet_count FROM New_Packet WHERE Node = 'Node3' ORDER BY packet_count DESC LIMIT 1 OFFSET 4").fetchall()


#query_six= new_cur.execute(" SELECT Node, packet_count FROM New_Packet WHERE Node = 'Node3' ORDER BY packet_count DESC LIMIT 3,1 ").fetchall()

		query_one = new_cur.execute("SELECT Node, packet_count FROM New_Packet WHERE Node = 'Node3' ORDER BY packet_count DESC LIMIT 5").fetchall()
		print(query_one)
		#print(query_four)
		#print(query_five)
		#print(query_six)
		#print(query_seven)


#query_eight = new_cur.execute(" SELECT * FROM New_Packet WHERE Node = 'Node4' ").fetchall()
#print(query_eight)

		query_nine = new_cur.execute(" SELECT Node, MAX(packet_count) FROM New_Packet WHERE Node = 'Node4' ").fetchall()
		print(query_nine)

		query_ten = new_cur.execute(" SELECT Node, MAX(packet_count) FROM New_Packet WHERE Node = 'Node4' AND packet_count NOT IN (SELECT MAX(packet_count) FROM New_Packet WHERE Node = 'Node3') ").fetchall()
#query_five = new_cur.execute("SELECT Node, MAX(packet_count) FROM ((SELECT* from Employee ORDER BY 'packet_count' DESC limit 5 ) AS T) ORDER BY T.`packet_count ASC limit 1;")
		print(query_ten)

		query_eleven = new_cur.execute("SELECT Node, packet_count FROM New_Packet WHERE Node = 'Node4' ORDER BY packet_count DESC LIMIT 1 OFFSET 2").fetchall()
		print(query_eleven)

		query_twelve = new_cur.execute(" SELECT Node, packet_count FROM New_Packet WHERE Node = 'Node4' ORDER BY packet_count DESC LIMIT 1 OFFSET 3").fetchall()
		print(query_twelve)

		query_thirteen = new_cur.execute(" SELECT Node, packet_count FROM New_Packet WHERE Node = 'Node4' ORDER BY packet_count DESC LIMIT 1 OFFSET 4").fetchall()
		print(query_thirteen)


		query_two= new_cur.execute("SELECT Node, packet_count FROM New_Packet WHERE Node = 'Node4' ORDER BY packet_count DESC LIMIT 5").fetchall()
		print(query_two)


####

#query_fourteen = new_cur.execute(" SELECT * FROM New_Packet WHERE Node = 'Node5' ").fetchall()
#print(query_eight)

		query_nine = new_cur.execute("SELECT Node, MAX(packet_count) FROM New_Packet WHERE Node = 'Node5' ").fetchall()
		print(query_nine)

		query_ten = new_cur.execute(" SELECT Node, MAX(packet_count) FROM New_Packet WHERE Node = 'Node5' AND packet_count NOT IN (SELECT MAX(packet_count) FROM New_Packet WHERE Node = 'Node5') ").fetchall()
#query_five = new_cur.execute("SELECT Node, MAX(packet_count) FROM ((SELECT* from Employee ORDER BY 'packet_count' DESC limit 5 ) AS T) ORDER BY T.`packet_count ASC limit 1;")
		print(query_ten)

		query_eleven = new_cur.execute("SELECT Node, packet_count FROM New_Packet WHERE Node = 'Node5' ORDER BY packet_count DESC LIMIT 1 OFFSET 2").fetchall()
		print(query_eleven)

		query_twelve = new_cur.execute("SELECT Node, packet_count FROM New_Packet WHERE Node = 'Node5' ORDER BY packet_count DESC LIMIT 1 OFFSET 3").fetchall()
		print(query_twelve)

		query_thirteen = new_cur.execute("SELECT Node, packet_count FROM New_Packet WHERE Node = 'Node5' ORDER BY packet_count DESC LIMIT 1 OFFSET 4").fetchall()
		print(query_thirteen)



		query_14 = new_cur.execute("SELECT Node, packet_count FROM New_Packet WHERE Node = 'Node5' ORDER BY packet_count DESC LIMIT 5").fetchall()
		print(query_14)


		#gen.delete_contents()
		#gen.GenerateData()
		#insert.deleteData()
		#insert.InsertData()
		count += 1

		#cur.close()
		#new_cur.close()
		#cursor.close()

	#Output()


Output()





#query_three = new_cur.execute("SELECT DISTINCT top(5) packet_count FROM New_Packet WHERE Node = 'Node3' ").fetchall()


#while (count < 5):
#query_three = new_cur.execute("SELECT Node, MAX(packet_count) FROM New_Packet WHERE Node = 'Node3' ").fetchall()
#print(query_three)
	#count += 1

#query_four = new_cur.execute("SELECT Node, MAX (packet_count) FROM New_Packet WHERE Node = 'Node3' AND packet_count NOT IN (SELECT MAX(packet_count) FROM New_Packet WHERE Node = 'Node3')").fetchall()
#print(query_four)

#query_five = new_cur.execute("SELECT Node, MAX(packet_count) FROM New_packet WHERE Node = 'Node 3' AND packet_count NOT IN (SELECT MAX(packet_count) FROM New_Packet WHERE Node = 'Node3' AND packet_count NOT IN (SELECT MAX(packet_count) FROM New_Packet WHERE Node = 'Node3'))").fetchall()
#print(query_five)


#for dat in query_three:
#	print(dat)

#query_three = new_cur.execute("SELECT * FROM New_Packet WHERE (packet_count IN (SELECT TOP(5) FROM New_Packet WHERE Node = 'Node3' ))")






