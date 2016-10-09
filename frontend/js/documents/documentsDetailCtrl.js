(function(){
  'use strict';
  angular
  .module('sshdb.documents')
  .controller('DocsDetailCTRL', ['Docs', '$stateParams', '$sce', function DocsDetailCTRL(Docs, $stateParams, $sce){
    var vm = this;
    vm.docDetail = '';
    vm.searchText = '';
    vm.Immutable = '';
    vm.searched=0;
    var id = $stateParams.id;
    vm.name = $stateParams.name;
    vm.getText = function() {
      Docs.getDocById(id).then(function(response){
        vm.Immutable = response;
        vm.docDetail = vm.Immutable;
      });
    }

    vm.highlight = function(){
      if(!vm.searchText){
        return;
      }
      vm.searched = 1;
      var buffer = '';
      var feedback = '';
      Docs.highlightWords(id, vm.searchText)
      .then(function(response){
        feedback = Docs.scanText(vm.Immutable, response);
        vm.totalMatches = feedback[1];
        vm.docDetail = $sce.trustAsHtml(feedback[0]);
      })
    }
    vm.getText();
  }]);
}());
