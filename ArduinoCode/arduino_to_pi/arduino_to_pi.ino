
#include <DHT.h>

// Pin Definitions for Temperature Sensors
#define R1DHTPIN 2   // Pin which is connected to the DHT22 sensor
#define R2DHTPIN 3   // Pin which is connected to the DHT11 sensor
#define R3DHTPIN 4   // Pin which is connected to the DHT11 sensor
#define R4DHTPIN 5   // Pin which is connected to the DHT11 sensor
#define OUTDHTPIN 6   // Pin which is connected to the DHT11 sensor
#define R1DHT DHT11  // DHT22 sensor type
#define R2DHT DHT11  // DHT11 sensor type
#define R3DHT DHT11  // DHT11 sensor type
#define R4DHT DHT11  // DHT11 sensor type
#define OUTDHT DHT11  // DHT11 sensor type

// Declaring DHT Types
DHT r1(R1DHTPIN, R1DHT);
DHT r2(R2DHTPIN, R2DHT);
DHT r3(R3DHTPIN, R3DHT);
DHT r4(R4DHTPIN, R4DHT);
DHT out(OUTDHTPIN, OUTDHT);


void setup() {
  // Initialize serial communication at 9600 baud
  Serial.begin(9600);
  // Initialize DHT sensors
  r1.begin();
  r2.begin();
  r3.begin();
  r4.begin();
  out.begin();
}

void loop() {

  // Read Temperature in Celsius
  float R1Temp = (r1.readTemperature()) * (9/5.0) + 32;
  float R2Temp = (r2.readTemperature()) * (9/5.0) + 32;
  float R3Temp = (r3.readTemperature()) * (9/5.0) + 32;
  float R4Temp = (r4.readTemperature()) * (9/5.0) + 32;
  float OUTTemp = (out.readTemperature()) * (9/5.0) + 32;

  Serial.println(String(R1Temp) + "," + String(R2Temp) + "," + String(R3Temp) + "," + String(R4Temp) + "," + String(OUTTemp));
}
