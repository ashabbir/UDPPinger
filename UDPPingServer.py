#Ahmed Shabbir POLY ID 0504100
#CN 6843
#UDP Server Home work Assignment 2
#Server is modified to see clear results
import random 
from socket import * 
import sys

# Create a UDP socket 
# Notice the use of SOCK_DGRAM for UDP packets 
serverSocket = socket(AF_INET, SOCK_DGRAM) 
# Assign IP address and port number to socket 
IP = "localhost"
PORTNO = 1200
print "begin bind IP:{0} PORT:{1}".format(IP,PORTNO)
serverSocket.bind((IP, PORTNO)) 
print "bind successfull"
 
while True: 
    # Generate random number
    rand = random.randint(0, 10) 
    # Receive the client packet along with the address it is coming from 
    message, address = serverSocket.recvfrom(1024) 
    # Capitalize the message from the client 
    # If rand is less is than 4, we consider the packet lost and do not respond
    message = message.upper()
    if rand < 4:
        print "message received: {0}, will not repond".format(str(message))
        continue 
    
    # Otherwise, the server responds 
    serverSocket.sendto(message, address) 
    print "message received: {0}, will responded to:{1}".format(str(message), str(address))
    