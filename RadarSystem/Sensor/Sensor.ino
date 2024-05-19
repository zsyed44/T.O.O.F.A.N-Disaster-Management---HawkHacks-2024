// Many credits to The Indian Hacker on youtube, the code is heavilly based off his provided RADAR Code

// A LINK TO HIS GOOGLE DRIVE CODES ARE GIVEN BELOW!
// https://drive.google.com/drive/folders/0BwsV1jJYW9dnenRYYXRneUtLcnM?resourcekey=0-axsBFCosolW_5i1X1cXRVw


#include <Servo.h> 

const int trigPin = 10;
const int echoPin = 11;
const int servoPin = 12;

long duration;
int distance;
Servo myServo;

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Serial.begin(9600);
  myServo.attach(servoPin); 
}

void loop() {
  // rotates the servo motor from 15 to 165 degrees
  for(int i=15;i<=165;i++){  
  myServo.write(i);
  delay(30);
  distance = calculateDistance();
  
  Serial.print(i);
  Serial.print(","); 
  Serial.print(distance); 
  Serial.print("."); 
  
  for(int i=165;i>15;i--){  
    myServo.write(i);
    delay(30);
    distance = calculateDistance();
    Serial.print(i);
    Serial.print(",");
    Serial.print(distance);
    Serial.print(".");
  }
  
}

int calculateDistance(){ 
  
  digitalWrite(trigPin, LOW); 
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH); 
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distance= duration*0.034/2;
  return distance;
}
