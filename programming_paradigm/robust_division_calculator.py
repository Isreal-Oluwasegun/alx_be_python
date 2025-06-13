def safe_divide(numerator, denominator):
    try:
        result = numerator / denominator
    except:
        return "Cannot divide by zero"
