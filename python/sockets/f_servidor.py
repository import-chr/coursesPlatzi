import socket
import sys

# ADIOS - FIN DE COMUNICACION

# Configuración del servidor
host = 'localhost'
port = 12345

# Crear un socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlace del socket al host y puerto
server_socket.bind((host, port))

# Escuchar conexiones entrantes
server_socket.listen(3)
print(f"El servidor está escuchando en {host}:{port}")

while True:
    # Aceptar una conexión entrante
    client_socket, client_address = server_socket.accept()
    print(f"Conexión entrante desde {client_address}")

    try:
        for i in range(5):
            # Recibir datos del cliente
            data = client_socket.recv(1024)
            print(f"Datos recibidos del cliente: {data.decode('utf-8')}")

            if "adios" in data.decode('utf-8'):
                print("cerrando conexion con el cliente")
                break #client_socket.close()

            # Enviar respuesta al cliente
            response = input() # "Hola, cliente"
            client_socket.sendall(response.encode('utf-8'))
    except:
        print ('\n Hubo un fallo en la fase de comunicacion')
        
        # Cerrar las conexiones
        client_socket.close()        
        # server_socket.close()