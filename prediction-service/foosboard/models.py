from datetime import datetime
import pickle
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

class Player(db.Model):
    __tablename__ = 'players'

    id = db.Column(db.Integer, primary_key=True)

    created_at = db.Column(db.DateTime())
    nickname = db.Column(db.String())

    def __init__(self,
                 nickname):
        self.created_at = datetime.utcnow()
        self.nickname = nickname

class PredictionModelEntity(db.Model):
    __tablename__ = 'prediction_model'

    id = db.Column(db.Integer, primary_key=True)

    model_data = db.Column(db.String())

    def __init__(self, model_data):
        self.model_data = model_data

    @classmethod
    def store(cls, model):
        entity = cls(pickle.dumps(model))

        db.session.add(entity)
        db.session.commit()


    @classmethod
    def load(cls):
        entity = cls.query.order_by('-id').first()
        return pickle.loads(entity.model_data)

