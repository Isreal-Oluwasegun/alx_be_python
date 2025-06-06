def perform_operation(num1:float, num2:float, operation:str):
    result = 0
    match operation:
        case 'add':
            result = num1 + num2
        case 'subtract':
            result = num1 - num2
        case 'multiply':
            result = num1 * num2
        case 'divide' if num2 == 0:
            result = 'Cannot divide by zero'
        case 'divide':
            result = num1/num2
    return f'Result: {result}'

print(perform_operation(20, 10, 'subtract'))
        