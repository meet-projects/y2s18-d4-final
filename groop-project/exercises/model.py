from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
	"""
	Create a students table. This table has
	4 columns.

	The first column, student_id is
	the primary key for the table. The second
	column is a string, representing the name of
	the student. The third column is an integer,
	representing the year the student was born. The last
	column is a Boolean, representing whether or not the student
	has completed the lab.
	"""
	__tablename__ = 'users'
	user_id = Column(Integer, primary_key=True)
	fname = Column(String)
	lname = Column(String)
	password = Column(Integer)

	def __repr__(self):
		return ("User First Name: {}\n"
				"User Last Year: {} \n"
				"User Password: {}").format(
					self.fname,
					self.lname,
					self.password)


