FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_fahrenheit(celsius):
    CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
    fahrenheit=(CELSIUS_TO_FAHRENHEIT_FACTOR * celsius) + 32
    return f"{celsius}°C is {fahrenheit}°F"

def convert_to_celsius(fahrenheit):
    FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
    celsius = (fahrenheit - 32)*FAHRENHEIT_TO_CELSIUS_FACTOR  
    return f"{fahrenheit}°F is {celsius}°C"

temperature = input("Enter the temperature to convert: ")
try:
     temperature = float(temperature)
except:
     print("Invalid temperature. Please enter a numeric value.")
else:
    options = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
    if options == "C":
        print(convert_to_fahrenheit(temperature))
    elif options == "F":
        print(convert_to_celsius(temperature))
    else:
        print("Invalid unit.")
        
