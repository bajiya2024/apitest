import sys;

fields = ['pin', 'place_name', 'city_name', 'latitude', 'longitude']   #fields which in database

def isValidlatlong(lat, long):
	flag =True
	return flag
'''********************** Get inputs for Query or get_by_PostgreSQL API *****************'''	
#Get query inputs	
def getQueryInput(params):#give getQueryInput input 
	inputs = {}
	err_msg = ""
	radius = float(params.get('radius'))
	if not radius:
		return ("invalid radius", inputs)
	inputs['radius'] = radius
	location = params.get('location')
	if not location:
		return ("Please provide location", inputs)
	lat_long = location.split(',')
	if len(lat_long)!=2:
		return ("Please use comma separated lat and long in location", inputs)
	lat = float(lat_long[0].strip()) #"28.6333";
	long = float(lat_long[1].strip()) #"77.25";
	if not isValidlatlong(lat, long):
		return ("Please provide valid lat and long in location", inputs)
	inputs['lat']= lat
	inputs['long'] = long
	inputs['pin_only'] = int(params.get('pin_only', 0))
	return (err_msg, inputs)

	
	
	
'''********************** Get inputs for Post API *****************'''	
#get post inputs	
def getPostInput(params):
	inputs = {}
	err_msg = ""
	for f in fields:
		if f in params and params.get(f):
			inputs[f]= params.get(f)
		else:
			return ("Please provide param : %s"%f, inputs)
	return (err_msg, inputs)
	
	

	
	
'''********************** Get inputs for FindPlace API *****************'''		
#get find place parameter or inputs
new_field = ['latitude', 'longitude']

def getFindPlaceInput(params):
	inputs = {}
	err_msg = ""
	for f in new_field:
		if f in params and params.get(f):
			inputs[f] =float(params.get(f))
		else:
			return ("Please provide valid parameter: %s"%f, inputs)
	return (err_msg, inputs)
	
	
	

	
'''********************** Get inputs for using_self API *******************'''		
#input parameters for self 
	
new_field2 = ['latitude', 'longitude']	
def getUsingSelfInput(params):
	inputs = {}
	err_msg = ""
	radius = float(params.get('radius'))
	if not radius:
		return ("invalid radius", inputs)
	inputs['radius'] = radius
	
		
	for f in new_field2:
		if f in params and params.get(f):
			inputs[f] = float(params.get(f))
		else:
			return ("Please provide valid parameter: %s"%f, inputs)
	return (err_msg, inputs)
