from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def game():
    return render_template('game.html', name="Andrea's Game")

@app.route('/new')
def a():
    return "This is something new!"

