from flask import Flask,render_template,request
app=Flask(__name__)

@app.route('/')
def index():
    return render_template("form.html")
@app.route('/greet',methods=['POST'])
def welcome():
    name=request.form.get('name',"world")
    return render_template("index.html",name=name)


if __name__ == "__main__":
    app.run(debug=True)