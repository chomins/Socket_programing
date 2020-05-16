import socket

def connection(port_num):
    print("Student ID: 20150465")
    print("Name : Chominsu")
    host="localhost"
    port=int(port_num)
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind((host,port))
    sock.listen(5)
    while 1:
        print("ready")
        client_sock, client_addr = sock.accept()
        try:
            message = client_sock.recv(1024)
            filename = message.split()[1]
            f = open(filename[1:])
            print(filename[1:])
            
            f.close()
            client_sock.send('HTTP/1.0 200 OK\r\n\r\n')
            
            for i in f.readlines():
                client_sock.send(i)
            client_sock.close()
        except IOError:
            client_sock.send('404 Not Found')
            client_sock.close()
        sock.close() 
while 1:
    port=input()
    port=int(port)
    connection(port)

    
