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

    def test_creating_a_game(self):
        payload = {
            'team1defense': 'EC',
            'team1offense': 'TG',
            'team2offense': 'BB',
            'team2defense': 'NB'
        }

        rv = self.client.post('/api/games',
                              headers={'Accept': 'application/json',
                                       'Content-Type': 'application/json'},
                              data=json.dumps(payload))

        expected_response = {
            'id': 1,
            'team_1_score': None,
            'team_2_score': None,
            'team_1': {'offense': 'TG', 'defense': 'EC'},
            'team_2': {'offense': 'BB', 'defense': 'NB'}
        }

        self.assertEqual(rv.status, '201 CREATED')
        self.assertEqual(json.loads(rv.data), expected_response)

    def test_retrieving_a_game(self):
        game = Game("EC", "BB", "TG", "NB")
        game.team1score = 3
        game.team2score = 5

        db.session.add(game)
        db.session.commit()

        rv = self.client.get('/api/games/1',
                             headers={'Accept': 'application/json'})

        expected_response = {
            'id': 1,
            'team_1_score': 3,
            'team_2_score': 5,
            'team_1': {'offense': 'BB', 'defense': 'EC'},
            'team_2': {'offense': 'TG', 'defense': 'NB'}
        }

        self.assertEqual(json.loads(rv.data), expected_response)

    def test_updating_a_game(self):
        game = Game("EC", "BB", "TG", "NB")

        db.session.add(game)
        db.session.commit()
        payload = {'team1score': 5, 'team2score': 0}

        rv = self.client.patch('/api/games/1',
                               headers={'Accept': 'application/json',
                                        'Content-Type': 'application/json'},
                               data=json.dumps(payload))

        expected_response = {
            'id': 1,
            'team_1_score': 5,
            'team_2_score': 0,
            'team_1': {'offense': 'BB', 'defense': 'EC'},
            'team_2': {'offense': 'TG', 'defense': 'NB'}
        }

        self.assertEqual(json.loads(rv.data), expected_response)


if __name__ == '__main__':
    unittest.main()
