from databases import *
from flask import Flask, render_template, url_for , request
app = Flask(__name__)

@app.route('/' , methods=['GET' , 'POST'])
def register():
	if request.method== 'GET':
		return render_template('register.html')
	else:	
		fname = request.form['txb_fname']
		lanme = request.form['txb_lname']
		username = request.form['txb_username']
		password = request.form['txb_pass']
		Register(fname , lanme , username , password)
		return render_template('home.html' , userName = username)
	
    

@app.route('/Login', methods=['GET' , 'POST'])
def LogIn_page():
	if request.method== 'GET':
		return render_template('LogIn.html')
	else:	
		username = request.form['txb_uname']
		password = request.form['txb_pass']
		u=query_by_name(username)
		if u is not None and u.uname==username and u.password==password:
			return render_template('home.html', userName=username )

@app.route('/Home' , methods=['GET' , 'POST'])
def home_page():
	if request.method== 'GET':
		return render_template('home.html')
	else:	
		post = request.form['txb_post']
		nickName = request.form['txb_name']
		u=query_by_name(nickName)
		add_post(nickName , post)
		return render_template('home.html')

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
