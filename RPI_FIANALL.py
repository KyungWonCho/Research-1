import serial
import socket
import picamera
import time
import io
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
ser=serial.Serial('/dev/ttyUSB2',9600)
HOST = ''
PORT = 2048
BUFSIZE = 1024

camera = PiCamera()

while True:
    while True:
        button=GPIO.input(18)
        if button == False:
            break;
    
    camera.start_preview()
    sleep(2)
    camera.capture('img.jpg')
    camera.stop_preview()

    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))

    with open('img.jpg', 'rb') as inf:
        jpgdata=inf.read()

    while jpgdata:
        senddata = jpgdata[:BUFSIZE]
        jpgdata=jpgdata[BUFSIZE:]
        conn.send(senddata)

    cmd = conn.recv(BUFSIZE)
    cmd=cmd.decode('utf-8')
    
    ser.write(cmd.encode('ascii'))
