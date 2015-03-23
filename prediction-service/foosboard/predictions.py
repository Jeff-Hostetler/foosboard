from sklearn import cross_validation
from numpy import zeros, array
from foosboard.models import Game, Player


# Use
# sklearn.neighbors.KNeighborsClassifier(15, weights='distance')
# sklearn.neighbors.KNeighborsClassifier(15, weights='uniform')
# sklearn.svm.SVC(gamma=0.001, C=100.)
# for model

'''
Example:
from foosboard.predictions import DataParser, PredictionModel
from foosboard.models import Game
from sklearn import neighbors

dp = DataParser()
clf = neighbors.KNeighborsClassifier(15, weights='distance')
pm = PredictionModel(dp, clf)
pm.cross_validate()

pm.train_model()

games = Game.query.all()

pm.predict(games[0])
'''

class PredictionModel():

    def __init__(self, parser, model):
        self.parser = parser
        self.model = model

    def train_model(self):
        dataset = self.parser.parse_data()

        self.model.fit(array(dataset['inputs']), array(dataset['results']))


    def predict(self, game):
        input = array(self.parser.parse_input(game))

        result = self.model.predict(input)[0]
        return self.parser.interpret_result(result)


    def cross_validate(self):
        dataset = self.parser.parse_data()

        kfold = cross_validation.KFold(len(dataset['inputs']), n_folds=3)

        return cross_validation.cross_val_score(
            self.model,
            dataset['inputs'],
            dataset['results'],
            cv=kfold,
            n_jobs=-1
        )


class DataParser():

    def __init__(self):
        players = Player.query.all()

        count = 0
        self.player_id_map = {}

        for player in players:
            self.player_id_map[player.id] = count
            count += 1

        self.player_length = count + 1


    def parse_data(self):
        games = Game.query.all()

        inputs = []
        results = []

        for game in games:
            inputs.append(self.parse_input(game))
            results.append(self.parse_result(game))
            inputs.append(self.parse_symmetric_input(game))
            results.append(self.parse_symmetric_result(game))

        return {'inputs': inputs, 'results': results}


    def parse_input(self, game):
        players = zeros(2 * self.player_length)

        players[self.get_index(game.team1defense_id, 1)] = 1
        players[self.get_index(game.team1offense_id, 1)] = 1

        players[self.get_index(game.team2defense_id, 2)] = 1
        players[self.get_index(game.team2offense_id, 2)] = 1

        return players


    def parse_symmetric_input(self, game):
        players = zeros(2 * self.player_length)

        players[self.get_index(game.team1defense_id, 2)] = 1
        players[self.get_index(game.team1offense_id, 2)] = 1

        players[self.get_index(game.team2defense_id, 1)] = 1
        players[self.get_index(game.team2offense_id, 1)] = 1

        return players


    def parse_result(self, game):
        if game.team1score > game.team2score:
            return 1
        else:
            return -1


    def parse_symmetric_result(self, game):
        if game.team1score > game.team2score:
            return -1
        else:
            return 1


    def interpret_result(self, result):
        if result == 1:
            return "Team 1"
        else:
            return "Team 2"


    def get_index(self, id, team):
        if team == 1:
            return self.player_id_map[id]
        else:
            return self.player_id_map[id] + self.player_length
