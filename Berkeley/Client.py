import socket
import time

def berkeley_client(server_address, port):
    # Creamos un socket TCP/IP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Nos conectamos al servidor
        s.connect((server_address, port))
        # Enviamos una solicitud de tiempo al servidor
        s.sendall(b"GET_TIME")
        # Recibimos la hora del servidor
        data = s.recv(1024)
        server_time = float(data.decode())
        # Calculamos la diferencia de tiempo entre el servidor y el cliente
        offset = server_time - time.time()
        # Ajustamos la hora local del cliente
        adjusted_time = time.time() + offset
        print("Server time:", server_time)
        print("Local time:", time.time())
        print("Adjusted time:", adjusted_time)

if __name__ == "__main__":
    server_address = 'localhost'
    server_port = 12345
    berkeley_client(server_address, server_port)