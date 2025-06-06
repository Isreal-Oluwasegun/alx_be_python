def perform_operation(num1, num2, operation):
    result = 0
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide' and num2 == 0:
        result = 'Cannot divide by zero'
    elif operation == 'divide':
        result = num1/num2
    return f'Result: {result}'

print(perform_operation(20, 0, 'divide'))
        