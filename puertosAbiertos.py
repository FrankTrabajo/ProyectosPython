import socket

# Dirección IP que quieres escanear
ip_address = "127.0.0.1"

# Crear un socket
a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Rango de puertos a escanear
start_port = 1
end_port = 65535

# Escanear puertos en el rango especificado
for port in range(start_port, end_port):
    location = (ip_address, port)
    # Verificar si el puerto está abierto
    result = a_socket.connect_ex(location)
    
    if result == 0:
        print(f"Port {port} on IP {ip_address} is open")
        
    # Cerrar el socket y crear uno nuevo para la próxima iteración
    a_socket.close()
    a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Cerrar el socket final
a_socket.close()
