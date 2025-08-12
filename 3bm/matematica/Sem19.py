#11/08
from scipy.constants import convert_temperature

TempCelsius = 20 

TempFahrenheit = convert_temperature(TempCelsius, 'Celsius', 'Fahrenheit')

print(f"{TempCelsius} graus celsius é equivalente a {TempFahrenheit:.2f} graus Fahrenheit")