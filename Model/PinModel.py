

#Its handle pin, InsertData, getplace calculation or all methods of pin, InsertData, getplace 

import psycopg2
#connect to data using psycopg2 library
conn = psycopg2.connect("host='localhost' port='5432' dbname='testapi' user='postgres' password='root'")


from shapely.geometry.polygon import Polygon
from shapely.geometry import Point

import pickle as cPickle
from Models import region


from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from init import getUrl
path = getUrl()
db = create_engine(path)






fields = ['pin', 'place_name', 'city_name', 'latitude', 'longitude']
boundary_restriction = 1 #km

def getNearbyPins(lat, long, radius, pin_only=0):
	rows = []
	cmd = """select %s from apidata WHERE earth_box(ll_to_earth(%s,%s), %s) @> ll_to_earth(latitude, longitude);"""%(",".join(fields), lat, long, radius*1000)
	cur = conn.cursor()
	cur.execute(cmd)
	rows = cur.fetchall()
	cur.close()
	if pin_only:
		rows = map(lambda x: x[0], rows)
	else:
		rows = map(lambda x:{fields[0]:x[0], fields[1]:x[1], fields[2]:x[2], fields[3]:x[3], fields[4]:x[4],}, rows)
	return rows

def getbyPin(pin):
	rows = []
	cmd = """select * from apidata WHERE pin=%s"""%pin
	cur = conn.cursor()
	cur.execute(cmd)
	rows = cur.fetchall()
	cur.close()
	rows = map(lambda x:{fields[0]:x[0], fields[1]:x[1], fields[2]:x[2], fields[3]:x[3], fields[4]:x[4],}, rows)
	return rows

def checkPinExists(pin):
	flag = False
	cmd = """select count(*) from apidata WHERE pin=%s"""%pin
	cur = conn.cursor()
	cur.execute(cmd)
	result = cur.fetchone()
	print result
	cur.close()
	if(result[0])>0:
		flag = True
	return flag

def checkInrange(lat, long, radius):
	flag = False
	cmd = """select count(*) from apidata WHERE earth_box(ll_to_earth(%s,%s), %s) @> ll_to_earth(latitude, longitude);"""%(lat, long, radius*1000)
	cur = conn.cursor()
	cur.execute(cmd)
	result = cur.fetchone()
	cur.close()
	if(result[0])>0:
		flag = True
	return flag
	
def InsertData(data):
	result = {'msg':"", 'res':[]}
	if checkPinExists(data['pin']):
		result['msg'] = "pin already exists."
		return result
	if checkInrange(data['latitude'], data['longitude'], boundary_restriction):
		result['msg'] = "Too close to other pins"
		return result
	#write in database
	rows = []
	cmd = """INSERT INTO apidata (%s) VALUES (%s, '%s', '%s', %s, %s);"""%(",".join(fields), data[fields[0]], data[fields[1]], data[fields[2]], data[fields[3]], data[fields[4]])
	cur = conn.cursor()
	cur.execute(cmd)
	conn.commit()
	cur.close()
	#fetch and check
	res = getbyPin(data['pin'])
	if len(res)==0:
		result['msg'] = "Unable to insert"
		return result
	result['msg'] =  "success"
	result['res'] = res
	return result
	
	
	
#get place 	
def getplace(data):
	Session = sessionmaker(db)
	session = Session()
	allData = session.query(region).all()

	givenLocation = Point(data['longitude'], data['latitude'])
	for i in allData:
		unpickledPolygon = cPickle.loads(i.polygon)
		#print (i.parent, unpickledPolygon)
		if unpickledPolygon.contains(givenLocation):
			return {i.type:i.name, 'Region':i.parent}
	return ('Nowhere')

	


