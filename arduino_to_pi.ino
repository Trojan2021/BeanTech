#include <DHT.h>

// Pin Definitions for Temperature Sensors
#define R1DHTPIN 2      // Pin which is connected to the DHT22 sensor
#define R2DHTPIN 4      // Pin which is connected to the DHT11 sensor
#define R1DHT DHT22     // DHT22 sensor type
#define R2DHT DHT11     // DHT11 sensor type

// Declaring DHT Types
DHT r1(R1DHTPIN, R1DHT);
DHT r2(R2DHTPIN, R2DHT);

// Pin Definitions for Rotatory Encoder
#define outputA 8
#define outputB 9

// Pin Definitions for Photo Resistors
const int R1Photo = A0;
const int R2Photo = A1;

// Variables for Rotatory Encoder
int counter = 0, aState, aLastState;

void setup() {
  // Pin Modes for Rotatory Encoder
  pinMode(outputA, INPUT);
  pinMode(outputB, INPUT);
  // Initialize serial communication at 9600 baud
  Serial.begin(9600);
  // Initialize DHT sensors
  r1.begin();          
  r2.begin();
  // Reads the initial state of the outputA
  aLastState = digitalRead(outputA);   
}

void loop() {

  // Read Temperature in Celsius
  float R1Temp = r1.readTemperature();
  float R2Temp = r2.readTemperature();

  // Read Relative Humidity
  // float R1Hum = r1.readHumidity();
  // float R2Hum = r2.readHumidity();

  // Reading the value from the Photo Resistors
  int R1PhotoValue = analogRead(R1Photo);
  int R2PhotoValue = analogRead(R2Photo);

  aState = digitalRead(outputA); // Reads the "current" state of the outputA
   // If the previous and the current state of the outputA are different, that means a Pulse has occured
   if (aState != aLastState){     
     // If the outputB state is different to the outputA state, that means the encoder is rotating clockwise
     if (digitalRead(outputB) != aState) { 
       if (counter > 39) {
          counter = 0;
       } else {
          counter++;
       }
     } else {
       if (counter < 1) {
         counter = 40;
       } else {
         counter--;
       }
     }
   } 
  aLastState = aState; // Updates the previous state of the outputA with the current state

  Serial.print(R1Temp);
  Serial.print(",");
  Serial.print(R2Temp);
  Serial.print(",");
  Serial.print(R1PhotoValue);
  Serial.print(",");
  Serial.print(R2PhotoValue);
  Serial.print(",");
  Serial.println(counter);
  delay(50);
}
