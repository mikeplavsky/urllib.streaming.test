from nose.tools import *

import sys
sys.path.append( ".." )

import urllib2 
from chunked import fix_urllib

def test_fix():

  fix_urllib(urllib2)

  opener = urllib2.build_opener(urllib2.ProxyHandler({}))
  urllib2.install_opener( opener )

  conn = urllib2.urlopen("http://localhost:2000")
  http = conn.fp._sock

  res = []

  for obj in http.read():

    res.append( obj )
    print res

  eq_( len(res), 2 ) 
  eq_( res[1], '{name:"Next", building: {room: 500}}' )
