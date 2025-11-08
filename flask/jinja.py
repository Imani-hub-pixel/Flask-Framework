#building url dynamically
#Variable rule
#Jinja 2 template engine
"""
jinja 2 template engine.There are multiple wasy to read dat source from backend:
{{ }} expressions to print output in html
{%  %} conditional statements,while loop,for loops etc
{#  #} comments
"""


#Intergrating html with  flask
from flask import Flask, redirect,render_template,request, url_for
'''
It creates an instance of the flask class, which will be
your WSGI application.

'''
#WSGI Application
app=Flask(__name__)

@app.route("/",methods=['GET'])
def welcome():
    return render_template('index.html')


@app.route("/index",methods=['GET'])
def index():
    return "Welcome to the index page"

@app.route('/about' )
def about():
    return render_template('about.html')

@app.route('/submitdemo',methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        return f"Hello {name}"
    return render_template('form.html')
#Variable rule

"""@app.route('/success/<int:score>')
def success(score):
    return "The marks you got is "+ str(score)"""
#Building url dynamically
@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res='PASSED'
    else:
        res='FAILED'
    return render_template('result.html',result=res)


@app.route('/successres/<int:score>')
def successres(score):
    res=""
    if score>=50:
        res='PASSED'
    else:
        res='FAILED'
    
    exp={'score':score,'res':res}

    return render_template('result1.html',results=exp)
#if condition
@app.route('/successif/<int:score>')
def successif(score):
    return render_template('result2.html',results=score)


def fail(score):
    return render_template('result2.html',results=score)

@app.route('/submit',methods=['POST','GET'])
def submitres():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])

        total_score=(science+maths+c+data_science)/4

        return redirect(url_for('successres',score=total_score))
    return render_template('getresults.html')

if __name__=="__main__":
    app.run(debug=True)
