import socket
import constants

host , port = constants.IP_SERVER , constants.PORT

def listen():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR , 1)
    serversocket.bind((host , port))
    serversocket.listen(1)
    print('servidor en el puerto',port)
    return serversocket


def temp(serversocket):
    while True:
        connection , address = serversocket.accept()
        request = connection.recv(1024).decode('utf-8')
        print("//////////////x1"+request+"//////////////")
        string_list = request.split(' ')

        if request == "":
            temp(serversocket)


        requesting_file = string_list[1]

        print("/////////x2"+requesting_file+"/////////")


        print('Client request',requesting_file)

        myfile = requesting_file.split('?')[0]
        myfile = myfile.lstrip('/')

        if(myfile == ''):
            myfile = 'index.html'
        try:
            file = open(myfile , 'rb')
            response = file.read()
            file.close()

            header = 'HTTP/1.1 200 OK\n'

            if(myfile.endswith('.jpg')):
                mimetype = 'image/jpg'
            else:
                mimetype = 'text/html'

            header += 'Content-Type: '+str(mimetype)+'\n\n'

            final_response = header.encode('utf-8')
            final_response += response
            send(connection,final_response)

        except Exception as e:
            print("-")
            header = 'HTTP/1.1 404 Not Found\n\n'
            response = '<html><body>Error 404: File not found</body></html>'.encode('utf-8')
            send(connection,response)


def send(connection,final_response):
    connection.send(final_response)
    connection.close()



if __name__ == '__main__':
    soc = listen()
    temp(soc)