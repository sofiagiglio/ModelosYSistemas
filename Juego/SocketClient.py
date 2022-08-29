import socket

HOST = "192.168.88.20"
PORT = 8080

mensaje = input("Gracias").encode("ascii")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(mensaje)
    data = s.recv(1024)

print(f"Recibido {data!r}")