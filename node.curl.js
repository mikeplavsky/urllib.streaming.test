var spawn = require('child_process').spawn
var curl = spawn('curl', ['--no-buffer', '--noproxy', 'localhost' , 'http://localhost:2000'] );

curl.stdout.setEncoding('utf8');
curl.stderr.setEncoding('utf8');

curl.stdout.on( 'data', function (data) {
  console.log( data );
});

curl.stderr.on( 'data', function (data){
  console.log( data );
});
