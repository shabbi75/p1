(function(){
  'use strict';

  angular
    .module('sshdb.documents', [])
    .config(function ($stateProvider){

      $stateProvider
      // Docs listing page
      .state('docs', {
        url: '/documents',
        templateUrl: 'js/documents/documents.html',
        controller:'DocsCTRL',
      })
      // Document browsing detail view
      .state('detail', {
        url: '/:id/:name',
        templateUrl: 'js/documents/document-detail-view.html',
        controller:'DocsDetailCTRL'
      });
  });
})();
