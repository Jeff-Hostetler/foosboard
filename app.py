from flask import Flask, request, render_template, redirect, flash
from flask.ext.sqlalchemy import SQLAlchemy

class Config(object):
    DEBUG = True
    SECRET_KEY = 'foosball'
    SQLALCHEMY_DATABASE_URI = 'postgresql://pivotal@localhost/foosboard'

app = Flask(__name__)
app.config.from_object(Config())

db = SQLAlchemy(app)

class Game(db.Model):
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True)

    team1player1 = db.Column(db.String())
    team1player2 = db.Column(db.String())
    team1score = db.Column(db.Integer())
    team2player1 = db.Column(db.String())
    team2player2 = db.Column(db.String())
    team2score = db.Column(db.Integer())

    def __init__(self, team1player1, team1player2, team1score, team2player1, team2player2, team2score):
        self.team2score = team2score
        self.team2player2 = team2player2
        self.team2player1 = team2player1
        self.team1score = team1score
        self.team1player1 = team1player1
        self.team1player2 = team1player2

    def __repr__(self):
        return '<id {}>'.format(self.id)

    @property
    def serialize(self):
        return {
            "id": self.id,
            "team1player1": self.team1player1,
            "team1player2": self.team1player2,
            "team1score": self.team1score,
            "team2player1": self.team2player1,
            "team2player2": self.team2player2,
            "team2score": self.team2score
        }

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/games', methods=['POST'])
def create_game():
    print request.form

    game = Game(request.form["team1player1"],
                request.form["team1player2"],
                request.form["team1score"],
                request.form["team2player1"],
                request.form["team2player2"],
                request.form["team2score"])
    db.session.add(game)
    db.session.commit()

    flash('Game submitted')
    return redirect("/")

if __name__ == "__main__":
    app.run()
