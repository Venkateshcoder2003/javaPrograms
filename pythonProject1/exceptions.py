def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        result = None
    except TypeError:
        print("Error: Input values must be numbers.")
        result = None
    except Exception as e:
        print("An error occurred:", e)
        result = None
    finally:
        print("Division attempt completed.")

    return result


# Example usage
numerator =12
denominator = 2
result = divide(numerator, denominator)
if result is not None:
    print(f"Result of division: {result}")
