'use strict';

var React = require('react/addons');
var Header = require('./Header');
var GameForm = require('./GameForm');
var GameList = require('./GameList');

// Export React so the devtools can find it
(window !== window.top ? window.top : window).React = React;

// CSS
require('../../styles/main.css');

var FoosboardRoot = React.createClass({
  render: function () {
    return (
      <div className="container">
        <Header />
        <GameForm />
        <GameList />
      </div>
    );
  }
});

module.exports = FoosboardRoot;
