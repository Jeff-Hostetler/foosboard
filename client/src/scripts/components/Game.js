'use strict';

var React = require('react/addons'),
  GameService = require('../services/GameService'),
  Router = require('react-router'),
  State = Router.State,
  Navigation = Router.Navigation;

var ScoreSelect = React.createClass({
  getInitialState: function () {
    return {
      finalScore: 0
    };
  },

  updateScore: function (e) {
    var newScore = e.target.value;
    this.setState({finalScore: newScore});
  },

  render: function () {
    return (
      <div className="form-group">
        <label> {this.props.title} </label>
        <select className="form-control" name={this.props.name} value={this.state.finalScore} onChange={this.updateScore}>
          <option>0</option>
          <option>1</option>
          <option>2</option>
          <option>3</option>
          <option>4</option>
          <option>5</option>
        </select>
      </div>
    );
  }
});

var Game = React.createClass({
  mixins: [Navigation, State],

  getInitialState: function () {
    return {
      team_1_score: 0,
      team_2_score: 0,
      team_1: {
        offense: "",
        defense: ""
      },
      team_2: {
        offense: "",
        defense: ""
      }
    };
  },

  getGameId: function () {
    return this.getParams().gameId;
  },

  componentDidMount: function () {
    var _this = this;

    GameService.get(this.getGameId())
      .then(function (response) {
        var gameState = {
          team_1_score: response.team_1_score,
          team_2_score: response.team_2_score,
          team_1: {
            offense: response.team_1.offense,
            defense: response.team_1.defense
          },
          team_2: {
            offense: response.team_2.offense,
            defense: response.team_2.defense
          }
        };

        _this.setState(gameState);
      });
  },

  handleSubmit: function (e) {
    e.preventDefault();

    var _this = this,
      gameScore = {
        team1score: this.refs.team1score.state.finalScore,
        team2score: this.refs.team2score.state.finalScore
      };

    console.log(gameScore);

    GameService.update(this.getGameId(), gameScore)
      .then(function () {
        _this.transitionTo('/');
      });
  },

  updateScore: function () {

  },

  render: function () {
    return (
      <div>
        <dl>
          <dt>Team 1 Defense</dt>
          <dd>{this.state.team_1.defense}</dd>

          <dt>Team 1 Offense</dt>
          <dd>{this.state.team_1.offense}</dd>

          <dt>Team 2 Offense</dt>
          <dd>{this.state.team_2.offense}</dd>

          <dt>Team 2 Defense</dt>
          <dd>{this.state.team_2.defense}</dd>
        </dl>

        <form ref="scoreForm" onSubmit={this.handleSubmit}>
          <ScoreSelect
            title='Team 1 Score'
            name='team1score'
            ref='team1score' />

          <ScoreSelect
            title='Team 2 Score'
            name='team2score'
            ref='team2score' />

          <input className="btn btn-default" type="submit" value="Save" />
        </form>
      </div>
    );
  }
});

module.exports = Game;
