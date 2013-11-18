'use strict';

/* Controllers */

var classControllers = angular.module('classControllers', []);

classControllers.controller('ClassListCtrl', [ '$scope', '$http' ,
	function ClassListCtrl( $scope, $http ){
	$http.get('http://localhost:10080/class').success(function(data) {
		$scope.course = data;
	});
	$scope.orderProp = 'data.time';
}]);


classControllers.controller('ClassMsgCtrl', ['$scope', '$routeParams', '$http',
  function($scope, $routeParams, $http) {
    $http.get('http://localhost:10080/class/' + $routeParams.courseId).success(function(data) {
      $scope.messages = data;
      $scope.courseId = $routeParams.courseId;
    });
    $http.get('http://localhost:10080/class').success(function(classData) {
    	$scope.courseData = classData;
    });
    $scope.orderProp = '-time';
  }]);