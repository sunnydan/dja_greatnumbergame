from flask import Flask, render_template, redirect, request, session
import random
app = Flask(__name__)
app.secret_key = "420blazeit"

@app.route('/')
def index():
    session['solution'] = random.randint(1,100)
    print session['solution']
    return render_template('index.html', result="none")

@app.route('/', methods=["POST"])
def index2():
    print session['solution']
    guess = request.form['guess']
    print guess
    if guess == "reset":
        return redirect('/')
    elif int(guess) == session['solution']:
        return render_template('index.html', result="correct")
    elif int(guess) > session['solution']:
        return render_template('index.html', result="high")
    else:
        return render_template('index.html', result="low")
    
app.run(debug=True)