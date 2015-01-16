'use strict';

var React = require('react/addons');

// CSS
require('../../styles/main.css');

var GameForm = React.createClass({
  render: function () {
    var allPlayers = ["EC", "TG", "NW", "BC", "BB", "EA"],
      playerOptions = allPlayers.map(function (playerInitials) {
        return (
          <option>{playerInitials}</option>
        );
      });


    return (
      <form className="form-horizontal" method="get" action="/games/new">
        <div className="form-group">
          <label className="col-sm-2 control-label">Team 1 Defense</label>
          <div>
            <div className="col-sm-2">
              <select className="form-control" name="team1defense">
                {playerOptions}
              </select>
            </div>
          </div>
        </div>

        <div className="form-group">
          <label className="col-sm-2 control-label">Team 1 Offense</label>
          <div className="col-sm-2">
            <select className="form-control" name="team1offense">
              {playerOptions}
            </select>
          </div>
        </div>

        <div className="form-group">
          <label className="col-sm-2 control-label">Team 2 Offense</label>
          <div className="col-sm-2">
            <select className="form-control" name="team2offense">
              {playerOptions}
            </select>
          </div>
        </div>

        <div className="form-group">
          <label className="col-sm-2 control-label">Team 2 Defense</label>
          <div className="col-sm-2">
            <select className="form-control" name="team2defense">
             {playerOptions}
            </select>
          </div>
        </div>

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
