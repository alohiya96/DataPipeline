from faker import Faker
from faker.providers import internet
import random

#Fake time, fake IP Protocol, fake source address, fake destination address, fake protocol(TCP, UDP)

def GenerateData():

	Transport_Protocol = ['TCP', 'UDP']
	Internet_Protocol = ['IP']
	Nodes = ['Node1', 'Node2', 'Node3', 'Node4', 'Node5', 'Node6', 'Node7', 'Node8', 'Node9', 'Node10']
	Interface = ['Int1', 'Int2', 'Int3', 'Int4', 'Int5', 'Int6', 'Int7', 'Int8', 'Int9', 'Int10']

	file = open('Packet.csv', 'w') 
	fake = Faker()

#create date time
	Faker.seed(0)

	for _ in range(100):
		file.write(" " + fake.date() + ", "  + random.choice(Internet_Protocol) +
		", " +  fake.ipv4_private()  
		 + ","  + fake.ipv4_private() + "," +  random.choice(Transport_Protocol) + ", ")

		file.write(str(random.randint(1, 1000000)))
		file.write("," + random.choice(Nodes) + ", " + random.choice(Interface))
		file.write("\n")

	for _ in range(3):
		file.write( " " + fake.date() + ", "  + random.choice(Internet_Protocol) + ", " + '10.1.1.1' + "," + '20.1.1.1' + "," + random.choice(Transport_Protocol) + ", ")
		file.write(str(random.randint(1, 1000000)))
		file.write("," + random.choice(Nodes) + ", " + random.choice(Interface))
		file.write("\n")


def delete_contents():
	file = open('Packet.csv', 'w+')
	file.close()

delete_contents()
GenerateData()







