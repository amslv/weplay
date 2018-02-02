var myApp = angular.module('weplay', ['ngRoute']);

myApp.config(function ($routeProvider) {
  $routeProvider
    .when('/', {templateUrl: '/static/components/home.html'});
});
