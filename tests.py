import unittest
#using unittest module

from json import loads
from urllib import  urlopen
import  requests
import urllib
from requests import post
class test(unittest.TestCase):
	
	#test case fro ping using postgres
	def test_pin_using_postgres(self):
		url = "http://127.0.0.1:5000/get_using_postgres"
		
		testConditions = [{"input":"?radius=1&location=28.6333,77.25", "output":[{'city_name':'New Delhi','latitude':28.6333,'longitude':77.25,'pin':110002,'place_name':'Darya Ganj'}]},\
		             {"input":"?radius=5&location=26.6833,77.25", "output":[{ 'city_name': 'Rajasthan','latitude': 26.6333,'longitude': 77.2167,'pin': 322242,'place_name': 'Machilpur'},{"city_name": "Rajasthan","latitude": 26.6333,"longitude": 77.2167, "pin": 322243,"place_name": "Kailadevi"},
					 {"city_name": "Rajasthan","latitude": 26.6333,"longitude": 77.2167,"pin": 322246,"place_name": "Talchiri"},
					 {"city_name": "Rajasthan","latitude": 26.6333,"longitude": 77.2167,"pin": 322247,"place_name": "Chainpur"},
					 {"city_name": "Rajasthan","latitude": 26.6333,"longitude": 77.2167,"pin": 322248,"place_name": "Salempur Chowki"}]}]
		
		for R in testConditions:
			self.assertEqual(loads(urllib.urlopen(url+R["input"]).read()),R["output"])
	
	

	#test case for find place_name
	def test_find_place(self):
		url = "http://127.0.0.1:5000/find_place"
		
		testConditions = [ {"input":"?latitude=28.65&longitude=77.2167", "output":{"Region": "Delhi","Zone": "North Delhi"}},\
		{"input":"?latitude=28.6333&longitude=77.4567", "output":{"City": "Ghaziabad","Region": "Uttar Pradesh"}},\
		{"input":"?latitude=30.65&longitude=75.2167", "output":"Nowhere"}]
		
		for  R in testConditions:
			self.assertEqual(loads(urllib.urlopen(url+R["input"]).read()), R["output"])
			
			
	#test case for get using self			
	def test_get_using_self(self):
		url = "http://127.0.0.1:5000/get_using_self"
		
		
		testConditions = [{"input":"?radius=4&latitude=28.6333&longitude=77.25", "output":[110001,110002,110003,110004,110006,110008,
		110051,110052,110053,110054,110055, 110056,110057,110058,110059]},\
		{"input":"?radius=100&latitude=26.5&longitude=70.2", "output":[344013,344014,344015,345030]}]
		
		for R in testConditions:
			self.assertEqual(loads(urllib.urlopen(url+R["input"]).read()),R["output"])	
			

	#test case for post location		
	def test_post_location(self):
		url = "http://127.0.0.1:5000/post_location"
		
		testConditions = [ {"input":{"?pin=110002&place_name=abc&city_name=def&latitude=28.6333&longitude=77.25"},
							"output":{"msg": "pin already exists.","res": []}}]		
		for R in testConditions:
			self.assertEqual(loads(post(url, data=R['input']).text), R["output"])
			
if __name__ == '__main__':
	unittest.main()
	