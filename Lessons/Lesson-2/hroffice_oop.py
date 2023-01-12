class Employee:
    def __init__(self, name, mail, job, age, salary):
        self.name = name
        self.mail = mail
        self.job = job
        self.age = age
        self.salary = salary
    def greet(self):
       #(f"Hello {emp['name']}! You are {emp['age']} years old and you work as a {emp['job']} in our company. Your email address is {emp['mail']} and your salary is {emp['salary']}$ per year.")
        return(f"Hello {self.name}! You are {self.age} years old and you work as a {self.job} in our company. Your email address is {self.mail} and your salary is {self.salary}$ per year.")
    def getmail(self):
        return ("Your mail is: "+self.mail)

#create employees
Emp_1 = Employee(name="frank murphy", mail="frank.murphy@gmail.com", job="Driver", age=39, salary=30000)
Emp_2 = Employee(name="Joe Bidome", mail="joe.bidome@gmail.com", job="President", age=45, salary=50000)

db = [Emp_1, Emp_2]
for emp in db:
    print(emp.greet())
    print(emp.getmail())
