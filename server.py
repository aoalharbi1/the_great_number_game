from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')         
def index():
    if 'num' not in session:
        session['num'] = random.randint(1, 100)
    return render_template("index.html")

@app.route('/check_guess', methods=['POST'])         
def check():
    guess = int(request.form['guess'])

    if guess > session['num']:
        session['guess'] = "h"
    elif guess < session['num']:
        session['guess'] = "l"
    else:
        session['guess'] = "got it"

    return render_template("index.html")

@app.route('/again')
def clear_session():
    session.clear()
    return redirect('/')

if __name__=="__main__":   
    app.run(debug=True)    