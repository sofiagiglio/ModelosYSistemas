# echo-client.py

import socket
HOST = "192.168.88.45"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
mensaje = input("Graciasty").encode("ascii")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(mensaje)
    data = s.recv(1024)

print(f"Received {data!r}")