CREATE DATABASE foosboard;

CREATE TABLE games (
    id BIGSERIAL PRIMARY KEY,
    team1defense varchar,
    team1offense varchar,
    team2offense varchar,
    team2defense varchar,
    team1score integer,
    team2score integer
);

ALTER TABLE games ADD COLUMN created_at timestamp without time zone;
