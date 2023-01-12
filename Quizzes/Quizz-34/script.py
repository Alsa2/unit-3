
def numbertoroman(a:int)->str:
    """
    if not isinstance(a, int):
        raise TypeError("Error: has to be int")
    if a >= 100:
        raise ValueError("Has to be less or equal to 100")
    """
    b = []
    for i in str(a):
        b.append(i)
    dictionary = {"1":"I", "2":"II", "3":"III", "4":"IV", "5":"V", "6":"VI", "7":"VII", "8":"VIII", "9":"IX", "10": "X", "50": "L", "100": "C"}
    result = ""
    for i in b:
        i = dictionary[i]
        result += i
    return result

print(numbertoroman(input()))
