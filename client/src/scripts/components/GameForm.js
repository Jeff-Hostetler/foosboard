'use strict';

var React = require('react/addons');
var Navigation = require('react-router').Navigation;
var GameService = require('../services/GameService');

var PlayerSelect = React.createClass({
  getInitialState: function () {
    return {
      value: "EC"
    };
  },

  onChange: function (event) {
    this.setState({value: event.target.value});
  },

  render: function () {
    var playerOptions = this.props.allPlayers.map(function (player, index) {
      return (
        <option key={index} value={player.name}>{player.name}</option>
      );
    });

    return (
      <div className="form-group">
        <label className="col-sm-2 control-label">{this.props.label}</label>
        <div>
          <div className="col-sm-2">
            <select className="form-control" onChange={this.onChange} value={this.state.value} name={this.props.name}>
                {playerOptions}
            </select>
          </div>
        </div>
      </div>
    );
  }
});

var GameForm = React.createClass({
  mixins: [Navigation],

  handleSubmit: function (e) {
    e.preventDefault();

    var newGame = {
      team1defense: this.refs.team1defense.state.value,
      team1offense: this.refs.team1offense.state.value,
      team2offense: this.refs.team2offense.state.value,
      team2defense: this.refs.team2defense.state.value
    },
      _this = this;

    GameService.create(newGame)
      .then(function (response) {
        // mixed in from Navigation
        _this.transitionTo('/games/' + response.id);
      });
  },

  getDefaultProps: function () {
    return {
      allPlayers: [
        {id: 1, name: "EC"},
        {id: 2, name: "TG"},
        {id: 3, name: "NW"},
        {id: 4, name: "BC"},
        {id: 5, name: "BB"},
        {id: 6, name: "EA"}
      ]
    };
  },

  render: function () {
    return (
      <form ref="gameForm" className="form-horizontal" onSubmit={this.handleSubmit}>
        <PlayerSelect
          allPlayers={this.props.allPlayers}
          ref="team1defense"
          name='team1defense'
          label='Team 1 Defense' />

        <PlayerSelect
          allPlayers={this.props.allPlayers}
          ref="team1offense"
          name='team1offense'
          label='Team 1 Offense' />

        <PlayerSelect
          allPlayers={this.props.allPlayers}
          ref="team2offense"
          name='team1defense'
          label='Team 2 Offense' />

        <PlayerSelect
          allPlayers={this.props.allPlayers}
          ref="team2defense"
          name='team1defense'
          label='Team 2 Defense' />

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
