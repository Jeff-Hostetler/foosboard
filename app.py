import os
from flask import Flask, request, render_template, redirect, flash
from flask.ext.sqlalchemy import SQLAlchemy

class Config(object):
    DEBUG = True
    SECRET_KEY = 'foosball'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

app = Flask(__name__)
app.config.from_object(Config())

db = SQLAlchemy(app)

class Game(db.Model):
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True)

    team1defense = db.Column(db.String())
    team1offense = db.Column(db.String())
    team1score = db.Column(db.Integer())
    team2offense = db.Column(db.String())
    team2defense = db.Column(db.String())
    team2score = db.Column(db.Integer())

    def __init__(self, team1defense, team1offense, team1score, team2offense, team2defense, team2score):
        self.team2score = team2score
        self.team2defense = team2defense
        self.team2offense = team2offense
        self.team1score = team1score
        self.team1defense = team1defense
        self.team1offense = team1offense

    def __repr__(self):
        return '<id {}>'.format(self.id)

    @property
    def serialize(self):
        return {
            "id": self.id,
            "team1defense": self.team1defense,
            "team1offense": self.team1offense,
            "team1score": self.team1score,
            "team2offense": self.team2offense,
            "team2defense": self.team2defense,
            "team2score": self.team2score
        }

@app.route('/', methods=['GET'])
def index():
    games = Game.query.all()
    return render_template('index.html', games=games)

@app.route('/games', methods=['POST'])
def create_game():
    game = Game(request.form["team1defense"],
                request.form["team1offense"],
                request.form["team1score"],
                request.form["team2offense"],
                request.form["team2defense"],
                request.form["team2score"])
    db.session.add(game)
    db.session.commit()

    flash('Game submitted')
    return redirect("/")

@app.route('/games/new', methods=['GET'])
def new_game():
    return render_template("games/new.html",
                           team1defense=request.args["team1defense"],
                           team1offense=request.args["team1offense"],
                           team2defense=request.args["team2defense"],
                           team2offense=request.args["team2offense"])

port = os.getenv('VCAP_APP_PORT', '5000')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port))
