

//#include <ESP8266HTTPClient.h>
//#include <ArduinoJson.h>
//#include <ESP8266WiFi.h>
#include <DHT.h>
#include <Adafruit_Sensor.h>

#define DHTPIN 8
#define DHTTYPE DHT11

DHT dht(DHTPIN,DHTTYPE);
 
void setup() {
  Serial.begin(115200);
  // Inisialisasi koneksi WiFi
//  WiFi.begin("Arta jaya c02", "1231231234");
//  while (WiFi.status() != WL_CONNECTED) {
//    delay(1000);
//    Serial.println("Connecting to WiFi..");
//  }
//  Serial.println("Connected to WiFi");
 

}
 
void loop() {
  // Loop kosong
    // Baca nilai suhu dari sensor (contoh)

  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();
  float cahaya= analogRead(A0);
  if (!isnan(temperature)&!isnan(cahaya)){
    if (temperature<0){
    float tmp=temperature*-1;
    Serial.print("temperature = ");
    Serial.println(tmp);
    Serial.print("humidity = ");
    Serial.println(humidity);
    Serial.print("cahaya = ");
    Serial.println(cahaya);
      }else{
    float tmp=temperature*1;
    Serial.print("temperature = ");
    Serial.println(tmp);
    Serial.print("humidity = ");
    Serial.println(humidity);
    Serial.print("cahaya = ");
    Serial.println(cahaya);
      }
    }
    
    
  else{
    Serial.println("Data Tidak Ada");}

  delay(2000);
}
 
