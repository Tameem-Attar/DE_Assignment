from flask import *

app=Flask(__name__) 




@app.route("/home")
def home():
    return "Home Page Is Loaded" 
@app.route("/employees")
def return_list():
    return "Employees Page Is Loaded" 
@app.route("/projects/<name>") 
def return_projects(name):
    return render_template("htmlforflask.html",peru=name)


if __name__=='__main__':
    app.run(debug=True) 