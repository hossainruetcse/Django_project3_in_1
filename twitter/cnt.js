
var app=angular.module('myApp', [])
app.controller('myCtrl', function ($scope, $http) {
   

    $scope.sendPost = function() {
        var data ={
           
                
            oauth_consumer_key : "eVn2thT0m67dUIsXBYBZhoanw", 
	    oauth_nonce : "915f03f0f0dbd991c8353d97c3d40e44", 
	    oauth_signature : "OsYUYkUaKKdOo4mStrLicqH6m4c%3D",
	    oauth_signature_method :"HMAC-SHA1", 
	    oauth_timestamp : "1456915821",
	    oauth_token :"388776429-JroFtisb4DUOQKkIC7yHe5NhIDk3tlo7HYQfz6m2",
	    oauth_version : "1.0",

            };
        $http.post("https://api.twitter.com/oauth/request_token", data).success(function(response, status) {
            console.log(respone);
        })
    }                   
})









