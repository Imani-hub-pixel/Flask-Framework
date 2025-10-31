#Intergrating html with  flask
from flask import Flask,render_template
'''
It creates an instance of the flask class, which will be
your WSGI application.

'''
#WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return render_template('index.html')

@app.route("/index")
def index():
    return "Welcome to the index page"

@app.route('/about')
def about():
    return render_template('about.html')


if __name__=="__main__":
    app.run(debug=True)
