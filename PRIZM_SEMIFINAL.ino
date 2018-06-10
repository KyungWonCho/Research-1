#include <PRIZM.h>
#include <Wire.h>

#define SLAVE_ADDRESS 0x04

PRIZM prizm;

void setup() {
  Wire.begin(SLAVE_ADDRESS);
  Wire.onReceive(receiveData);
  prizm.PrizmBegin();
}

void loop() {
  delay(100);
}

void move(int time){
  prizm.setMotorPower(1, 50);
  delay(time);
  prizm.setMotorPower(1, 125);
  delay(time);
  prizm.setMotorPower(1, -50);
  delay(time);
  prizm.setMotorPower(1, 125);
}

void receiveData(int byteCount){
  int num=Wire.read();
  switch(num){
  case 1:
    move(600);
    break;
  case 2:
    move(800);
    break;
  case 3:
    move(1000);
    break;
  case 4:
    move(1200);
    break;
  }
}
