from flask import Flask, json, jsonify, request

import Model.PinModel as pm

import Helper.InputHandler as inp

from utilities import getusingself
app = Flask(__name__)



APIs = {}
APIs['query'] = "http://127.0.0.1:5000/get_using_postgres?radius=3&location=28.6333,77.25&pin_only=0"
APIs["exists"] = "http://127.0.0.1:5000/post_location?pin=110002&place_name=abc&city_name=def&latitude=28.6333&longitude=77.25"
APIs['close'] = "http://127.0.0.1:5000/post_location?pin=100003&place_name=abc&city_name=def&latitude=28.6434&longitude=77.25"
APIs['new'] = "http://127.0.0.1:5000/post_location?pin=100003&place_name=abc&city_name=def&latitude=28.8434&longitude=77.25"
APIs['find_place'] = "http://127.0.0.1:5000/find_place?latitude=28.65&longitude=77.2167"
APIs['get_using_self'] = "http://127.0.0.1:5000/get_using_self?radius=10&latitude=28.6333&longitude=77.25"



#get_using_postgres API (GET)
@app.route('/', methods =['GET'])
def index():
	return jsonify(APIs)

@app.route('/get_using_postgres', methods=['GET'])
def get_using_postgres():
	error= {"error":"invalid params", "msg":""}
	try:
		params = request.args;
		err_msg, inputs =  inp.getQueryInput(params)
	except Exception, e:
		print e
		error['msg'] = "please provide valid params"
		return jsonify(error)
	if err_msg:
		error['msg'] = err_msg
		return jsonify(error)
	
	nearby_pins  = pm.getNearbyPins(inputs['lat'],inputs['long'], inputs['radius'], inputs['pin_only'])
	return jsonify(nearby_pins)


	

#post_location API (POST)

@app.route('/post_location', methods=['GET', 'POST'])
def post_location():
	error= {"error":"invalid params", "msg":""}
	#if request.headers['Content-Type'] == 'application/json':
	#	error['data'] = request.data
		
	try:
		params = request.args;
		err_msg, inputs =  inp.getPostInput(params)
	except Exception, e:
		print e
		error['msg'] = "please provide valid params"
		return jsonify(error)
	if err_msg:
		error['msg'] = err_msg
		return jsonify(error)
	
	success_json  = pm.InsertData(inputs)
	return jsonify(success_json)
	
	
#find_place (GET)	
@app.route('/find_place', methods =['GET'] )
def find_place():
	error= {"error":"invalid params", "msg":""}
	try:
		params = request.args;
		err_msg, inputs =  inp.getFindPlaceInput(params)
	except Exception, e:
		print e
		error['msg'] = "please provide valid params"
		return jsonify(error)
	if err_msg:
		error['msg'] = err_msg
		return jsonify(error)
	place = pm.getplace(inputs)
	return (jsonify(place))


	
#get_using_self API
@app.route('/get_using_self', methods=['GET'])
def get_using_self():
	error= {"error":"invalid params", "msg":""}
	try:
		params = request.args;
		err_msg, inputs =  inp.getUsingSelfInput(params)
	except Exception, e:
		print e
		error['msg'] = "please provide valid params"
		return jsonify(error)
	if err_msg:
		error['msg'] = err_msg
		return jsonify(error)
	result = getusingself(inputs)
	return (jsonify(result))
	

if __name__=='__main__':
	app.run(debug = True)


	
'''
The url_for() function is very useful for dynamically building a URL for a specific function
https://gist.github.com/norman/1535879#file-earthdistance-rb-L50
'''