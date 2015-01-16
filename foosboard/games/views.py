from flask import render_template, request, flash, redirect, make_response, jsonify
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

@app.route('/api/games', methods=['POST'])
def api_create_game():
    game = Game(request.json["team1defense"],
                request.json["team1offense"],
                request.json["team2offense"],
                request.json["team2defense"])
    db.session.add(game)
    db.session.commit()

    return make_response(jsonify(game.serialize()), 201)

@app.route('/api/games/<int:game_id>', methods=['PUT'])
def api_show_game(game_id):
    game = Game.query.get(game_id)

    game.team1score = request.json["team1score"]
    game.team2score = request.json["team2score"]

    db.session.add(game)
    db.session.commit()

    return jsonify(game.serialize())

@app.route('/api/games', methods=['GET'])
def api_index():
    games = Game.query.all()
    return jsonify({'games': [game.serialize() for game in games]})

@app.route('/api/games/<int:game_id>', methods=['GET'])
def api_update_game(game_id):
    game = Game.query.get(game_id)

    return jsonify(game.serialize())

@app.errorhandler(400)
def not_found(_):
    return make_response(jsonify({'error': 'Bad request'}), 400)

@app.errorhandler(404)
def not_found(_):
    return make_response(jsonify({'error': 'Not found'}), 404)
