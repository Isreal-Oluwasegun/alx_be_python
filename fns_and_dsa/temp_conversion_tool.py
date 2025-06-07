FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
  temp = (fahrenheit - 32 ) * FAHRENHEIT_TO_CELSIUS_FACTOR
  return f'{fahrenheit}\N{DEGREE SIGN}F is {temp}\N{DEGREE SIGN}C'

def convert_to_fahrenheit(celsius):
  temp = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
  return f'{celsius}\N{DEGREE SIGN}C is {temp}\N{DEGREE SIGN}F'



temperature = input("Enter the temperature to convert: ")
try:
     temperature = float(temperature)
except:
     print("Invalid temperature. Please enter a numeric value.")
else:
    options = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
    if options == "C":
        print(convert_to_fahrenheit(temperature))
    elif options == "F":
        print(convert_to_celsius(temperature))
    else:
        print("Invalid unit.")
        
