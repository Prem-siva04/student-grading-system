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






def grade(a):
    if a<=100 or a>=90:
        print("grade is  A")
    elif a<=90 or  a>=75:
        print("grade is B")
    elif a<=75 or a>=50:
        print("grade is C")
    elif a<=50 or a>=25:
        print("grade is D")
    else:
        print("")         




if __name__ == "__main__":
    app.run(debug=True)