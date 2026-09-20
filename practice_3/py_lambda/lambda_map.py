# Here is lambda used with map to convert celsius temps to fahrenheit 
celsius_temps = [0, 10, 20, 30]
fahrenheit_temps = list(map(lambda c: c * 9/5 + 32, celsius_temps))
print(fahrenheit_temps)