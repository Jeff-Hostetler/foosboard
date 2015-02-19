'use strict';

var App = require('./App'),
  Dashboard = require('./Dashboard'),
  Game = require('./Game'),
  Status = require('./Status'),
  React = require('react'),
  Router = require('react-router'),
  Route = Router.Route,
  DefaultRoute = Router.DefaultRoute;

var content = document.getElementById('app');

var Routes = (
  <Route ref="appRouter" name="app" path="/" handler={App}>
    <Route name="game" path="/games/:gameId" handler={Game} />
    <Route name="status" path="/status" handler={Status} />
    <DefaultRoute handler={Dashboard} />
  </Route>
);

Router.run(Routes, function (Handler) {
  React.render(<Handler/>, content);
});
