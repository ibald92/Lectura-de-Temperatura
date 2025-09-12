#include <WiFi.h>
//funciona
const char* ssid = "wifi_name";
const char* password = "password";
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);

  WiFi.begin(ssid, password);

  while(WiFi.status() != WL_CONNECTED){
    delay(1000);
    Serial.println("Conectado a WIFI ...");
  }


  Serial.print("Conexión WIFI establecida");

  Serial.println("Direccion IP asignada: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  // put your main code here, to run repeatedly:


}
