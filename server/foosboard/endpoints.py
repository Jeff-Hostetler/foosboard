from flask import request, make_response, jsonify
from flask_cors import cross_origin
from numpy import average
from foosboard.models import Game, Player, PredictionModelEntity
from foosboard.predictions import DataParser, PredictionModel
from foosboard.repositories import GameRepository
from foosboard import app, db
from sklearn import neighbors


@cross_origin()
@app.route('/api/games', methods=['GET'])
def api_index():
    games = Game.query.all()
    return jsonify({'games': [game.serialize() for game in games]})


@cross_origin()
@app.route('/api/players', methods=['GET'])
def api_player_index():
    players = Player.query.all()
    return jsonify({'players': [player.serialize() for player in players]})


@cross_origin()
@app.route('/api/games/<int:game_id>', methods=['GET'])
def api_show_game(game_id):
    game = Game.query.get(game_id)

    response = game.serialize()

    prediction_model = PredictionModelEntity.load()

    response['prediction'] = prediction_model.predict(game)

    return jsonify(response)


@cross_origin()
@app.route('/api/games', methods=['POST'])
def api_create_game():
    game = Game(request.json["team1defense_id"],
                request.json["team1offense_id"],
                request.json["team2offense_id"],
                request.json["team2defense_id"])

    db.session.add(game)
    db.session.commit()

    return make_response(jsonify(game.serialize()), 201)


@cross_origin()
@app.route('/api/games/<int:game_id>', methods=['PATCH'])
def api_update_game(game_id):
    game = Game.query.get(game_id)

    game.team1score = request.json["team1score"]
    game.team2score = request.json["team2score"]
    game.inProgress = False

    db.session.add(game)
    db.session.commit()

    return jsonify(game.serialize())

@cross_origin()
@app.route('/api/status', methods=['GET'])
def api_show_status():
    if(Game.query.filter_by(inProgress=True).first()):
        return jsonify({'status': 'In Progress'})
    else:
        return jsonify({'status': 'Open'})

@cross_origin()
@app.route('/api/stats', methods=['GET'])
def api_show_stats():
    players = Player.query.all()
    return jsonify({
        'stats':
            [
                {
                    'nickname': player.nickname,
                    'win_percentage': GameRepository().win_percentage_for_player_id(player.id),
                    'goals_scored': GameRepository().goals_scored_for_player_id(player.id),
                    'goals_against': GameRepository().goals_against_for_player_id(player.id)
                }
                for player in players
            ]
    })


@cross_origin()
@app.route('/api/model', methods=['POST'])
def api_train_model():
    parser = DataParser()
    model = neighbors.KNeighborsClassifier(15, weights='distance')
    prediction_model = PredictionModel(parser, model)
    prediction_model.train_model()

    PredictionModelEntity.store(prediction_model)

    return jsonify({'accuracy': average(prediction_model.cross_validate())})


@cross_origin()
@app.errorhandler(400)
def bad_request(_):
    return make_response(jsonify({'error': 'Bad request'}), 400)


@cross_origin()
@app.errorhandler(404)
def not_found(_):
    return make_response(jsonify({'error': 'Not found'}), 404)

