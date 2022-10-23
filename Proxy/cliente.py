
import socket
import constants

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def main():
    print('***********************************')
    print('Client is running...')
    client_socket.connect((constants.IP_SERVER,constants.PORT))
    local_tuple = client_socket.getsockname()
    print('Connected to the server from:', local_tuple)
    print('Enter \"quit\" to exit')
    print('Input commands:')
    command_to_send = input()

    while command_to_send != constants.QUIT:

      if command_to_send == '':
            print('Please input a valid command...')
            command_to_send = input()                                   
      else:        
            client_socket.send(bytes(command_to_send,constants.ENCONDING_FORMAT))
            data_received = client_socket.recv(constants.RECV_BUFFER_SIZE)        
            print(data_received.decode(constants.ENCONDING_FORMAT))
            command_to_send = input()
        
    close(command_to_send)

  
def close(command_to_send):
  client_socket.send(bytes(command_to_send,constants.ENCONDING_FORMAT))
  data_received = client_socket.recv(constants.RECV_BUFFER_SIZE)        
  print(data_received.decode(constants.ENCONDING_FORMAT))
  print('Closing connection...BYE BYE...')
  client_socket.close() 

if __name__ == '__main__':
    main()