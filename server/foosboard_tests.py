import unittest
import json
from foosboard import app, db
from foosboard.models import Game


class FoosboardTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.client = app.test_client()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        db.drop_all()

    def test_endpoint_returns_no_games_by_default(self):
        rv = self.client.get('/api/games',
                             headers={'Accept': 'application/json'})

        expected_response = {'games': []}

        self.assertEqual(json.loads(rv.data), expected_response)

    def test_endpoint_returns_all_persisted_games(self):
        game = Game("EC", "BB", "TG", "NB")
        game.team1score = 3
        game.team2score = 5

        db.session.add(game)
        db.session.commit()

        rv = self.client.get('/api/games',
                             headers={'Accept': 'application/json'})

        expected_response = {'games': [{
            'id': 1,
            'team_1_score': 3,
            'team_2_score': 5,
            'team_1': {'offense': 'BB', 'defense': 'EC'},
            'team_2': {'offense': 'TG', 'defense': 'NB'}
        }]}

        self.assertEqual(json.loads(rv.data), expected_response)

if __name__ == '__main__':
    unittest.main()
