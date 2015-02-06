var React = require('react'),
  GameService = require('../services/GameService');

var Status = React.createClass({
  getInitialState: function () {
    return {status: 'In Progress'};
  },

  componentDidMount: function () {
    var _this = this;

    GameService.getStatus()
      .then(function (response) {
        _this.setState({status: response.status});
      });
  },

  render: function () {
    return (
      <h1>Game state: {this.state.status}</h1>
    );
  }
});

module.exports = Status;