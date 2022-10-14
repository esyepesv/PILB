import socket 

host , port = '127.0.0.1' , 8080

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR , 1)
serversocket.bind((host , port))
serversocket.listen(1)
print('servidor en el puerto',port)

while True:
    connection , address = serversocket.accept()
    request = connection.recv(1024).decode('utf-8')
    print(request)