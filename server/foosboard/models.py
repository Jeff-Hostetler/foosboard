from datetime import datetime

from foosboard import db


class Game(db.Model):
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True)

    created_at = db.Column(db.DateTime())
    team1defense = db.Column(db.String())
    team1offense = db.Column(db.String())
    team1score = db.Column(db.Integer())
    team2offense = db.Column(db.String())
    team2defense = db.Column(db.String())
    team2score = db.Column(db.Integer())

    def __init__(self,
                 team1defense,
                 team1offense,
                 team2offense,
                 team2defense):
        self.created_at = datetime.utcnow()
        self.team2defense = team2defense
        self.team2offense = team2offense
        self.team1defense = team1defense
        self.team1offense = team1offense

    def has_invalid_score(self):
        return self.team1score == 5 or self.team2score == 5

    def serialize(self):
        return {
            "id": self.id,
            "team_1_score": self.team1score,
            "team_2_score": self.team2score,
            "team_1": {
                "offense": self.team1offense,
                "defense": self.team1defense
            },
            "team_2": {
                "offense": self.team2offense,
                "defense": self.team2defense
            }
        }
