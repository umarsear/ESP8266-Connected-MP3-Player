# Acknowledgement
# Code in the file is based on the code share in the following Github Gist
# https://gist.github.com/zatarra/fcb9409ef1c1835fa5fb25a860991751
# https://www.davidgouveia.net/category/iot/

import machine
import socket
import ure
import mp3

RELAYS = [machine.Pin(i, machine.Pin.OUT) for i in (12, 13, 14, 15)]
html = """<!DOCTYPE html>
<html>
<head>
<style>
	.btn {
		background-color: #0c7538;
		border: none;
		color: white;
		padding: 15px 32px;
		text-align: center;
		text-decoration: none;
		display: inline-block;
		font-size: 16px;
		margin: 4px 2px;
		cursor: pointer;
	}
	.lnk {
		background-color: #500c75;
		padding: 5px 32px;
	}
	body {background-color: powderblue;}
	h1   {color: blue;}
	p    {color: red;}
</style>
<title>MP3 Player</title>
</head>
<body>
	<h1>WiFi MP3 Player</h1>
		<p>
			<a href="/prev" class="btn">Prev</a>
			<a href="/play" class="btn">Play</a>
			<a href="/pause" class="btn">Pause</a>
			<a href="/resume" class="btn">Resume</a>
			<a href="/next" class="btn">Next</a>
		</p>
		<p>
			<a href="/play?track=1" class="btn lnk">1</a>
			<a href="/play?track=5" class="btn lnk">5</a>
			<a href="/play?track=10" class="btn lnk">10</a>
			<a href="/play?track=15" class="btn lnk">15</a>
			<a href="/play?track=20" class="btn lnk">20</a>
		</p> 
	</body>
</html>
"""
  
def play_track(track):
  if track is None:
    track=1
  mp3.play_track(int(track))
  return "track %s" % (int(track))

def play_next():
  mp3.next()
  return "done"

def play_prev():
  mp3.previous()
  return "done"
  
def pause_play():
  mp3.pause()
  return "Paused"

def resume_play():
  mp3.resume()
  return "resumed"
  
def parseURL(url):
  #PARSE THE URL AND RETURN THE PATH AND GET PARAMETERS
  parameters = {}
  
  path = ure.search("(.*?)(\?|$)", url) 
  
  while True:
    vars = ure.search("(([a-z0-9]+)=([a-z0-8.]*))&?", url)
    if vars:
      parameters[vars.group(2)] = vars.group(3)
      url = url.replace(vars.group(0), '')
    else:
      break

  return path.group(1), parameters

def buildResponse(response):
  # BUILD DE HTTP RESPONSE HEADERS
  global html
  return '''HTTP/1.0 200 OK\r\nContent-type: text/html\r\nContent-length: %d\r\n\r\n%s''' % (len(html), html)
    
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

print('listening on', addr)

while True:
    cl, addr = s.accept()
    print('client connected from', addr)
    request = str(cl.recv(1024))
    print("REQUEST: ", request)

    obj = ure.search("GET (.*?) HTTP\/1\.1", request)
    print(obj.group(1))
    
    if not obj:
      cl.send(buildResponse("INVALID REQUEST"))
    else:
      path, parameters = parseURL(obj.group(1))
      
      if path.startswith("/play"):
        track=parameters.get("track",None)
        cl.send(buildResponse("Playing:\n%s" % play_track(track)))

      elif path.startswith("/next"):
        cl.send(buildResponse("Next :\n%s" % play_next()))

      elif path.startswith("/prev"):
        cl.send(buildResponse("Previous :\n%s" % play_prev()))

      elif path.startswith("/resume"):
        cl.send(buildResponse("Pause play:\n%s" % resume_play()))
      
      elif path.startswith("/pause"):
        cl.send(buildResponse("Pause play:\n%s" % pause_play()))
      
      elif path.startswith("/halt"):
        cl.send(buildResponse("Shutting down server\n"))
        break
      else:
        cl.send(buildResponse("UNREGISTERED ACTION\r\nPATH: %s\r\nPARAMETERS: %s" % (path, parameters)))
        
    cl.close()
