import urllib2

opener = urllib2.build_opener(urllib2.ProxyHandler({}))
urllib2.install_opener( opener )

conn = urllib2.urlopen("http://localhost:2000")
socket = conn.fp._sock.fp._sock


while True:
  
  data = socket.recv(4*1024)

  if not data: 
    exit(0) 
  
  print data
