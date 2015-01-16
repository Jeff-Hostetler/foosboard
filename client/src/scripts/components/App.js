'use strict';

var React = require('react/addons');
var Router = require('react-router');
var Header = require('./Header');
var RouteHandler = Router.RouteHandler;

// Export React so the devtools can find it
(window !== window.top ? window.top : window).React = React;

// CSS
require('../../styles/main.css');

var App = React.createClass({
  render: function () {
    return (
      <div className="container">
        <Header />

        <RouteHandler />
      </div>
    );
  }
});

module.exports = App;
