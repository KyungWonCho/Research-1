import socket

HOST = '192.168.0.3'
PORT = 5030
BUFSIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

print('Connected to Server:', HOST, PORT)

f = open('imgcopy.jpg', 'w')

jpgimg=b""

while True:
    data = s.recv(BUFSIZE)
    if not data:
        break
    jpgimg+=data

print('Receive End')

with open('imgcopy.jpg', 'wb') as inf:
    inf.write(jpgimg)
    
print('Copying Image End')

f.close()
s.close()

PORT=5031

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

print('Connected to Server:', HOST, PORT)

message = input('Message to Send:')

s.send(message.encode())

print('Send End')

s.close()
