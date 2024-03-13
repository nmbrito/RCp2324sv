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
serverName = "172.24.1.12"
serverPort = 80
serverDestination = "/dashboard"

# GET list
"""
httpMessages = ["GET " + serverDestination + " HTTP/1.1\r\nHost:" + serverName + "\r\n\r\n",
                "GET " + serverDestination + " HTTP/1.\r\nHost:" + serverName + "\r\n\r\n"]
httpMessages = ["GET HTTP/1.1\r\nHost:\r\n\r\n",
                "GET HTTP/1.1\r\nHost:\r\n\r\n"]
"""

httpMessages = [
        "GET /dashboard/ HTTP/1.1\r\nHost:172.24.1.12\r\n\r\n",             # 200 OK
        "GET /dashboard HTTP/1.1\r\nHost:172.24.1.12\r\n\r\n",              # 301 Moved Permanently
        "PUT / HTTP/1.1\r\nHost:172.24.1.12\r\n\r\n",                       # 302 Found
        "GET /dashboard HTTP/1.\r\nHost:172.24.1.12\r\n\r\n",               # 400 Bad Request
        "GET /dashboard/index.htm HTTP/1.1\r\nHost:172.24.1.12\r\n\r\n",    # 404 Not Found
        "PUT /d HTTP/1.1\r\nHost:172.24.1.12\r\n\r\n",                      # 405 Method Not Allowed
        ]

# Socket open and connect
#clientSocket = socket(AF_INET, SOCK_STREAM)
#clientSocket.connect((serverName,serverPort))

# FALL BACK
# HTTP1.1/GET message
#sentence = raw_input(‘Input lowercase sentence:’)                   # User input
#sentence = "GET /dashboard/ HTTP/1.1\r\nHost:172.24.1.12\r\n\r\n"   # Manual message
#
## Socket send
#clientSocket.send(sentence.encode())
#
## Receive and output the response message
#modifiedSentence = clientSocket.recv(1024)
#print ("From Server:", modifiedSentence.decode())
#
## Socket close connection
#clientSocket.close()

# The cycle Way
for sentence in httpMessages:
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    # Socket encode message and send
    clientSocket.send(sentence.encode())
    # Receive and out the response message
    modifiedSentence = clientSocket.recv(1024)
    # Print the requested message
    print ("-"*60)
    print ("From Server:", modifiedSentence.decode())
    clientSocket.close()

#clientSocket.close()
