var Q = require("q"),
  Request = require("superagent"),
  baseEndpoint = "http://localhost:5000/api/games";

var GameService = {
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
