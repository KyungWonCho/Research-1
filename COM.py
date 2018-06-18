import io
import socket
import time

HOST = ''
PORT = 2048
BUFSIZE = 1024

sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock1.bind((HOST, PORT))
sock1.listen(5)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock2.bind((HOST, PORT+1))
sock2.listen(5)

while True:
    (conn, addr) = sock1.accept()
    print('connect: ', addr)

    jpgimg=b""

    while True:
        data=conn.recv(BUFSIZE)
        if not data:
            break
        jpgimg+=data

    conn.close()
    
    print('finish receiving')

    with open('img.jpg', 'wb') as inf:
        inf.write(jpgimg)

    a=int(input('type:'))
    a=str(a)
    
    (conn, addr) = sock2.accept()
    print('connect: ', addr)

    conn.send(a.encode('utf-8'))

    conn.close()
