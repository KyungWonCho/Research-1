import serial

ser=serial.Serial('/dev/ttyUSB2',9600)
print("2".encode("ascii"))
ser.write(b'2')