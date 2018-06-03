#include <PRIZM.h>
#include <Wire.h>

#define SLAVE_ADDRESS 0x04

int number;
int state=0;
PRIZM prizm;

void setup() {
  Serial.begin(9600);
  Wire.begin(SLAVE_ADDRESS);
  Wire.onReceive(receiveData);
  Wire.onRequest(sendData);
  prizm.PrizmBegin();
}

void loop() {
  delay(100);
}

void receiveData(int byteCount){
  int num=Wire.read();
  Serial.println(num);
  
  number=0;

  if(num==1) number=1;
  
}

void sendData(){
  Wire.write(number);
}

