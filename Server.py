import socket
import time

def berkeley_server(port):
    # Creamos un socket TCP/IP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Asociamos el socket al puerto especificado
        s.bind(('localhost', port))
        # Escuchamos conexiones entrantes
        s.listen(5)
        print("Server listening on port", port)

        while True:
            # Aceptamos una conexión
            conn, addr = s.accept()
            print("Connected by", addr)
            with conn:
                # Recibimos la solicitud del cliente
                data = conn.recv(1024)
                if data:
                    # Respondemos con la hora actual del servidor
                    current_time = time.time()
                    conn.sendall(str(current_time).encode())

if __name__ == "__main__":
    server_port = 12345
    berkeley_server(server_port)
