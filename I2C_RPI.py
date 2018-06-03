import smbus
import time

bus=smbus.SMBus(1)

address=0x04

while True:
    
    num=int(input('input number:'))
    
    bus.write_byte(address, num)
    
    print(bus.read_byte(address))
