from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Post(Base):
	__tablename__ = 'posts'
	post_id = Column(Integer, primary_key=True)
	title = Column(String)
	body = Column(String)

	def __repr__(self):
		return ("User First Name: {}\n"
				"User Last Year: {} \n"
				"User Name: {} \n"
				"User Password: {}").format(
					self.fname,
					self.lname,
					self.uname,
					self.password)


