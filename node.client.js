var http = require('http');
var client = http.createClient(2000,'localhost');

var request = client.request('GET', '/');

request.on( 'response', function(response) {

  response.setEncoding( "utf8" );

  response.on( 'data', function(chunk) {
    console.log( chunk );
  });

});

request.end()
