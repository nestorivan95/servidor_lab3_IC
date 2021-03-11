#servidor
import socket
import threading

host = "127.0.0.1"
port = 6666

# Creamos el socket del servidor TCP:
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ("Socket Created")

# Lo vinculamos al puerto con la función bind()
sock.bind((host, port))
print ("socket bind complete")

# Establecemos un *timeout*
socketServidor.settimeout(60)

# Ponemos el servidor en modo escucha:
sock.listen()
print ("socket now listening")


def worker(*args):
    conn = args[0]
    addr = args[1]
    try:
        print('conexion con {}.'.format(addr))
        conn.send("server: Hello client".encode('UTF-8'))
        while True:
            datos = conn.recv(4096)
            if datos:
                print('recibido: {}'.format(datos.decode('utf-8')))
                print("Recibo conexion de la IP: " + str(addr[0]) + " Puerto: " + str(addr[1]))

            else:
                print("prueba")
                break
    finally:
        conn.close()
        sock.close()
        print("Conexiones cerradas")

# Se crea un bucle infinito
while 1:
    # Recibimos la petición
    conn, addr = sock.accept()
    threading.Thread(target=worker, args=(conn, addr)).start()
