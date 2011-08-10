import urllib2

def _read_chunked(self,amt):
  
  chunk_left = self.chunk_left

  while True:

      if chunk_left is None:

	  line = self.fp.readline()
	  i = line.find(';')
	  if i >= 0:
	      line = line[:i] # strip chunk-extensions
	  chunk_left = int(line, 16)
	  if chunk_left == 0:
	      break

      yield self._safe_read(chunk_left)
      
      # we read the whole chunk, get another
      self._safe_read(2)      # toss the CRLF at the end of the chunk
      chunk_left = None

  # read and discard trailer up to the CRLF terminator
  ### note: we shouldn't have any trailers!
  while True:
      line = self.fp.readline()
      if not line:
	  # a vanishingly small number of sites EOF without
	  # sending the trailer
	  break
      if line == '\r\n':
	  break

  # we read everything; close the "file"
  self.close()

urllib2.httplib.HTTPResponse._read_chunked = _read_chunked

opener = urllib2.build_opener(urllib2.ProxyHandler({}))
urllib2.install_opener( opener )

conn = urllib2.urlopen("http://localhost:2000")
http = conn.fp._sock

for res in http.read():
  print res
