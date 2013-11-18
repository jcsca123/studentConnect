'use strict';



var studentconnectApp = angular.module('studentconnectApp', [
  'ngRoute',
  'classControllers'
]);
 
studentconnectApp.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.
      when('/class', {
        templateUrl: 'partials/class-list.html',
        controller: 'ClassListCtrl'
      }).
      when('/class/:courseId', {
        templateUrl: 'partials/message-list.html',
        controller: 'ClassMsgCtrl'
      }).
      otherwise({
        redirectTo: '/class'
      });
  }]);