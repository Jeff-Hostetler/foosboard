from sklearn import svm
from numpy import zeros, array
from foosboard.models import Game, Player


class GamePredictionModel():

    def __init__(self):
        self.model = svm.SVC(gamma=0.001, C=100.)
        players = Player.query.all()

        count = 0
        self.player_id_map = {}

        for player in players:
            self.player_id_map[player.id] = count
            count += 1

        self.player_length = count + 1

    def train_model(self):
        games = Game.query.all()

        inputs = []
        results = []

        for game in games:
            inputs.append(self.parse_input(game))
            results.append(self.parse_result(game))

        self.model.fit(array(inputs), array(results))


    def predict(self, game):
        input = array(self.parse_input(game))

        result = self.model.predict(input)[0]
        return self.interpret_result(result)


    def parse_input(self, game):
        players = zeros(2 * self.player_length)

        players[self.get_index(game.team1defense_id, 1)] = -1
        players[self.get_index(game.team1offense_id, 1)] = 1

        players[self.get_index(game.team2defense_id, 2)] = -1
        players[self.get_index(game.team2offense_id, 2)] = 1

        return players


    def parse_result(self, game):
        if game.team1score > game.team2score:
            return 1
        else:
            return -1


    def interpret_result(self, result):
        if result == 1:
            return "Team 1 will win"
        else:
            return "Team 2 will win"


    def get_index(self, id, team):
        if team == 1:
            return self.player_id_map[id]
        else:
            return self.player_id_map[id] + self.player_length