const int pinoLuz = 8;
const int pinoSirene = 9;

void setup() {
  Serial.begin(9600);
  pinMode(pinoLuz, OUTPUT);
  pinMode(pinoSirene, OUTPUT);
  digitalWrite(pinoLuz, LOW);
  digitalWrite(pinoSirene, LOW);
}

void loop() {
  if (Serial.available() > 0) {
    char acao = Serial.read();
    if (acao == 'L') digitalWrite(pinoLuz, HIGH);
    if (acao == 'D') digitalWrite(pinoLuz, LOW);
    if (acao == 'S') {
      digitalWrite(pinoSirene, HIGH);
      delay(1000);
      digitalWrite(pinoSirene, LOW);
    }
  }
}