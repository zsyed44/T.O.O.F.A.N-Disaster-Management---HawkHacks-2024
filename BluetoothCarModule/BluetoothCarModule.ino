
#define CUSTOM_SETTINGS
#define INCLUDE_GAMEPAD_MODULE
#include <DabbleESP32.h>

// Control two left wheels
int motorOnePinOne = 12;
int motorOnePinTwo = 14;

// Control two right wheels
int motorTwoPinOne = 26;
int motorTwoPinTwo = 27;

void setUpPinModes()
{
  pinMode(motorOnePinOne,OUTPUT);
  pinMode(motorOnePinTwo,OUTPUT);
  
  pinMode(motorTwoPinOne,OUTPUT);
  pinMode(motorTwoPinTwo,OUTPUT);
}

void setup()
{
  setUpPinModes();
  Dabble.begin("Batmobile"); 
}

void loop()
{
  Dabble.processInput();
  if (GamePad.isLeftPressed())
  {
    // TURN LEFT
    digitalWrite(motorOnePinOne, HIGH);
    digitalWrite(motorOnePinTwo, LOW);
    digitalWrite(motorTwoPinOne, HIGH);
    digitalWrite(motorTwoPinTwo, LOW);
  }

  else if (GamePad.isRightPressed())
  {
    // TURN RIGHT
    digitalWrite(motorOnePinOne, LOW);
    digitalWrite(motorOnePinTwo, HIGH);
    digitalWrite(motorTwoPinOne, LOW);
    digitalWrite(motorTwoPinTwo, HIGH);
  }

  else if (GamePad.isDownPressed())
  {
    // MOVE BACKWARDS
    digitalWrite(motorOnePinOne, LOW);
    digitalWrite(motorOnePinTwo, HIGH);
    digitalWrite(motorTwoPinOne, HIGH);
    digitalWrite(motorTwoPinTwo, LOW);
  }

  else if (GamePad.isUpPressed())
  {
    // MOVE BACKWARDS
    digitalWrite(motorOnePinOne, HIGH);
    digitalWrite(motorOnePinTwo, LOW);
    digitalWrite(motorTwoPinOne, LOW);
    digitalWrite(motorTwoPinTwo, HIGH);
  }

  else{
    // STOP
    digitalWrite(motorOnePinOne, LOW);
    digitalWrite(motorOnePinTwo, LOW);
    digitalWrite(motorTwoPinOne, LOW);
    digitalWrite(motorTwoPinTwo, LOW);
  }

}
