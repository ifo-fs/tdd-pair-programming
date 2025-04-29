def devide(a: int, b: int) -> float:
    if not a or (not b and b != 0):
        raise ValueError("arguments are required")

    return a / b
