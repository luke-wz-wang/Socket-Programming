
from socket import *
import sys

hostAndPort = sys.argv[1].split(":")

serverName = hostAndPort[0]  # IP addr or host's name
serverPort = int(hostAndPort[1])  # server's Port
message = sys.argv[2]  # countdown value

clientSocket = socket(AF_INET, SOCK_DGRAM)
value = int(message)
clientSocket.sendto(message.encode(), (serverName, serverPort))
print("SENT ", message)


if value > 0:  # if value is 0 then there is no need to continue
    while True:
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        print("RECEIVED ", modifiedMessage.decode())
        value = int(modifiedMessage.decode())
        if value > 0:  # if value is 0 then there is no need to continue
            value = value - 1
            modifiedMessage = str(value)
            clientSocket.sendto(modifiedMessage.encode(),
                                (serverName, serverPort))  # send x - 1
            print("SENT ", modifiedMessage)
            if value == 0:
                clientSocket.close()
                break
        else:
            clientSocket.close()
            break
else:
    clientSocket.close()
