var Q = require("q"),
  Request = require("superagent"),
  baseEndpoint = __SERVER_URL__ + "/players";

var PlayerService = {
  getList: function () {
    var deferred = Q.defer(),
      url = baseEndpoint;

    Request
      .get(url)
      .end(function (response) {
        if (response.status === 200) {
          deferred.resolve(response.body.players);
        } else {
          deferred.reject(response.body);
        }
      });

    return deferred.promise;
  }
};

module.exports = PlayerService;
