CREATE TABLE games (
    id BIGSERIAL PRIMARY KEY,
    team1player1 varchar,
    team1player2 varchar,
    team2player1 varchar,
    team2player2 varchar,
    team1score integer,
    team2score integer
);