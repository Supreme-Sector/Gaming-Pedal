int buttonPin = 8; //Button connected to pin 8

void setup() {
  Serial.begin(9600); //Begin serial interface at a baud rate of 9600
  pinMode(buttonPin,INPUT);  //Set pin 8 to INPUT
  
}



void loop() {
  if (digitalRead(buttonPin)==HIGH){
    Serial.write('P'); // Transmit P for "press"
    delay(10); //For debouncing
    while (digitalRead(buttonPin)); // Stays in this loop while the buttonPin is high
    Serial.write('R'); // Transmit R for "release"
  }

}
