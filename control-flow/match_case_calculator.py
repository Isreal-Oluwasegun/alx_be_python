num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
operation = input("Choose the operation (+, -, *, /): ")
result = 0
match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/" if num2 == 0: 
        result = "Cannot divide by zero"
    case "/":
        result = num1/num2
print(f"The result is {result}")
    