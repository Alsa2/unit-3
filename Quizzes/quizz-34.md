# Quizz 34

## Code:

```python
def numbertoroman(a:int)->str:
    b = []
    for i in str(a):
        b.append(i)
    out = ""
    dictionary = {1:"I", 2:"II", 3:"III", 4:"IV", 5:"V", 6:"VI", 7:"VII", 8:"VIII", 9:"IX", 10: "X", 20:"XX", 30:"XXX", 40:"XL", 50:"L", 60:"LX", 70:"LXX", 80:"LXXX", 90:"XC", 100:"C"}
    if len(b) == 1:
        out = dictionary[int(b[0])]
    elif len(b) == 2:
        out = dictionary[int(b[0])*10] + dictionary[int(b[1])]
    elif len(b) == 3:
        out = dictionary[int(b[0])] + "C" + dictionary[int(b[1])*10] + dictionary[int(b[2])]


print(numbertoroman(input()))
```

## Proof:

![](/Images/quizz34-proof.png)