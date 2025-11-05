from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')
def calculator():
    return render_template("calculator.html",result=None)

@app.route('/calculate',methods=['POST'])
def calculate():
    num1=float(request.form.get('num1'))
    num2=float(request.form.get('num2'))
    operation=request.form['operation']

    if operation=='add':
        result=num1+num2
    elif operation=="subtract":
        result=num1-num2
    elif operation=="multiply":
        result=num1*num2
    elif operation=='divide':
        if num2==0:
            result="Cannot divide by zero"
        else:
            result=round(num1/num2)
    else:
        print("Invalid input!")

    return render_template("calculator.html",result=result)

if __name__=="__main__":
    app.run(debug=True)

