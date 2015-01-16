'use strict';

var React = require('react/addons');
var ReactTransitionGroup = React.addons.TransitionGroup;

// Export React so the devtools can find it
(window !== window.top ? window.top : window).React = React;

// CSS
require('../../styles/main.css');

var imageURL = require('../../images/yeoman.png');

var FoosboardRoot = React.createClass({
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

module.exports = FoosboardRoot;
