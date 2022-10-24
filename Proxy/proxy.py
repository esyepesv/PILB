import socket 
import constants


host , port =  constants.IP_SERVER, constants.PORT

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def listen():
    serversocket.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR , 1)
    serversocket.bind((host , port))
    serversocket.listen(1)
    print('servidor en el puerto',port)

    received = True
    while received:
        connection , address = serversocket.accept()
        request = connection.recv(1024).decode('utf-8')
        print(request)
        send(request)
        received = False

def send(command_to_send):
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect((constants.IP_SERVER,constants.PORT2))
    
    if command_to_send == '':
        print('Please input a valid command...')
    else:        
        clientsocket.send(bytes(command_to_send,constants.ENCONDING_FORMAT))
        data_received = clientsocket.recv(constants.RECV_BUFFER_SIZE)        
        print(data_received.decode(constants.ENCONDING_FORMAT))

if __name__ == '__main__':
    listen()