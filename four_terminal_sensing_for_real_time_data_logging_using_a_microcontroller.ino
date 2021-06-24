float R_series = 10e3;

void setup()
{
  Serial.begin(9600);
}
void loop()
{
  float V_1 = analogRead(1);
  float V_2 = analogRead(2);
  float V_3 = analogRead(3);

  float I = V_1 / R_series;
  float V_elem = V_3 - V_2;
  float R_elem = V_elem / I;

  Serial.print("R_elem:");
  Serial.print(R_elem);
  Serial.print("\t");

  Serial.print("lower:");
  Serial.print(0);
  Serial.print("\t");

  Serial.print("upper:");
  Serial.print(10e3);
  Serial.print("\n");
}
