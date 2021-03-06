from databases import *
from os import urandom
from flask import Flask, render_template, url_for , request ,session, escape, request, redirect
app = Flask(__name__)

app.secret_key = urandom(24)

@app.route('/' , methods=['GET' , 'POST'])
def register():
	if request.method== 'GET':
		return render_template('register.html')
	else:	
		fname = request.form['txb_fname']
		lanme = request.form['txb_lname']
		username = request.form['txb_username']
		password = request.form['txb_pass']
		cheack_user=query_by_name(username)

		if cheack_user==None:		
			Register(fname , lanme , username , password)
			session['username']=username
			return redirect(url_for('home_page' ))
		else :
			return render_template('register.html' , taken='this user name is taken')
    

@app.route('/Login', methods=['GET' , 'POST'])
def LogIn_page():
	if request.method== 'GET':
		return render_template('LogIn.html')
	else:	
		username = request.form['txb_uname']
		password = request.form['txb_pass']
		u=query_by_name(username)
		if u is not None and u.uname==username and u.password==password:
			session['username']=username
			return redirect(url_for('home_page' ))
		else:

			return render_template('LogIn.html' , wrong='wrong password or username')

@app.route('/sign_out')
def sign_out():
    session.pop('username')
    return render_template('LogIn.html')

@app.route('/home' , methods=['GET' , 'POST'])
def home_page():
	if session.get('username')==None:
		return redirect(url_for('LogIn_page'))
	if request.method== 'GET':	
		posts = query_all_posts()
		return render_template('home.html' ,posts=posts , username=session.get('username') )
	posts = query_all_posts()	
	return render_template('home.html' ,posts=posts , username=session.get('username') )


@app.route('/share' , methods=['GET' , 'POST'])
def Share():
	if session.get('username')==None:
		return redirect(url_for('LogIn_page'))
	if request.method== 'GET':
		posts = query_all_posts()
		return render_template('Share.html' , username=session.get('username') )
	else:	
		post = request.form['txb_post']
		nickName = request.form['txb_name']
		u=query_by_name(nickName)
		add_post(nickName , post , session.get('username'))
		posts = query_all_posts()
		return redirect(url_for('home_page'))


@app.route('/delete')
def delete_all():
	puname = session.get('username')
	delete(puname)
	post=query_all_posts()
	return render_template('home.html' , posts=post , username=session.get('username'))

# @app.route('/delete1post')
# def delete_one(id):
# 	pass
# 	puname = session.get('username')
# 	delete_one_post(  , puname)
# 	psot=query_all_posts()
# 	return render_template('home.html' posts=post , username=session.get('username'))

@app.route('/delete_one/<int:post_id>')
def delete_post(post_id):
	delete_one_post(post_id, session.get('username'))
	return redirect(url_for('home_page'))

@app.route('/Quotes')
def Quotes():
	return render_template('quotes.html' , username=session.get('username'))

@app.route('/about')
def About():
	return render_template('About.html' , username=session.get('username'))
#@app.route('/student/<int:student_id>')
#def display_student(student_id):
#    return render_template('student.html', student=query_by_id(student_id))
'''
@app.route("/add" , methods=['GET' , 'POST'])

def add_student_route():
	if rquest.method== 'GET':
		return render_template('add.html')
	else:
		name=rquest.form('username') 
		year=rquest.form('year')
		finish_lab=True
		add_student(name , year , finish_lab)
		return render_template('student.html' ,name=name , year=year , finish_lab=finish_lab)

'''
app.run(debug=True)

