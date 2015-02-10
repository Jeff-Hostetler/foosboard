from datetime import datetime

from foosboard import db


class Game(db.Model):
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True)

    created_at = db.Column(db.DateTime())
    team1defense_id = db.Column(db.Integer(), db.ForeignKey('players.id'))
    team1offense_id = db.Column(db.Integer(), db.ForeignKey('players.id'))
    team1score = db.Column(db.Integer())
    team2offense_id = db.Column(db.Integer(), db.ForeignKey('players.id'))
    team2defense_id = db.Column(db.Integer(), db.ForeignKey('players.id'))
    team2score = db.Column(db.Integer())
    inProgress = db.Column(db.Boolean())

    def __init__(self,
                 team1defense_id,
                 team1offense_id,
                 team2offense_id,
                 team2defense_id):
        self.created_at = datetime.utcnow()
        self.team2defense_id = team2defense_id
        self.team2offense_id = team2offense_id
        self.team1defense_id = team1defense_id
        self.team1offense_id = team1offense_id
        self.inProgress = True

    def has_invalid_score(self):
        return self.team1score == 5 or self.team2score == 5

    def serialize(self):
        return {
            "id": self.id,
            "team_1_score": self.team1score,
            "team_2_score": self.team2score,
            "team_1": {
                "offense": Player.query.get(self.team1offense_id).initials,
                "defense": Player.query.get(self.team1defense_id).initials
            },
            "team_2": {
                "offense": Player.query.get(self.team2offense_id).initials,
                "defense": Player.query.get(self.team2defense_id).initials
            },
            "in_progress": self.inProgress
        }


class Player(db.Model):
    __tablename__ = 'players'

    id = db.Column(db.Integer, primary_key=True)

    created_at = db.Column(db.DateTime())
    initials = db.Column(db.String())

    def __init__(self,
                 initials):
        self.created_at = datetime.utcnow()
        self.initials = initials

    def serialize(self):
        return {
            "id": self.id,
            "initials": self.initials
        }
