'use strict';

var React = require('react/addons');
var Route = require('react-router');
var Link = Route.Link;

// CSS
require('../../styles/main.css');

var Header = React.createClass({
  render: function () {
    return (
      <nav className="navbar navbar-default">
        <div className="container-fluid">
          <div className="navbar-header">
            <Link className="navbar-brand" to="/">
              Foosboard&nbsp;
              <small>I totally meant to do that.&trade;</small>
            </Link>

            <ul className="nav navbar-nav">
              <li>
                <Link to="status">
                  Status
                </Link>
              </li>

              <li>
                <Link to="stats">
                  Stats
                </Link>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    );
  }
});

module.exports = Header;
