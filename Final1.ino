#include <PRIZM.h>
const int TriggerPin = 2; //Trig pin
const int EchoPin = 9; //Echo pin
long Duration = 0;
PRIZM prizm;

void setup() {
  Serial.begin(9600);
  pinMode(TriggerPin, OUTPUT); // Trigger is an output pin
  pinMode(EchoPin, INPUT); // Echo is an input pin
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
  Duration = pulseIn(EchoPin, HIGH);
  return Distance(Duration); 
}
long Distance(long time){
  long DistanceCalc = ((time / 2.9) / 2); // Actual calculation in mm
  return DistanceCalc; // return calculated value
}

void goforward(int stp){
  prizm.setMotorPower(2, -15);
  delay(400);
  int pcnt=0, cnt=0, cont=0;
  while(1){
    long dist = getdist();
    Serial.println(dist);
    if(dist < 100){
      pcnt++;
      cont = 1;
    }
    else if( cont ){
      cont = 0;
      pcnt = 0;
    }
    if(pcnt==10){
      cnt++;
      pcnt=0;
      cont=0;
      if(cnt==stp){
        prizm.setMotorPower(2, 0);
        delay(100);
        prizm.setServoPosition(1, 60);
        delay(1000);
        prizm.setServoPosition(1, 0);
        delay(1000);
        return;
      }
      delay(800);
    }
  }
}

void gobackward(int stp){
  prizm.setMotorPower(2, 15);
  delay(400);
  int pcnt=0, cnt=0, cont=0;
  while(1){
    long dist = getdist();
    if(dist < 100){
      pcnt++;
      cont = 1;
    }
    else if( cont ){
      cont = 0;
      pcnt = 0;
    }
    if(pcnt==10){
      cnt++;
      pcnt=0;
      cont=0;
      if(cnt==stp){
        delay(100);
        prizm.setMotorPower(2, 0);
        return;
      }
      delay(800);
    }
  }
}

void loop() {
  goforward(3);
  gobackward(4);
  delay(3000);
  goforward(2);
  gobackward(3);
  prizm.PrizmEnd();
}

