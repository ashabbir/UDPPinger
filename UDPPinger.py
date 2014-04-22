#Ahmed Shabbir POLY ID 0504100
#CN 6843
#SIMPLE UDP PINGER Home work Assignment 2

import time
from socket import *



def percent(part, whole):
    return 100 * float(part)/float(whole)
    
    
#added these comments as check points as i m using textmate and this is my first python program
print "Being program"

#Constant definations
IP = "localhost"
PORTNO = 1200
PAYLOADSIZE = 1024
#create address
udpserveraddress = (IP,PORTNO)
#creating clientsocket 
clientsocket = socket(AF_INET, SOCK_DGRAM)

#setting time 
clientsocket.settimeout(1)
counter = 1
totalloss = 0
average = 0
maxtime = 0
mintime = 1

#loop 10 times
while counter < 11:
    #creating message to send
    msg = "{0} {1}".format(str(counter) , str(time.clock()))
    #start the clock
    timer = time.clock()
    clientsocket.sendto(msg , udpserveraddress)
    try:
        message, addy = clientsocket.recvfrom(PAYLOADSIZE)
        timespan = time.clock() - timer
        if timespan >= maxtime:
            maxtime = timespan
        if timespan <= mintime:
            mintime = timespan
        
        average = average + timespan
        print("Sequence number {0} {1} ".format(str(counter), str(timespan)))
    except Exception as e:
        #oops had an error what was it
        timespan = time.clock() - timer
        totalloss = totalloss + 1 
        print("Sequence number {0} {1} Package lost ".format(str(counter), str(timespan)))

    counter = counter + 1;

#calcualte percent loss and average RTT (where aRTT Sum(sentsuccesstime) / no of success)
loss =percent(totalloss , counter-1)
average = average / (counter-totalloss)
print "max RTT: {0}\nmin RTT: {1}\naverage RTT: {2}\nPackage lost % {3}".format(str(maxtime) , str(mintime),  str(average) ,str(loss))



