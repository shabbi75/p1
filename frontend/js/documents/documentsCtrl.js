(function(){
  'use strict';
  angular
  .module('sshdb.documents')
  .controller('DocsCTRL', ['Docs', function DocsCTRL(Docs){
    var vm = this;
    vm.docsList = [];

    Docs.all().then(function(response){
      vm.docsList = response;
    });

  }]);
}());
