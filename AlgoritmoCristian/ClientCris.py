import socket
import time
import datetime

def stringToTime(string):
    format = '%Y%m%d %H:%M:%f'
    timeString = datetime.datetime.strptime(string,format)
    return timeString

ServerIP="localhost"
ServerPort= 9099
#creación del socket
clientSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
start=time.time()
#Solicitar conexion con el servidor
clientSocket.connect((ServerIP,ServerPort))
#Recibir del servidor
timeString = clientSocket.recv(4096).decode()

final = time.time()
time = final-start

hora = stringToTime(timeString)
print("Total time (ida y vuelta): ", time)

halfTime= time/2

print("Total time: ", halfTime)
print("Server time: ", timeString)
print("Exact time: " , hora + datetime.timedelta(seconds=halfTime))

clientSocket.close()
