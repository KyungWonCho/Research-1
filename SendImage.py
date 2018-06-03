import socket
from picamera import PiCamera
from time import sleep
import io

#  constant for socket
HOST = ''
PORT = 5030
BUFSIZE = 1024

# camera
camera = PiCamera()

camera.start_preview()
sleep(2)
camera.capture('img.jpg')
camera.stop_preview()

sleep(0.5)

sock = socket.socket(socket.AF_INET, socket. SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(1)

conn, addr = sock.accept()
print('Client address : ', addr)

with open('img.jpg', 'rb') as inf:
    jpgdata=inf.read()
    
while jpgdata:
    senddata = jpgdata[:BUFSIZE]
    jpgdata=jpgdata[BUFSIZE:]
    conn.send(senddata)

print('Send End')

conn.close()
sock.close()

PORT=5031

sock = socket.socket(socket.AF_INET, socket. SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(1)

conn, addr = sock.accept()

print('Client address : ', addr)

kind = conn.recv(BUFSIZE)

print('Message :', kind)

conn.close()
sock.close()


