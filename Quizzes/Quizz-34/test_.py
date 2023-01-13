import script

class quizz34:
    def __init__(self, num:int):
        self.num = num
        print("You have created a new object")
    def solve(self)->str:
        return script.numbertoroman(self.num)

case1 = quizz34(1)
solution1 = case1.solve()
print(solution1)