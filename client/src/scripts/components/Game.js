'use strict';

var React = require('react/addons');

var Game = React.createClass({
  render: function () {
    return (
      <form method="POST" action="/games">
        <input type="hidden" name="team1defense" value="{{team1defense}}" />
        <input type="hidden" name="team1offense" value="{{team1offense}}" />
        <input type="hidden" name="team2defense" value="{{team2defense}}" />
        <input type="hidden" name="team2offense" value="{{team2offense}}" />

        <div className="form-group">

          <label> Team 1 Score </label>
          <select className="form-control" name="team1score">
            <option>0</option>
            <option>1</option>
            <option>2</option>
            <option>3</option>
            <option>4</option>
            <option>5</option>
          </select>
        </div>
        <div className="form-group">

          <label> Team 2 Score </label>
          <select className="form-control" name="team2score">
            <option>0</option>
            <option>1</option>
            <option>2</option>
            <option>3</option>
            <option>4</option>
            <option>5</option>
          </select>
        </div>

        <input className="btn btn-default" type="submit" value="Save" />
      </form>
    );
  }
});

module.exports = Game;
