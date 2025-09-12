#include <OneWire.h>
#include <DallasTemperature.h>

// Pin del sensor DS18B20
#define ONE_WIRE_BUS 16

// Setup del bus 1-Wire
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

// Pin del ventilador
int fan = 15;

// Temperaturas de control
int tempMin = 25; // temp mínima para arrancar fan
int tempMax = 29; // temp máxima para fan al 100%

void setup() {
  pinMode(fan, OUTPUT);
  sensors.begin();
  Serial.begin(9600);
}

void loop() {
  sensors.requestTemperatures(); // lee temperatura
  float temp = sensors.getTempCByIndex(0); // obtiene temperatura en °C
  int fanSpeed = 0;

  Serial.print("Temp: ");
  Serial.println(temp);

  if(temp < tempMin) {
    // Fan apagado
    fanSpeed = 0;
  } 
  else if(temp >= tempMin && temp <= tempMax) {
    // Fan proporcional a la temperatura
    fanSpeed = map(temp, tempMin, tempMax, 0, 255); // PWM 0-255
  } 
  else if(temp > tempMax) {
    // Fan al máximo
    fanSpeed = 255;
  }

  analogWrite(fan, fanSpeed); // controla la velocidad del ventilador
  //Serial.println(fanSpeed);
  delay(500); // espera medio segundo antes de nueva lectura
}

