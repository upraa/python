# Session 2
F_name = input("Enter your first name: ")
L_name = input("Enter your last name: ")
age = int(input("Enter your age: "))
job = input("Enter your field of work: ")
salary = salary = float(input("enter your salary (toman): "))
children = int (input("enter num of children: "))

if salary >= 25000000 :
    tax = salary * 0.02
elif salary < 25000000 or salary < 15000000 :
    tax = salary * 0.01
else :
    tax = 0
if children >= 4:
    tax = tax - 50000


print(f""" {"*"*15} Salary Report {"*"*15}
{"="*45}

First Name: {F_name}    ||   Age: {age}
Last Name: {L_name}     ||   Field of Work: {job} 

{"="*45}

Monthly Salary: {salary - tax :,.2f} toman
Tax : {tax:,.2f} toman
Net Salary: {salary:,.2f} toman

{"="*45}

{"*"*10} Employee Information {"*"*10}
Please keep your information private.
{"*"*45}""")
