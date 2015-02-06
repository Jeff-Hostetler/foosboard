'use strict';

var React = require('react/addons');
var Route = require('react-router');
var Link = Route.Link;

// CSS
require('../../styles/main.css');

var Header = React.createClass({
  render: function () {
    return (
      <div className="page-header">
        <Link to="/">
          <h1>
            Foosboard&nbsp;
            <small>I totally meant to do that.&trade;</small>
          </h1>
        </Link>
        <Link to="status">
          Status
        </Link>
      </div>
    );
  }
});

module.exports = Header;
