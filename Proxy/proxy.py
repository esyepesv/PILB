import socket 
import constants
import logging
import time


host , port =  constants.IP_SERVER, constants.PORT
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
logging.basicConfig(filename = 'Register.log', format="%(asctime)s %(levelname)s %(message)s",  level = 'INFO')



def main():
    serversocket.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR , 1)
    serversocket.bind((host , port))
    serversocket.listen(1)
    print('servidor en el puerto',port)
    ip_index = 0
    while True:
        connection , address = serversocket.accept()
        request = connection.recv(1024).decode('utf-8')
        print(address)

        #log
        print(request)
        logging.info('Consulta: %r\n recibida en el puerto: %r\n',request, port)

       
        data_received = send(request, ip_index)
        print(data_received)
        response = data_received
       #response = str(data_received.decode(constants.ENCONDING_FORMAT))
        #connection.send(response.encode(constants.ENCONDING_FORMAT))
        connection.send(response)
        #log
        print(response)
        logging.info('respuesta: %r\n enviada por el puerto: %r\n', response, port)

        #cambio de server
        ip_index+=1 if ip_index < len(constants.IP_SERVERS)-1 else 0

    


def send(command_to_send, ip_index):
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect((constants.IP_SERVERS[0],constants.PORT))
    
    if command_to_send == '':
        print('Please input a valid command...')
    else:        
        clientsocket.send(bytes(command_to_send,constants.ENCONDING_FORMAT))
        data_received = clientsocket.recv(constants.RECV_BUFFER_SIZE)        
        #print(data_received.decode(constants.ENCONDING_FORMAT))

        return data_received


if __name__ == '__main__':
    main()