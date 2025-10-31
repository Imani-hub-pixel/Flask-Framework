from flask import Flask
'''
It creates an instance of the flask class, which will be
your WSGI application.

'''
#WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this flask course.This should be an amazing course"

@app.route("/index")
def index():
    return "Welcom to the index page"


if __name__=="__main__":
    app.run(debug=True)
