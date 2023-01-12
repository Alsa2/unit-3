Emp_1 ={
    "name": "frank murphy",
    "mail": "frank.murphy@company.xy",
    "job": "Driver",
    "age": 39,
    "salary": 30000
}
Emp_2 ={
    "name": "Joe Bidome",
    "mail": "joe.bidome@company.xy",
    "job": "President",
    "age": 45,
    "salary": 50000
}
Emp_3 ={
    "name": "Obama Prism",
    "mail": "obama.prism@company.xy",
    "job": "CEO",
    "age": 55,
    "salary": 100000
}
Emp_4 ={
    "name": "Trumpy Bumpy",
    "mail": "trumpy.bumpy@company.xy",
    "job": "CFO",
    "age": 50,
    "salary": 80000
}
Emp_5 ={
    "name": "Steve Jobs",
    "mail": "steve.jobs@company.xy",
    "job": "Dead",
    "age": 60,
    "salary": 0
}
emp_list = [Emp_1, Emp_2, Emp_3, Emp_4, Emp_5]

def greet(emp:list)->str:
    return(f"Hello {emp['name']}! You are {emp['age']} years old and you work as a {emp['job']} in our company. Your email address is {emp['mail']} and your salary is {emp['salary']}$ per year.")

name = input("Enter your name: ")
for i in emp_list:
    if name in i["name"]:
        print(greet(i))
        break
else:
    print("Employee not found")
