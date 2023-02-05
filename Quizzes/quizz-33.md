# Quizz 33

## Code:
    
```python
def mystery(list1, list2):
    output = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                output.append(list1[i])
    return output


print(mystery([1, 2, 3], [3, 4, 5]))
```
## Proof:

![](/Images/quizz33-proof.png)