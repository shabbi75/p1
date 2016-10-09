(function(){
  'use strict';

  angular
    .module('menu.bar', [])
    .directive('menuBar', function(){
      return {
        restrict: 'EA',
        templateUrl: 'js/menu/menubar.html',
        controller:menuCTRL,
        controllerAs: 'vm'
      }
    });
    //directive's own controller
    menuCTRL.$inject = ['$state'];
    function menuCTRL($state){
      var vm = this;
      vm.listStates = $state.get();
    }
})();
