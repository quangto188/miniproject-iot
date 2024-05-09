#include <DHT.h>

#define DHTPIN 4
#define DHTTYPE DHT22

DHT dht(DHTPIN, DHTTYPE);

const int switchPin = 3;
int counter_button = 0;
int counter_th = 0;
int previousState = HIGH;

void setup() {
  Serial.begin(115200);
  dht.begin();
  pinMode(switchPin, INPUT_PULLUP); 
}

void loop() {
  counter_button += 1;
  counter_th += 1;
  // Đọc trạng thái nút nhấn
  int currentState = digitalRead(switchPin);
  if (currentState != previousState) {
    Serial.print("!1:B:");
    Serial.print(currentState);
    Serial.print(":N:");
    Serial.print("None");
    Serial.print("#");
    Serial.println();
    previousState = currentState; 
  }
  // Gửi dữ liệu qua UART

  if (counter_th == 5000) {
    // Đọc dữ liệu từ cảm biến DHT22
    float humidity = dht.readHumidity();
    float temperature = dht.readTemperature();
    Serial.print("!1:T:");
    Serial.print(String(temperature, 1));
    Serial.print(":H:");
    Serial.print(String(humidity, 1));
    Serial.print("#");
    Serial.println();
    counter_th = 0;
  }
  delay(1);
}
