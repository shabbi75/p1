var gulp = require('gulp');
var connect = require('gulp-connect');
var plugins            = require('gulp-load-plugins')();
var historyApiFallback = require('connect-history-api-fallback');

// A local web server to proxy calls to back-end
gulp.task('webserver', function() {
  plugins.connect.server({
    root: './',
    port: 5001,
    livereload: true,
    middleware: function(connect, o) {
      return [ (function() {
        var url = require('url');
        var proxy = require('proxy-middleware');
        var options = url.parse('http://localhost:3000/api');
        options.route = '/api';
        return proxy(options);
      })(), historyApiFallback() ];
    }
  });
});


gulp.task('default', [ 'webserver'])
