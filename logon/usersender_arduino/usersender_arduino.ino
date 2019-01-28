#include <Keyboard.h>
int buttonPin = 9;  // Set a button to any pin

void setup()
{
  pinMode(buttonPin, INPUT);  // Set the button as an input
  digitalWrite(buttonPin, HIGH);  // Pull the button high
  Serial.begin(9600);     // opens serial port, sets data rate to 9600 bps
  Serial1.begin(9600);

}
int incomingByte = 0;   // for incoming serial data

void username(int num) {
      Keyboard.print("zcseguest");
      if (num < 10) Keyboard.write('0');
      Keyboard.println(String(num));
}
void password() {
  Keyboard.println("CSE2018b");
}


void loop()
{

  if (Serial1.available() > 0) {
    // read the incoming byte:
    incomingByte = Serial1.read();

    if (incomingByte > 0) {
      Serial.print("I received: ");
      Serial.println(incomingByte, DEC);

      incomingByte -= 1;

      username(incomingByte);
      delay(500);
      password();

      
      
    }
  }

  if (digitalRead(buttonPin) == 0)  // if the button goes low
  {
    Keyboard.write('z');  // send a 'z' to the computer via Keyboard HID
    delay(1000);  // delay so there aren't a kajillion z's
  }
}
