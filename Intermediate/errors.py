def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None
    except TypeError as e:
        raise ValueError(f"Bad input: {e}")
    else:
        return result
    finally:
        print("Attempted division")
