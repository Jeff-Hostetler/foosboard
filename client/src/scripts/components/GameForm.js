'use strict';

var React = require('react/addons');

var GameForm = React.createClass({
  render: function () {
    function createPlayerInput(labelText, selectName, allPlayerInitials) {
      var playerOptions = allPlayerInitials.map(function (player) {
        return (
          <option>{player.name}</option>
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

    var allPlayers = [
        {id: 1, name: "EC"},
        {id: 2, name: "TG"},
        {id: 3, name: "NW"},
        {id: 4, name: "BC"},
        {id: 5, name: "BB"},
        {id: 6, name: "EA"}
      ],
      team1Defense = createPlayerInput("Team 1 Defense", "team1defense", allPlayers),
      team1Offense = createPlayerInput("Team 1 Offense", "team1offense", allPlayers),
      team2Offense = createPlayerInput("Team 2 Offense", "team2defense", allPlayers),
      team2Defense = createPlayerInput("Team 2 Defense", "team2defense", allPlayers);

    return (
      <form className="form-horizontal" method="get" action="/#game">
        {team1Defense}
        {team1Offense}
        {team2Offense}
        {team2Defense}
        <div className="form-group">
          <div className="col-sm-offset-2 col-sm-10">
            <input className="btn btn-default" type="submit" value="Start game" />
          </div>
        </div>
      </form>
    );
  }
});

module.exports = GameForm;
