const int tachoPin = 16;
volatile unsigned long counter = 0;

void countPulses() {
  counter ++;
}

void setup() {
  Serial.begin(9600);
  attachInterrupt(digitalPinToInterrupt(tachoPin), countPulses, FALLING);
}

void loop() {
  delay(1000);
  long  rpm = counter * 60 / 2;
  Serial.print("RPM:");
  Serial.println(rpm);
  counter = 0;
}
