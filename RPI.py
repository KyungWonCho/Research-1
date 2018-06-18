import serial
import socket
import picamera
from time import sleep
import io
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
ser=serial.Serial('/dev/ttyUSB2',9600)
HOST = 'localhost'
PORT = 2048
BUFSIZE = 1024

camera = PiCamera()

try:
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
        print('connected')

        with open('img.jpg', 'rb') as inf:
            jpgdata=inf.read()

        print('finish reading')

        while jpgdata:
            senddata = jpgdata[:BUFSIZE]
            jpgdata=jpgdata[BUFSIZE:]
            sock.send(senddata)

        sock.close()

        print('finish sending')

        sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT+1))
        print('connected')

        cmd = sock.recv(BUFSIZE)

        sock.close()
        
        print(cmd)
        cmd=cmd.decode('utf-8')
        ser.write(cmd.encode('ascii'))
except Exception as excp:
    print(excp)
    sock.close()

