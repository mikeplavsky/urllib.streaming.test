import urllib

conn = urllib.urlopen("http://localhost:2000")

while True:
  
  data = conn.readline()

  if not data: 
    exit(0) 
  
  print data
