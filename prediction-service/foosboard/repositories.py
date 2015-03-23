from foosboard import db

class GameRepository():
    def win_percentage_for_player_id(self, player_id):
        total_games = db.engine.execute(
            "select count(*) as games_played from games where team1defense_id = %s or team1offense_id = %s or team2defense_id = %s or team2offense_id = %s;",
            player_id,
            player_id,
            player_id,
            player_id
        ).fetchone()[0]

        wins = db.engine.execute(
            "select count(*) as games_won from games where ((team1defense_id = %s or team1offense_id = %s) and team1score = 5) or ((team2defense_id = %s or team2offense_id = %s) and team2score = 5);",
            player_id,
            player_id,
            player_id,
            player_id
        ).fetchone()[0]

        if total_games == 0:
            return 0
        else:
            return wins * 100 / total_games

    def goals_scored_for_player_id(self, player_id):
        goals_scored = db.engine.execute(
            "select (select coalesce(sum(team1score), 0) from games where team1offense_id = %s) + (select coalesce(sum(team2score), 0) from games where team2offense_id = %s)",
            player_id,
            player_id
        ).fetchone()[0]

        return goals_scored

    def goals_against_for_player_id(self, player_id):
        goals_against = db.engine.execute(
            "select (select coalesce(sum(team2score), 0) from games where team1defense_id = %s) + (select coalesce(sum(team1score), 0) from games where team2defense_id = %s)",
            player_id,
            player_id
        ).fetchone()[0]

        return goals_against