float R_series = 10e3;        // Known value of resistor in series with 4-terminal sensor.

void setup()
{
  Serial.begin(9600);         // Open communication with a computer via USB or with another device via UART.
}
void loop()
{
  float V_1 = analogRead(1);  // Measured voltage across series resistor.
  float V_2 = analogRead(2);  // Measured voltage looking into the sensor at terminal `T2`.
  float V_3 = analogRead(3);  // Measured voltage looking into the sensor at terminal `T3`.

  float I = V_1 / R_series;   // Calculated current through both series resistor and sensor.
  float V_elem = V_3 - V_2;   // Calculated voltage across sensing element.
  float R_elem = V_elem / I;  // Calculated resistance of sensing element.

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
