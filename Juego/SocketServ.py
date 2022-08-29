import socket
import sys
 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.88.20'
port = 8080

sock.bind((host, port))

sock.listen(1)

print('Esperando por una conexión')
connection, client = sock.accept()
 
print(client, 'Conectado')
 
data = connection.recv(16)
print('Recibido "%s"' % data)
if data:
 
    connection.sendall(data)
else:
    print('Sin datos de', client)
 
connection.close()