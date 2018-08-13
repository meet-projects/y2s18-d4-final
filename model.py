from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
	__tablename__ = 'users'
	user_id = Column(Integer, primary_key=True)
	fname = Column(String)
	lname = Column(String)
	uname = Column(String)
	password = Column(String)

	def __repr__(self):
		return ("User First Name: {}\n"
				"User Last Year: {} \n"
				"User Name: {} \n"
				"User Password: {}").format(
					self.fname,
					self.lname,
					self.uname,
					self.password)

class Posts(Base):
	__tablename__='posts'
	post_id = Column(Integer, primary_key=True)
	uname = Column(String)
	post = Column(String)

	def __repr__(self):
		return ("Post id: {}\n"
				"User Name: {} \n"
				"Post: {}").format(
					self.post_id,
					self.uname,
					self.post)
