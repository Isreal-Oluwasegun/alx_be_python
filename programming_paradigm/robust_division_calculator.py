def safe_divide(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except TypeError:
        print("Error: Please enter numeric values only.")
    else:
        print("The result of the division is {result}")
