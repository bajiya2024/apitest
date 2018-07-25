from sqlalchemy import create_engine

from sqlalchemy import Column, String, Integer, Float

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import TypeDecorator, PickleType

from init import getUrl

#getUrl get the url from init file
path = getUrl()
db = create_engine(path)
base = declarative_base()


class region(base):
	#create a table name region and store the data 
	__tablename__ = 'region'
	id = Column(Integer, primary_key = True)
	name = Column(String)
	type = Column(String)
	parent = Column(String)
	polygon = Column(PickleType) #In the binary format we can unpickle when we need 
	def __init__(self, name, type, parent, polygon):
		self.name = name
		self.type = type
		self.parent = parent
		self.polygon = polygon  
		
if __name__ == "__main__":
	base.metadata.create_all(db)
	
	
	