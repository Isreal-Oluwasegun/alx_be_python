def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        result = numerator / denominator
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
    except OverflowError:
        return "Error: Number too large to handle."
    except Exception as e:
        return f"Unexpected error: {str(e)}"
    else:
        return f"The result of the division is {result}"
safe_divide(12,6,7)