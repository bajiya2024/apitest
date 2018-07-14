import csv
import psycopg2
#connect to database
conn = psycopg2.connect("host='localhost' port='5432' dbname='testapi' user='postgres' password='root'")


cur = conn.cursor()

def create_tables():
	#create a table command
	commands = ("""create table apidata (pin int PRIMARY KEY ,
	placename  varchar(50) not NULL,
	cityname  varchar(50) not Null,
	latitude float not NULL,
	longitude float not NULL,
	accuracy float)""")
	
	#create table 
	cur.execute(commands)
	
	#close connection from postgresql 
	cur.close()
	#commit the changes
	conn.commit()
if __name__ == '__main__':
    create_tables()
	

#add csv file into the database(postgresql)
cur.execute("""Copy apidata from 'C:\Users\savitri chopra\Desktop\dharmaWork\IN.csv'  delimiter ',' csv header;""")

#changes in data
conn.commit()

#close the data base 
conn.close()

