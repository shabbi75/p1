var routerApp = angular.module('sshdb', [

  //3rd party modules
  'ui.router',
  'ngSanitize',

  // app modules
  'menu.bar',
  'sshdb.documents'
]);
function authInterceptor($location, $q) {

  return {

    request: function(config) {
      return config;
    },

    response: function(res) {
      return res;
    },

    responseError: function(rejection){
      if(rejection.status==401) {
        $location.path('/login');
      }
      return $q.reject(rejection);
    }
  }
}

routerApp.config(function($stateProvider, $urlRouterProvider, $httpProvider) {

    $httpProvider.interceptors.push(authInterceptor);


    $stateProvider
        // Login View
        .state('home', {
            url: '/login',
            templateUrl: 'js/login/login.html',
            controller:'loginCTRL'
        });

    $urlRouterProvider.otherwise('/login');

});
