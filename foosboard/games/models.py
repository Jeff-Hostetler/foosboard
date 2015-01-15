from foosboard import db


class Game(db.Model):
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True)

    team1defense = db.Column(db.String())
    team1offense = db.Column(db.String())
    team1score = db.Column(db.Integer())
    team2offense = db.Column(db.String())
    team2defense = db.Column(db.String())
    team2score = db.Column(db.Integer())

    def __init__(self, team1defense, team1offense, team1score, team2offense, team2defense, team2score):
        self.team2score = team2score
        self.team2defense = team2defense
        self.team2offense = team2offense
        self.team1score = team1score
        self.team1defense = team1defense
        self.team1offense = team1offense