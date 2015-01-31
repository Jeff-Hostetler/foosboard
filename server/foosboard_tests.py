import unittest
import json
from foosboard import app
from flask_sqlalchemy import SQLAlchemy
from config import TestConfig


class FoosboardTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.client = app.test_client()
        self.db = SQLAlchemy(self.app)

    def test_empty_db(self):
        rv = self.client.get('/api/games',
                             headers={'Accept': 'application/json'})

        expected_response = {'games': []}

        self.assertEqual(json.loads(rv.data), expected_response)

if __name__ == '__main__':
    unittest.main()
