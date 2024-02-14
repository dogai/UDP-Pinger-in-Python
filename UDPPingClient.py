import time
from socket import *

serverAddr = 'localhost' 
serverPort = 12000  

clSocket = socket(AF_INET, SOCK_DGRAM)
clSocket.settimeout(1)

for sequence_number in range(1, 11):
    try:
        sendTime = time.time()

        msg = f'Ping {sequence_number} {sendTime}'.encode()
        clSocket.sendto(msg, (serverAddr, serverPort))
        modifiedMsg, serverAddress = clSocket.recvfrom(1024)

        rcvTime = time.time()

        RTT = rcvTime - sendTime

        print(f'{modifiedMsg.decode()} ')
        print(f'RTT time is {RTT:.6f} sec')
        print('')

    except timeout:
        print('Request timed out.')
        print('')

clSocket.close()

