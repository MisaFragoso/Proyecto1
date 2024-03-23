import socket
import datetime

serverDirect = "localhost"
serverPort = 9099

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverSocket.bind((serverDirect, serverPort))
serverSocket.listen()

while True:
    socketConection, addr = serverSocket.accept()
    print("Conectado con cliente", addr)

    hora = datetime.datetime.now()

    horaCadena = hora.strftime('%Y%m%d %H:%M:%f')
    print(" Envio la hora al cliente", addr)
    print(hora)
    socketConection.send(horaCadena.encode())
    socketConection.close()