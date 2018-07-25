'''it calculate get self function related work like find distance and other'''

import sys;

from sqlalchemy import create_engine
from math import radians, sin, cos, atan2, sqrt

#connect to the database
db_string = "postgresql://postgres:root@localhost/testapi"

db = create_engine(db_string)



#distance to calculate distance between two points
def distance(a, b):

    lat1 = float(a[0])
    lat2 =float((b.latitude))
	
    lon1 = float(a[1])
    lon2 = float(b.longitude)
	
    phi_1 = radians((lat1))	
    phi_2 = radians(lat2)
    delta_phi = radians(lat2-lat1)
    delta_lambda = radians(lon2-lon1)
    x = sin(delta_phi/2.0)**2 + cos(phi_1)*cos(phi_2)*sin(delta_lambda/2.0)**2   #It uses Haversine formula
    y=2*atan2(sqrt(x),sqrt(1-x))
	#radius or R in km
    R = 6356
    return R*y

	
def getusingself(data):
	#fecth data from apidata table 
	result_set = db.execute("SELECT * FROM apidata")
	new = [data['latitude'], data['longitude']]
	result = [i.pin for i in result_set if distance(new, i) <= data['radius']]
	return result
	