'use strict';

var React = require('react/addons');
var Navigation = require('react-router').Navigation;
var GameService = require('../services/GameService');
var PlayerService = require('../services/PlayerService');

var PlayerSelect = React.createClass({
  onChange: function (event) {
    this.setState({value: event.target.value});
  },

  render: function () {
    var playerOptions = this.props.allPlayers.map(function (player, index) {
      return (
        <option key={index} value={player.id}>{player.nickname}</option>
      );
    });

    return (
      <div className="form-group">
        <label className="col-sm-2 control-label">{this.props.label}</label>
        <div>
          <div className="col-sm-2">
            <select className="form-control" onChange={this.onChange} name={this.props.name}>
                <option disabled="disabled"></option>
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
      team_1: {
        defense: {id: this.refs.team_1_defense.state.value},
        offense: {id: this.refs.team_1_offense.state.value}
      },
      team_2: {
        offense: {id: this.refs.team_2_offense.state.value},
        defense: {id: this.refs.team_2_defense.state.value}
      }
    },
      _this = this;

    GameService.create(newGame)
      .then(function (response) {
        // mixed in from Navigation
        _this.transitionTo('/games/' + response.id);
      });
  },

  getInitialState: function () {
    return {
      players: []
    };
  },

  componentDidMount: function () {
    var _this = this;

    PlayerService.getList().then(function (result) {
      _this.setState({players: result});
    });
  },

  render: function () {
    return (
      <form ref="gameForm" className="form-horizontal" onSubmit={this.handleSubmit}>
        <PlayerSelect
          allPlayers={this.state.players}
          ref="team_1_defense"
          name='team_1_defense'
          label='Team 1 Defense' />

        <PlayerSelect
          allPlayers={this.state.players}
          ref="team_1_offense"
          name='team_1_offense'
          label='Team 1 Offense' />

        <PlayerSelect
          allPlayers={this.state.players}
          ref="team_2_offense"
          name='team_1_defense'
          label='Team 2 Offense' />

        <PlayerSelect
          allPlayers={this.state.players}
          ref="team_2_defense"
          name='team_1_defense'
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
