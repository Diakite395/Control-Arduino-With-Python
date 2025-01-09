const int pin1 = 2;
const int pin2 = 4;
String msg = "stop";

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(pin1, OUTPUT);
  pinMode(pin2, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0){
    msg = Serial.readString();
    msg.trim(); // Supprimer les espaces et retours à la ligne

  }

  if(msg == "ON"){
    digitalWrite(pin1, HIGH);
    Serial.println("Pin 1 activé");

  } else if(msg == "OFF"){
    digitalWrite(pin1, LOW);
    Serial.println("Pin 1 désactivé");

  }else if(msg == "stop"){
    digitalWrite(pin1, LOW);
    digitalWrite(pin2, LOW);

  }else{
    digitalWrite(pin1, LOW);

    Serial.println("Clignotement en cours...");

    for(int i=0; i<20; i++){
      digitalWrite(pin2, HIGH);
      delay(100);
      digitalWrite(pin2, LOW);
      delay(100);
    }

    Serial.println("Clignotement terminé");

    msg = "stop";
  }

}
