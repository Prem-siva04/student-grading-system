from flask import Flask , render_template

app=Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/login')
def loginpage():
    return render_template('login.html')

@app.route('/AddGrades')
def  addgrades():
    return render_template('Add_Grades.html')

@app.route('/ViewGrades')
def viewgrades():
    return  render_template('View_Grades.html')



@app.route('/AddStudents')
def AddStudents():
    return render_template('Add_Student.html')

if __name__ == "__main__":
    app.run(debug=True)