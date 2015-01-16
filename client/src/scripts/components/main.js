'use strict';

var App = require('./App'),
  Dashboard = require('./Dashboard'),
  Game = require('./Game'),
  React = require('react'),
  Router = require('react-router'),
  Route = Router.Route,
  DefaultRoute = Router.DefaultRoute;

var content = document.getElementById('app');

var Routes = (
  <Route ref="appRouter" name="app" path="/" handler={App}>
    <Route name="game" path="/games/:gameId" handler={Game} />
    <DefaultRoute handler={Dashboard} />
  </Route>
);

Router.run(Routes, Router.HistoryLocation, function (Handler) {
  React.render(<Handler/>, content);
});
