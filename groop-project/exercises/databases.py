from model import Base, User

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///students.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def register(fname, lname , password ):
	"""
	Add a student to the database, given
	their name, year, and whether they have127.0.0.1:5000
	finished the lab.
	"""
	user_object = User(
		fname=fname,
		lname=lname,
		password=password)
	session.add(user_object)
	session.commit()

def query_by_name(name):
	"""
	Find the first student in the database,
	by their name
	"""
	user = session.query(User).filter_by(
		name=name).first()
	return user

def query_all():
	"""
	Print all the students in the database.
	"""
	users = session.query(User).all()
	return users

def delete_User(name):
	"""
	Delete all students with a certain name
	from the database.
	"""
	session.query(User).filter_by(
		name=name).delete()
	session.commit()

def update_password(name, password):
	"""
	Update a student in the database, with 
	whether or not they have finished the lab
	"""
	user_object = session.query(User).filter_by(
		name=name).first()
	user_object.password = password
	session.commit()

def query_by_id(user_id):
    user = session.query(User).filter_by(
        user_id=user_id).first()
    return user

register('noam', 'mertsen' , '123456789')