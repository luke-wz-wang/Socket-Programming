
from socket import *
import sys

# Port that being listened with number between 1024 and 65335
serverPort = int(sys.argv[1])
serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('', serverPort))

while True:
    message, clientAddress = serverSocket.recvfrom(2048)  # recieve x
    print("RECEIVED ", message.decode())
    value = int(message.decode())
    if value > 0:
        value = value-1
        modifiedMessage = str(value)
        serverSocket.sendto(modifiedMessage.encode(),
                            clientAddress)  # send x - 1
        print("SENT ", modifiedMessage)
