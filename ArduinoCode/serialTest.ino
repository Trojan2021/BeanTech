
int pi = 0;
void setup() {
  // put your setup code here, to run once:
  // Initialize serial communication at 9600 baud
  delay(10000);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0) {
    String incoming_data = Serial.readString();
    Serial.println("Recieved: " + incoming_data);
    String response = "Hello Python!";
    Serial.println(response);
  }

}
