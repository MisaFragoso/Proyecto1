import socket
import time

def berkeley_client(server_address, port, num_requests):
    times = []  # Lista para almacenar la lista de tiempo recibidos

    # Realizar varias solicitudes al servidor
    for _ in range(num_requests):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((server_address, port))
            s.sendall(b"GET_TIME")
            data = s.recv(1024)
            server_time = float(data.decode())
            offset = server_time - time.time()
            times.append(offset)
            print("Server time:", server_time)
            print("Local time:", time.time())
            print("Offset:", offset)
            print("")

    # Calcular el promedio de los ajustes de tiempo
    average_offset = sum(times) / len(times)
    print("Average offset:", average_offset)

if __name__ == "__main__":
    server_address = 'localhost'
    server_port = 12345
    num_requests = 5  # Número de solicitudes al servidor
    berkeley_client(server_address, server_port, num_requests)
