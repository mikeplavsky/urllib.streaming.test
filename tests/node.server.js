var http = require( 'http' );

var srv = http.createServer(function(req,res) {

  res.writeHead( 200, {'conten-type': 'text/plain' } );

  res.write( '{name:"Test", data: [1,2,3,4,5]}' );

  setTimeout ( function () {
    res.end( '{name:"Next", building: {room: 500}}' );
  }, 100);
  
});

srv.listen( 2000 );
