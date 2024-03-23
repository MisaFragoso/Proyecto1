import socket
import datetime

serverDirect = "localhost"
serverPort = 9099

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverSocket.bind((serverDirect, serverPort))
serverSocket.listen()

while True:
    socketConection, addr = serverSocket.accept()
    print("Connected to client: ", addr)

    time = datetime.datetime.now()

    timeString = time.strftime('%Y%m%d %H:%M:%f')
    print("Sending time to client: ", addr)
    print(time)
    socketConection.send(timeString.encode())
    socketConection.close()
