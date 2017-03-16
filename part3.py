import socket
import sys

def connect(socket):
  socket.listen(1)
  while True:
    print "Listening to connection.."
    connection, client = socket.accept()
    try:
      connection.sendall(data)
      print data
      d= connection.recv(1024)
      print d
    finally:
      return d

# Set up a socket connection to talk to Project server.
socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
add = ('taranis.eecs.utk.edu',15153)
socket1.connect(add)

# Receive the Project server's initial message.
data = socket1.recv(32)
print data

# Set up a socket connection to act as a server for the client.
# Send the client the Project server's message, and then
# receive the client's response.
socket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = ("localhost", 10000)
socket2.bind(server)
socket2.listen(1)
message = connect(socket2)
socket2.close()

# Send the client's response to the Project server and receive
# the secret from the Project server.
socket1.send(message)
secret = socket1.recv(1024)
print secret
