'use strict';

var React = require('react/addons');

// CSS
require('../../styles/main.css');

var GameForm = React.createClass({
  render: function () {
    function createPlayerInput(labelText, selectName, allPlayerInitials) {
      var playerOptions = allPlayerInitials.map(function (initials) {
        return (
          <option>{initials}</option>
        );
      });

      return (
        <div className="form-group">
          <label className="col-sm-2 control-label">{labelText}</label>
          <div>
            <div className="col-sm-2">
              <select className="form-control" name={selectName}>
                {playerOptions}
              </select>
            </div>
          </div>
        </div>
      );
    }

    var allPlayers = ["EC", "TG", "NW", "BC", "BB", "EA"],
      team1Defense = createPlayerInput("Team 1 Defense", "team1defense", allPlayers),
      team1Offense = createPlayerInput("Team 1 Offense", "team1offense", allPlayers),
      team2Offense = createPlayerInput("Team 2 Offense", "team2defense", allPlayers),
      team2Defense = createPlayerInput("Team 2 Defense", "team2defense", allPlayers);

    return (
      <form className="form-horizontal" method="get" action="/games/new">
        {team1Defense}
        {team1Offense}
        {team2Offense}
        {team2Defense}
      </form>
    );
  }
});

module.exports = GameForm;
