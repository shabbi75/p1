routerApp.service('Login', ['$http', '$window', function($http, $window){
  var self = this;

  self.authenticate = function(data) {

    /*preparing post setup*/

    var uname = data.username || 'ssh';
    var pwd = data.password || 'homework';

    var postvals = "username=" + uname + "&password=" + pwd;
    var postconfig = {
      method:'POST',
      url:'/api/login',
      data: postvals,
      headers: {'Content-Type': 'application/x-www-form-urlencoded'}
    };

    var promise = $http(postconfig)
    .then(function(response){
      if(response.data.token)
        self.saveToken(response.data.token);
      return response.data;
    })
    return promise;
  }

  self.saveToken = function(token) {
    $window.localStorage['jwtToken'] = token;
  }

  self.getToken = function() {
    return $window.localStorage['jwtToken'];
  }

}]);
