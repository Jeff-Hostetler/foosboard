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
      team1defense_id: this.refs.team1defense.state.value,
      team1offense_id: this.refs.team1offense.state.value,
      team2offense_id: this.refs.team2offense.state.value,
      team2defense_id: this.refs.team2defense.state.value
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
          ref="team1defense"
          name='team1defense'
          label='Team 1 Defense' />

        <PlayerSelect
          allPlayers={this.state.players}
          ref="team1offense"
          name='team1offense'
          label='Team 1 Offense' />

        <PlayerSelect
          allPlayers={this.state.players}
          ref="team2offense"
          name='team1defense'
          label='Team 2 Offense' />

        <PlayerSelect
          allPlayers={this.state.players}
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
