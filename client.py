import socket
import sys

socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

add = ('taranis.eecs.utk.edu',15153)
socket1.connect(add)

data = socket1.recv(32)
print data

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

###############################################
# Setup mock server to send data to interface #
###############################################
socket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = ("localhost", 10000)
socket2.bind(server)
socket2.listen(1)
message = connect(socket2)
socket2.close()

socket1.send(message)
secret = socket1.recv(1024)
print secret
