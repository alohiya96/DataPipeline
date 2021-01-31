from faker import Faker  #import this package to generate fake data
import random        #generate random data

#Fake time, fake IP Protocol, fake source address, fake destination address, fake protocol(TCP, UDP)

def GenerateData():

	#lists from which random elements will be chose
	Transport_Protocol = ['TCP', 'UDP']
	Internet_Protocol = ['IP']
	Nodes = ['Node1', 'Node2', 'Node3', 'Node4', 'Node5', 'Node6', 'Node7', 'Node8', 'Node9', 'Node10']
	Interface = ['Int1', 'Int2', 'Int3', 'Int4', 'Int5', 'Int6', 'Int7', 'Int8', 'Int9', 'Int10']

	file = open('Packet.csv', 'w')    #write fake data to this file
	fake = Faker() #create and initialize fake generator

#create date time
	Faker.seed(0)


	#Fake date, src)address, dest_address is chosen. Random IP and transport protocol is chosen and written to csv file
	for _ in range(100):   #generate 100 rows of data
		file.write(" " + fake.date() + ", "  + random.choice(Internet_Protocol) +
		", " +  fake.ipv4_private()  
		 + ","  + fake.ipv4_private() + "," +  random.choice(Transport_Protocol) + ", ")

		file.write(str(random.randint(1, 1000000)))   #random packet count
		file.write("," + random.choice(Nodes) + ", " + random.choice(Interface))  #random Node name and INterface name written to csv file
		file.write("\n") 

	for _ in range(3): #3 rows of additional data (customized data)
		file.write( " " + fake.date() + ", "  + random.choice(Internet_Protocol) + ", " + '10.1.1.1' + "," + '20.1.1.1' + "," + random.choice(Transport_Protocol) + ", ")
		file.write(str(random.randint(1, 1000000)))
		file.write("," + random.choice(Nodes) + ", " + random.choice(Interface))
		file.write("\n")


def delete_contents():
	file = open('Packet.csv', 'w+')  #truncate the csv file 
	file.close()

delete_contents()  #ensures new data is generated everytime this program is run
GenerateData()  #call this function to generate data







