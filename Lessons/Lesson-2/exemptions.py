def division(a:int, b:int)->float:
    if b== 0:
        raise ValueError("Cannot divide by 0")
    if not isinstance(a, int):
        raise TypeError("Error: a has to be int")
    if not isinstance(b, int):
        raise TypeError("Error: b has to be int")