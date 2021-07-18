float R_series = 10e3;  // Known value of resistor in series with 2-terminal sensor.

float V_1;

float I;
float V_sens;
float R_sens;

void setup()
{
    Serial.begin(9600);   // Open communication with a computer via USB or with another device via UART.
}
void loop()
{
    V_1 = analogRead(1);  // Measured voltage across series resistor.
    
    I = V_1 / R_series;   // Calculated current through both series resistor and 2-terminal sensor.
    V_sens = 5 - V_1;     // Calculated voltage across 2-terminal sensor.
    R_sens = V_sens / I;  // Calculated resistance of 2-terminal sensor.
    
    Serial.println(R_sens);
}
