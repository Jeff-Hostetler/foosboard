'use strict';

var React = require('react/addons');
var GameForm = require('./GameForm');
var GameList = require('./GameList');

var Dashboard = React.createClass({
  render: function () {
    return (
      <div>
        <GameForm />
        <GameList />
      </div>
    );
  }
});

module.exports = Dashboard;
