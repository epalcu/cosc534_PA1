import socket
import sys

def connect(socket):
  socket.listen(1)
  while True:
    print "Listening to connection.."
    connection, client = socket.accept()
  try:
    connection.sendall(data)
  finally:
    print "Connection to client lost.."
  return connect(socket)

  ###############################################
  # Setup mock server to send data to interface #
  ###############################################
  socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server = ("localhost", 10000)
  socket.bind(server)
  socket.listen(1)
  connect(socket)
