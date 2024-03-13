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

# GET list
httpTestMessages = [
        "GET /dashboard/ HTTP/1.1",             # 200 OK
        "GET /dashboard HTTP/1.1",              # 301 Moved Permanently
        "PUT / HTTP/1.1",                       # 302 Found
        "GET /dashboard HTTP/1.",               # 400 Bad Request
        "GET /dashboard/index.htm HTTP/1.1",    # 404 Not Found
        "PUT /d HTTP/1.1",                      # 405 Method Not Allowed
        ]

# Cycle through predefined messages
for sentence in httpTestMessages:

    # Socket open and connect
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))

    # Join serverName to the current sentence
    sentence += "\r\nHost:" + serverName + "\r\n\r\n"

    # Socket encode message and send
    clientSocket.send(sentence.encode())

    # Receive and out the response message
    modifiedSentence = clientSocket.recv(1024)

    # Print the requested message
    print ("-"*60)
    print ("From Server:", modifiedSentence.decode())

    # Close socket connection
    clientSocket.close()
