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
	username = Column(Integer)

	def __repr__(self):
		return ("post_id: {} \n"
				"User Name: {} \n"
				"Post: {} \n"
				"username {} \n").format(
					self.post_id,
					self.uname,
					self.post,
					self.username)

class Comments(Base):
	__tablename__='comments'
	comment_id = Column(Integer , primary_key=True)
	comment_body = Column(String)
	commentor_name = Column(String)

	def __repr__(self):
		return ("comment_id {} \n"
				"comment_body {} \n"
				"commentor_name {} \n").format(
					self.post_id,
					self.comment_body,
					self.commentor_name)




			