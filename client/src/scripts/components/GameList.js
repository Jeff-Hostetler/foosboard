'use strict';

var React = require('react/addons');

var GameList = React.createClass({
  render: function () {
    function renderAllGames(gameDate) {
      return gameData.map(function (game) {
        return (
          <tr>
            <td>{game.created_at}</td>
            <td>{game.team1defense}</td>
            <td>{game.team1offense}</td>
            <td>{game.team1score}</td>
            <td>{game.team2score}</td>
            <td>{game.team2offense}</td>
            <td>{game.team2defense}</td>
          </tr>
        );
      });
    }
    var gameData = [
      {id:1, created_at: (new Date()).toString(), team1offense: "EC", team1defense: "BB", team2offense: "NB", team2defense: "TG", team1score: 5, team2score: 1},
      {id:2, created_at: (new Date()).toString(), team1offense: "BB", team1defense: "EC", team2offense: "TG", team2defense: "NB", team1score: 5, team2score: 3}
    ],
      allGames = renderAllGames(gameData);

    return (
      <table className="table table-hover table-bordered">
        <thead>
          <tr>
            <th>Date</th>
            <th>Team 1 Defense</th>
            <th>Team 1 Offense</th>
            <th>Team 1 Score</th>
            <th>Team 2 Score</th>
            <th>Team 2 Offense</th>
            <th>Team 2 Defense</th>
          </tr>
        </thead>
        <tbody>
          {allGames}
        </tbody>
      </table>
    );
  }
});

module.exports = GameList;
