from flask import request, make_response, jsonify
from flask_cors import cross_origin

from foosboard import app, db
from foosboard.games.models import Game


@cross_origin()
@app.route('/api/games', methods=['POST'])
def api_create_game():
    print request.json
    game = Game(request.json["team1defense"],
                request.json["team1offense"],
                request.json["team2offense"],
                request.json["team2defense"])
    db.session.add(game)
    db.session.commit()

    return make_response(jsonify(game.serialize()), 201)

@cross_origin()
@app.route('/api/games/<int:game_id>', methods=['PATCH'])
def api_show_game(game_id):
    game = Game.query.get(game_id)

    game.team1score = request.json["team1score"]
    game.team2score = request.json["team2score"]

    db.session.add(game)
    db.session.commit()

    return jsonify(game.serialize())

@cross_origin()
@app.route('/api/games', methods=['GET'])
def api_index():
    games = Game.query.all()
    return jsonify({'games': [game.serialize() for game in games]})

@cross_origin()
@app.route('/api/games/<int:game_id>', methods=['GET'])
def api_update_game(game_id):
    game = Game.query.get(game_id)

    return jsonify(game.serialize())

@cross_origin()
@app.errorhandler(400)
def not_found(_):
    return make_response(jsonify({'error': 'Bad request'}), 400)

@cross_origin()
@app.errorhandler(404)
def not_found(_):
    return make_response(jsonify({'error': 'Not found'}), 404)
