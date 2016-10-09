(function(){
  'use strict';

angular
  .module('sshdb.documents')
  .service('Docs', ['$http', 'Login', function($http, Login){
  var self = this;
  var config = {
    method:'GET'
  };
  self.addHeader = function(){
    var token = Login.getToken();
    config.headers = {'Authorization': 'Bearer ' + token}
  }
  self.all = function() {
    /*preparing post setup*/
    config.url = '/api/documents';
    self.addHeader();
    var promise = $http(config)
    .then(function(response){
      return response.data;
    }, function(data, statusCode){
      console.log(' error occured in docs service func=all', data)

    })
    return promise;
  }

  self.getDocById = function(id){
    config.url = '/api/document/'+ id + '/text' ;
    self.addHeader();

    var promise = $http(config)
    .then(function(response){
      return response.data;
    },function(data, statusCode){
      console.log(' error occured in docs service func=getDocById', data)

    });
    return promise;
  }
  self.highlightWords = function(id, searchText){
    var searchParam = '';
    if(searchText!='') {
      searchParam = '?search=' + searchText;
    }
    self.addHeader();

    config.url = '/api/document/'+ id + '/text' + searchParam;

    var promise = $http(config)
    .then(function(response){
      return response.data;
    },function(data, statusCode){
      console.log(' error occured in docs service func=highlightWords', data)

    });
    return promise;
  }

  self.scanText = function(immutable, positions){
    var buffer = '';
    var totalMatches = 0;
    if(!immutable || !positions) {
      return;
    }
    _.each(immutable, function(chara, pos){
      _.each(positions, function(n){
        if(n[0]==pos && n[1]-1==pos){
          chara = '<span class="highlight">' + chara + '</span>';
          totalMatches++;
        }
        else if(n[0]==pos){
          chara = '<span class="highlight">' + chara ;
          totalMatches++;
        }
        else if(n[1]-1==pos){
          chara +=  '</span>';
        }
      });
      buffer+=chara;
    });
    return [buffer, totalMatches];
  }

}]);

}());
