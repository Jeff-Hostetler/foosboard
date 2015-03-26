from flask import request, make_response, jsonify
from flask_cors import cross_origin
from numpy import average
from foosboard.models import Game, PredictionModelEntity
from foosboard.predictions import DataParser, PredictionModel
from foosboard import app
from sklearn.ensemble import RandomForestClassifier


@cross_origin()
@app.route('/prediction', methods=['GET'])
def api_show_game(game_id):
    game = Game.query.get(game_id)

    prediction_model = PredictionModelEntity.load()

    prediction = prediction_model.predict(game)

    return prediction


@cross_origin()
@app.route('/model', methods=['POST'])
def api_train_model():
    parser = DataParser()

    model = RandomForestClassifier(n_estimators=10)
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

