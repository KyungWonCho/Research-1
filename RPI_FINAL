import smbus
import time
import socket
from picamera import PiCamera
import io

bus=smbus.SMBus(1)

address=0x04

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

conn.close()
sock.close()

PORT=5031

sock = socket.socket(socket.AF_INET, socket. SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(1)

conn, addr = sock.accept()

bcmd = conn.recv(BUFSIZE)

cmd = int(bcmd.decode('utf-8'))

bus.write_byte(address, cmd)

sleep(5)

conn.close()
sock.close()
