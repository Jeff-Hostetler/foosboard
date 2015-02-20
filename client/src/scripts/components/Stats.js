var React = require('react'),
  GameService = require('../services/GameService');

var Stats = React.createClass({
  getInitialState: function () {
    return {stats: []};
  },

  componentWillMount: function () {
    var _this = this;

    GameService.getStats().then(function (response) {
      _this.setState({stats: response.stats})
    });
  },

  render: function () {
    var stats = this.state.stats.map(function (stat) {
      return (
        <tr>
          <td>{stat.nickname}</td>
          <td>{stat.goals_scored}</td>
          <td>{stat.goals_against}</td>
          <td>{stat.win_percentage}</td>
        </tr>
      );
    });

    return (
      <table className="table table-hover table-bordered">
        <thead>
          <tr>
            <th>Nickname</th>
            <th>Goals scored</th>
            <th>Goals against</th>
            <th>Win percentage</th>
          </tr>
        </thead>
        <tbody>
        {stats}
        </tbody>
      </table>
    );
  }
});

module.exports = Stats;