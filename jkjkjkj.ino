#include <PRIZM.h>

PRIZM prizm;

void setup() {
  Serial.begin(9600);
  prizm.PrizmBegin();
}

void loop() {
  if(Serial.available()){
    char a=Serial.read();
    if(a=='1') Serial.println("1");
    else Serial.println("?");
  }
}
