 # Importar librerias
import socket
import threading

# Creamos el socket del servidor TCP:
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ("Socket Created")

# Se define el host
host = "localhost"

# Se define el puerto
port = 6666

# Lo vinculamos al puerto con la función bind()
sock.bind((host, port))
print ("socket bind complete")

# Establecemos un *timeout*
sock.settimeout(60)

file = open("img.png", "wb")
# Ponemos el servidor en modo escucha:
sock.listen(1)


while True:
    # Se establece la conexion con el cliente
    connection, client_address = sock.accept()
    print ('Got connection from', client_address)
    print ("Receiving...")

    data = connection.recv(1024)
    if data == b"DONE":
        print("Done Receiving.")
        break
    file.write(data)
file.close()
connection.send("End of connection")
connection.shutdown(2)
connection.close()
sock.close()  
