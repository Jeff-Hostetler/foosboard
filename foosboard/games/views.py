from flask import render_template, request, flash, redirect
from foosboard import app, db
from foosboard.games.models import Game


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
