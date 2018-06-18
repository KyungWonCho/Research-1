#include <PRIZM.h>
const int TriggerPin = 2;
const int EchoPin = 9;

PRIZM prizm;

void setup(){
  Serial.begin(9600);
  pinMode(TriggerPin, OUTPUT);
  pinMode(EchoPin, INPUT);
  prizm.PrizmBegin();
  prizm.setServoPosition(1, 0);
  prizm.setServoSpeed(1, 2);
  delay(1000);
  prizm.setServoSpeed(1, 30);
}

long getdist(){
  digitalWrite(TriggerPin, LOW);
  delayMicroseconds(2);
  digitalWrite(TriggerPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(TriggerPin, LOW);
  long time = pulseIn(EchoPin, HIGH);
  return (time/2.9)/2;
}

void drop(){
  prizm.setServoPosition(1, 60);
  delay(1000);
  prizm.setServoPosition(1, 0);
  delay(1000);
}
  

void move(int stp){
  prizm.setMotorPower(2, -15);
  delay(800);
  int pcnt=0, cnt=0, cont=0;
  while(cnt<stp){
    long dist=getdist();
    if(dist<60){
      pcnt++;
      cont=1;
    }
    else{
      cont=0;
      pcnt=0;
    }
    if(pcnt==10){
      cnt++;
      Serial.println(cnt);
      pcnt=0;
      cont=0;
      if(cnt==stp){
        prizm.setMotorPower(2, 0);
        delay(100);
        drop();
        break;
      }
      delay(1300);
    }
  }
  pcnt=cnt=cont=0;
  prizm.setMotorPower(2, 15);
  delay(800);
  while(cnt<stp+1){
    long dist=getdist();
    if(dist<60){
      pcnt++;
      cont=1;
    }
    else{
      cont=0;
      pcnt=0;
    }
    if(pcnt==10){
      cnt++;
      Serial.println(cnt);
      pcnt=0;
      cont=0;
      if(cnt==stp){
        prizm.setMotorPower(2, 0);
        delay(100);
      }
      delay(1300);
    }
  }
}

void loop(){
  if(Serial.available()){
    char cmd=Serial.read();
    int a=cmd-'0';
    Serial.println(a);
    move(a);
    Serial.write('1');
  }
}
