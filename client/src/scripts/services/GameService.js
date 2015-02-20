var Q = require("q"),
  Request = require("superagent"),
  baseEndpoint = __SERVER_URL__ + "/games";

var GameService = {
  get: function (gameId) {
    var deferred = Q.defer(),
      url = baseEndpoint + '/' + gameId;

    Request
      .get(url)
      .end(function (response) {
        if (response.status === 200) {
          deferred.resolve(response.body);
        } else {
          deferred.reject(response.body);
        }
      });

    return deferred.promise;
  },

  update: function (gameId, score) {
    var deferred = Q.defer(),
      url = baseEndpoint + '/' + gameId;

    Request
      .patch(url)
      .send(score)
      .end(function (response) {
        if (response.status === 200) {
          deferred.resolve(response.body);
        } else {
          deferred.reject(response.body);
        }
      });

    return deferred.promise;
  },

  getStatus: function () {
    var deferred = Q.defer(),
      url = __SERVER_URL__ + '/status';

    Request
      .get(url)
      .end(function (response) {
        if (response.status === 200) {
          deferred.resolve(response.body);
        } else {
          deferred.reject(response.body);
        }
      });

    return deferred.promise;
  },

  getList: function () {
    var deferred = Q.defer(),
      url = baseEndpoint;

    Request
      .get(url)
      .end(function (response) {
        if (response.status === 200) {
          deferred.resolve(response.body);
        } else {
          deferred.reject(response.body);
        }
      });

    return deferred.promise;
  },

  getStats: function () {
    var deferred = Q.defer(),
      url = __SERVER_URL__ + '/stats';

    Request
      .get(url)
      .end(function (response) {
        if (response.status === 200) {
          deferred.resolve(response.body);
        } else {
          deferred.reject(response.body);
        }
      });

    return deferred.promise;
  },

  create: function (newGame) {
    var deferred = Q.defer(),
      url = baseEndpoint;

    Request
      .post(url)
      .send(newGame)
      .end(function (response) {
        if (response.status === 201) {
          deferred.resolve(response.body);
        } else {
          deferred.reject(response.body);
        }
      });

    return deferred.promise;
  }
};

module.exports = GameService;
