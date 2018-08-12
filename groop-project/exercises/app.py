from databases import *
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def register():
    return render_template('register.html')

@app.route('/home')
def home_page():
	return render_template('hello.html')

@app.route('/student/<int:student_id>')
def display_student(student_id):
    return render_template('student.html', student=query_by_id(student_id))

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

app.run(debug=True)
