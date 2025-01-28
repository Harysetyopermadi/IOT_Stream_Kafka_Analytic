

#include <ESP8266HTTPClient.h>
#include <ArduinoJson.h>
#include <ESP8266WiFi.h>
#include <DHT.h>
#include <Adafruit_Sensor.h>

#define DHTPIN 4
#define DHTTYPE DHT11

DHT dht(DHTPIN,DHTTYPE);
 
void setup() {
  Serial.begin(115200);
  // Inisialisasi koneksi WiFi
  WiFi.begin("Arta jaya c02", "1231231234");
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi..");
  }
  Serial.println("Connected to WiFi");
 

}
 
void loop() {
  // Loop kosong
    // Baca nilai suhu dari sensor (contoh)

  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();
  float cahaya= analogRead(A0);
  // Buat objek JSON
  DynamicJsonDocument doc(200);
  doc["temperature"] = "27";
 
  // Konversi JSON ke string
  String data;
 
  // Buat objek HTTPClient
  HTTPClient http;
 
  // Tentukan alamat URL API
  http.begin("http://192.168.0.5:8080");
 

 
    Serial.print("temperature = ");
    Serial.println(temperature);
    Serial.print("humidity = ");
    Serial.println(humidity);
    Serial.print("cahaya = ");
    Serial.println(cahaya);
 
  if (!isnan(temperature)&!isnan(cahaya)){
      // Kirim permintaan POST dengan data JSON

        if (temperature<0){
    float tmp=temperature*-1;
      // Tambahkan header
  http.addHeader("Content-Type", "application/json");
  http.addHeader("temperature", String(tmp));
  http.addHeader("kelembaban", String(humidity));
  http.addHeader("cahaya", String(cahaya));
  http.addHeader("regional", "Jawa Timur");
  http.addHeader("name", "Channel_suhu_2");
    int httpResponseCode = http.POST(data);
    Serial.print("temperature = ");
    Serial.println(tmp);
    Serial.print("humidity = ");
    Serial.println(humidity);
    Serial.print("cahaya = ");
    Serial.println(cahaya);
                                      if (httpResponseCode > 0) {
                                        Serial.print("HTTP Response code: ");
                                        Serial.println(httpResponseCode);
                                        String payload = http.getString();
                                        Serial.println(payload);
                                      } else {
                                        Serial.print("Error code: ");
                                        Serial.println(httpResponseCode);
                                      }
      }else{
    float tmp=temperature*1;
      // Tambahkan header
  http.addHeader("Content-Type", "application/json");
  http.addHeader("temperature", String(tmp));
  http.addHeader("kelembaban", String(humidity));
  http.addHeader("cahaya", String(cahaya));
  http.addHeader("regional", "Jawa Timur");
  http.addHeader("name", "Channel_suhu_2");
    int httpResponseCode = http.POST(data);
    Serial.print("temperature = ");
    Serial.println(tmp);
    Serial.print("humidity = ");
    Serial.println(humidity);
    Serial.print("cahaya = ");
    Serial.println(cahaya);
                                      if (httpResponseCode > 0) {
                                        Serial.print("HTTP Response code: ");
                                        Serial.println(httpResponseCode);
                                        String payload = http.getString();
                                        Serial.println(payload);
                                      } else {
                                        Serial.print("Error code: ");
                                        Serial.println(httpResponseCode);
                                      }
      }
    }

    
                                        
    
    
    
  else{
    Serial.println("Data Tidak Ada");}
  // Cek kode respons

 
  // Akhiri sesi HTTP
  http.end();
  delay(5000);
}
 
