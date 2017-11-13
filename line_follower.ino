int enableLeft = 11, enableRight =6 , leftMotorFront = 12, leftMotorBack = 13, rightMotorFront = 8, rightMotorBack = 7;

void front(){
  digitalWrite(leftMotorFront,HIGH); 
  digitalWrite(leftMotorBack,LOW);
  digitalWrite(rightMotorFront,HIGH);
  digitalWrite(rightMotorBack,LOW);
}

void back(){
  digitalWrite(leftMotorFront,LOW);
  digitalWrite(leftMotorBack,HIGH);
  digitalWrite(rightMotorFront,LOW);
  digitalWrite(rightMotorBack,HIGH);
}

void left(){
  digitalWrite(leftMotorFront,LOW);
  digitalWrite(leftMotorBack,HIGH);
  digitalWrite(rightMotorFront,HIGH); 
  digitalWrite(rightMotorBack,LOW);
}

void right(){
  digitalWrite(leftMotorFront,HIGH);
  digitalWrite(leftMotorBack,LOW);
  digitalWrite(rightMotorFront,LOW);
  digitalWrite(rightMotorBack,HIGH);
}

void botStop(){
  digitalWrite(leftMotorFront,LOW);
  digitalWrite(leftMotorBack,LOW);
  digitalWrite(rightMotorFront,LOW);
  digitalWrite(rightMotorBack,LOW);

  
}

void setup() {
  Serial.begin(9600);
  pinMode(leftMotorFront,OUTPUT);
  pinMode(leftMotorBack,OUTPUT);
  pinMode(rightMotorFront,OUTPUT);
  pinMode(rightMotorBack,OUTPUT);
  pinMode(enableLeft,OUTPUT);
  pinMode(enableRight,OUTPUT);
  
  analogWrite(enableLeft,255);
  analogWrite(enableRight,255);
 
  
}

int x=0;
void loop(){
while (Serial.available() == 0); 
 // read the incoming byte:
 x = Serial.read();
 
 // say what you got:
 Serial.print("I got: "); // ASCII printable characters
 Serial.println(x, DEC);
  if(x==49) right();
  else if(x==50) front();
  else if(x==51) left();
  else if(x==52) back();
  else botStop();
  
while(Serial.available()>0) Serial.read();
}








