(function(){
  'use strict';
  routerApp
  .controller('loginCTRL', ['Login', '$location', '$state', function loginCTRL(Login, $location, $state){
    var vm = this;
    vm.userinfo = {};
    vm.userinfo.username = 'ssh';
    vm.userinfo.password = 'homework';
    vm.totalstates = $state.get();
    console.log('total stats', vm.totalstates)
    vm.send = function(){
      Login.authenticate(vm.userinfo).then(function(response){
        $location.path('/documents');
      })
    }
  }]);
}());
