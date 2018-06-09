import socket

HOST = '192.168.25.45'
PORT = 4096
BUFSIZE = 1024
IMAGENUM = 1

while True:

    input("Take A Photo! Press Enter!")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    print('Connected to Server:', HOST, PORT)

    jpgimg=b""

    while True:
        data = s.recv(BUFSIZE)
        if not data:
            break
        jpgimg+=data

    print('Receive End')

    with open('img%d.jpg'%IMAGENUM, 'wb') as inf:
        inf.write(jpgimg)
        
    print('Copying Image End')

    s.close()

    PORT += 1
    IMAGENUM += 1
