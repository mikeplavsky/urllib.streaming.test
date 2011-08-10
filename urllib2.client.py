import urllib2
from chunked import fix_urllib

fix_urllib(urllib2)

opener = urllib2.build_opener(urllib2.ProxyHandler({}))
urllib2.install_opener( opener )

conn = urllib2.urlopen("http://localhost:2000")
http = conn.fp._sock

for res in http.read():
  print res
