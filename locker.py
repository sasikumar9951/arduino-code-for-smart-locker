#include <Servo.h>

// Define pins
const int relayPin = 7;   // Relay control pin
Servo servoMotor;         // Servo motor

void setup() {
  // Initialize serial communication
  Serial.begin(9600);

  // Initialize relay pin as output
  pinMode(relayPin, OUTPUT);
  digitalWrite(relayPin, LOW); // Initially lock is OFF

  // Attach servo to pin
  servoMotor.attach(9);
  servoMotor.write(0); // Initial position of servo lock

  Serial.println("System ready...");
}

void loop() {
  // Listen for commands via Serial/ESP8266
  if (Serial.available()) {
    String command = Serial.readStringUntil('\n');
    command.trim();  // Remove extra spaces/newlines

    if (command == "UNLOCK") {
      digitalWrite(relayPin, HIGH);  // Activate solenoid lock
      servoMotor.write(90);          // Unlock using servo (optional)
      Serial.println("Locker unlocked");
    } else if (command == "LOCK") {
      digitalWrite(relayPin, LOW);   // Deactivate solenoid lock
      servoMotor.write(0);           // Lock position using servo
      Serial.println("Locker locked");
    }
  }
}




