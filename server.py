from flask import Flask, render_template, redirect, session, jsonify
from Models.game import Game 
app = Flask(__name__)
app.secret_key = 'Rubber Baby Buggy Bumpers'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/start')
def start_game():
    game = Game(10)
    data = game.to_json()
    return jsonify(data)


@app.route('/reveal', methods=['POST'])
def reveal():
    pass

if __name__ == '__main__':
    app.run(debug=True)
