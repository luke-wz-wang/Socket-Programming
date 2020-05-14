# Socket-Programming
Socket Programming in Python


**Project 1: Countdown Protocol**



Implemented a basic UDP-based client and server that run the following countdown protocol.



  - Client

  Send integer X to server.

  Print “SENT “ + X.

  while True:

  Receive message from server

  containing integer X.

  Print “RECEIVED “ + X.

  if X > 0:

  Send integer X - 1 to server.

  Print “SENT “ + X.





  - Server

  while True:

  Receive message from client

  containing integer X.

  Print “RECEIVED “ + X.

  if X > 0:

  Send integer X - 1 to client.

  Print “SENT “ + X.





**Project 2: Simplified Web Server**

- listens to a TCP port

- GET requests return 200 + the data for all existing files in tree

- GET requests return 301 for all paths specified as redirects in redirects.defs
and actually redirects the web client

- GET requests return 404 for all non-existent paths and www/redirect.defs

- HEAD requests return 200 (but no data) for all existing files

- HEAD requests return 301, 404 for all paths in exactly the same way as for GET
requests above

- Any other unknown method returns a 405

- Any malformed request returns a 400

- Server can handle multiple requests in succession without restarting (loops
around and accepts the connection again

- Server either spawns new thread, forks new process, or asynchronously
handles web requests


