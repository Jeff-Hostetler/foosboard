'use strict';

var React = require('react/addons');
var GameForm = require('./GameForm');
var GameList = require('./GameList');

var Dashboard = React.createClass({
  render: function () {
    return (
      <div>
        <GameForm url='http://localhost:5000/api/games' />
        <GameList url='http://localhost:5000/api/games' />
      </div>
    );
  }
});

module.exports = Dashboard;
