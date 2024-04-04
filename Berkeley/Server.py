import socket
import time
import threading  # Importamos el módulo threading

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
                    print("Sent time:", current_time)

# Función para calcular el promedio de los tiempos recibidos
def calculate_average_times(times):
    if not times:
        return None
    return sum(times) / len(times)

# Ejemplo de uso
if __name__ == "__main__":
    server_port = 12345
    times = []

    # Iniciar el servidor Berkeley en un hilo
    berkeley_server_thread = threading.Thread(target=berkeley_server, args=(server_port,))
    berkeley_server_thread.start()

    # Esperar a que el servidor inicie antes de conectarse
    time.sleep(1)