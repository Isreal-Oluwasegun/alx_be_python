FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    temperature = FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)
    return f"{fahrenheit}°F is {temperature}°C"

def convert_to_fahrenheit(celsius):
    temperature = 32 +( CELSIUS_TO_FAHRENHEIT_FACTOR * celsius) 
    return f"{celsius}°C is {temperature}°F"


temperature = input("Enter the temperature to convert: ")
try:
     temperature = float(temperature)
except:
     print("Invalid temperature. Please enter a numeric value.")
else:
    options = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
    if options not in ("C","F"):
         print("Invalid unit.")
    else:
        if options == "C":
            print(convert_to_fahrenheit(temperature))
        elif options == "F":
            print(convert_to_celsius(temperature))
        else: 
            print("Invalid temperature. Please enter a numeric value.")