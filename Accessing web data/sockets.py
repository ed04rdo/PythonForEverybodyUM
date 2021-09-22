import socket                                                           # socket library

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)              # declare socket
mysock.connect(('data.pr4e.org',80))                                    # connect socket passing address and port
cmd = "GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n".encode()        # request
mysock.send(cmd)                                                        # send request

while True:                                                             # receive data
    data = mysock.recv(512)                                             # receive up to 512 characters
    if len(data) < 1:                                                   # if we get no data, (EOF)
        break
    print(data.decode())                                                # decode received data            
mysock.close()                                                          # close socket