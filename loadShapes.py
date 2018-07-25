from shapely.geometry import Polygon
import urllib, json

from sqlalchemy import create_engine
from Models import region
from sqlalchemy.orm import sessionmaker
import pickle as cPickl

from init import getUrl

path = getUrl()
db = create_engine(path)

#store geojson data in database
def parse():
	Session = sessionmaker(db)
	session = Session()
	url = 'https://gist.githubusercontent.com/ramsingla/6202001/raw/1dc42df3c6d8f4db95b7f7b65add1f520578ab33/map.geojson'
	json_url =urllib.urlopen(url)
	data = json.loads(json_url.read())
  
	for f in data['features']:
		
		pickledPolygon = cPickle.dumps(Polygon(f['geometry']['coordinates'][0]))
		new = region(f['properties']['name'], f['properties']['type'], f['properties']['parent'], pickledPolygon)
		session.add(new)
	session.commit()

if __name__ == "__main__":
    parse()