'use strict';

var React = require('react/addons'),
  GameService = require('../services/GameService');

var GameList = React.createClass({
  getInitialState: function () {
    return {games: []};
  },

  componentDidMount: function () {
    var _this = this;

    GameService.getList()
      .then(function (response) {
        _this.setState({games: response.games});
      });
  },

  render: function () {
    function renderAllGames(gameData) {
      return gameData.map(function (game, index) {
        return (
          <tr key={index}>
            <td>{game.team_1.defense}</td>
            <td>{game.team_1.offense}</td>
            <td>{game.team_1_score}</td>
            <td>{game.team_2_score}</td>
            <td>{game.team_2.offense}</td>
            <td>{game.team_2.defense}</td>
          </tr>
        );
      });
    }

    return (
      <table className="table table-hover table-bordered">
        <thead>
          <tr>
            <th>Team 1 Defense</th>
            <th>Team 1 Offense</th>
            <th>Team 1 Score</th>
            <th>Team 2 Score</th>
            <th>Team 2 Offense</th>
            <th>Team 2 Defense</th>
          </tr>
        </thead>
        <tbody>
          {renderAllGames(this.state.games)}
        </tbody>
      </table>
    );
  }
});

module.exports = GameList;
