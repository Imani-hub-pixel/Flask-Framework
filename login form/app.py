from flask import Flask,render_template,request

app=Flask(__name__)
@app.route('/')
def index():
    return render_template('login_form.html')
@app.route('/login',methods=['POST'])
def login():
    name=request.form.get('username')
    return render_template('welcome.html',name=name)