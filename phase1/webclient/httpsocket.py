"""
Name: Python TCP Client
Description: Simple TCP client using sockets
Original code by: Luís Pires
Source: Chapter 2, slide 104

Commented and adapted by: Nuno Brito
"""

# Import from everything from the socket library
from socket import *

# Specify servername and port destination
serverName = ’172.24.1.12’
serverPort = 80

# Socket open and connect
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

# HTTP1.1/GET message
#   Input manually
#sentence = raw_input(‘Input lowercase sentence:’)
sentence = 
#   Cycle through a list
# TODO!!!

# Socket send
clientSocket.send(sentence.encode())

# Receive and output the response message
modifiedSentence = clientSocket.recv(1024)
print (‘From Server:’, modifiedSentence.decode())

# Socket close connection
clientSocket.close()
