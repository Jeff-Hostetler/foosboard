var FoosboardRoot = require('./FoosboardRoot');
var React = require('react');
var Router = require('react-router');
var Route = Router.Route;

var content = document.getElementById('app');

var Routes = (
  <Route handler={FoosboardRoot}>
    <Route name="/" handler={FoosboardRoot}/>
  </Route>
);

Router.run(Routes, function (Handler) {
  React.render(<Handler/>, content);
});
