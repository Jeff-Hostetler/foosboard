var React = require('react'),
  GameService = require('../services/GameService');

var interval;

var Status = React.createClass({
  getInitialState: function () {
    return {status: 'open'};
  },

  componentDidMount: function () {
    var _this = this;

    interval = setInterval(function () {
      GameService.getStatus()
        .then(function (response) {
          _this.setState({status: response.status});
        });
    }, 1000);
  },

  componentWillUnmount: function () {
    clearInterval(interval);
  },

  render: function () {
    return (
      <h1>Game state: {this.state.status}</h1>
    );
  }
});

module.exports = Status;
