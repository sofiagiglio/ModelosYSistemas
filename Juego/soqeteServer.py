import socket

listensocket = socket.socket() #Crea una instancia de socket
Port = 8080 #Port to host server on
maxConnections = 999
IP = '192.168.88.20'

listensocket.bind(('',Port))
listensocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#Inicia el servidor
listensocket.listen(maxConnections)
print("Server started at " + IP + " on port " + str(Port))

#Accepts the incomming connection
(clientsocket, address) = listensocket.accept()
print("New connection made!")

running = True

def funcion1():
    print("funcion1")

def funcion2():
    print("funcion2")
    
funciones_dic = {'f1':funcion1, 'f2':funcion2}

while running:
    message = clientsocket.recv(1024).decode() #Gets the incomming message
    if not message == "":
        funciones_dic[message]()