'use strict';

var React = require('react/addons');

// CSS
require('../../styles/main.css');

var Header = React.createClass({
  render: function () {
    return (
      <div className="page-header">
        <a href="/">
          <h1>
            Foosboard&nbsp;
            <small>I totally meant to do that.&trade;</small>
          </h1>
        </a>
      </div>
    );
  }
});

module.exports = Header;
