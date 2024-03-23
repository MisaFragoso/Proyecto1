import socket
import time
import datetime

def stringToTime(cadena):
    format= '%Y%m%d %H:%M:%f'
    horaCadena=datetime.datetime.strptime(cadena,format)
    return horaCadena

ServerIP="localhost"
ServerPort= 9099
#Apertura del socket
clientSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

start=time.time()
#Solicitar conexion con el servidor
clientSocket.connect((ServerIP,ServerPort))
#Recibir del servidor
horaCadena=clientSocket.recv(4096).decode()

final=time.time()
time=final-start

hora=stringToTime(horaCadena)
print("El  tiempoTotal de ida y vuelta fue:", time)

halfTime= time/2

print("Tiempo total de ida", halfTime)
print("Hora servidor", horaCadena)
print("La hora exacta es" , hora+datetime.timedelta(seconds=halfTime))

clientSocket.close()