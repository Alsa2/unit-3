# Quizz 35

## Code:
    
```python
class Person:
    def __init__(self, name:str, age:int):
        self.name = name
        if not isinstance(age, int):
            raise TypeError("Age must be an integer")
        self.age = age
        print("Person created")

    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    
class Student(Person):
    def __init__(self, name:str, age:int, grade:int):
        super().__init__(name = name , age = age)
        if not isinstance(grade, int):
            raise TypeError("Grade must be an integer")
        self.grade = grade
        print("Student created")
    
    def get_grade(self):
        return self.grade

class Classroom(Student):
    def __init__(self, name:str, age:int, grade:int, class_name:str):
        super().__init__(name = name , age = age, grade = grade)
        self.class_name = class_name
        print("Classroom created")
    def get_class_name(self):
        return self.class_name
    def get_number_students(self):
        return len(self.name)
    def add_student(self, name:str, age:int, grade:int, class_name:str):
        self.name = name
        self.age = age
        self.grade = grade
        self.class_name = class_name
        return self.name, self.age, self.grade, self.class_name
    def remove_student(self, name:str, age:int, grade:int, class_name:str):
        self.name = name
        self.age = age
        self.grade = grade
        self.class_name = class_name
        return self.name, self.age, self.grade, self.class_name
    def average_grade(self):
        return sum(self.grade) / len(self.grade)
```
## Proof:

![](/Images/quizz36-proof.png)