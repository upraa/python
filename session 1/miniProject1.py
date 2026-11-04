F_name = input("Enter your first name: ")
L_name = input("Enter your last name: ")
age = int(input("Enter your age: "))
job = input("Enter your field of work: ")
salary = float(input("Enter your monthly salary: "))

tax = salary * 0.10
net_salary = salary - tax

print(f""" {"*"*15} Salary Report {"*"*15}
{"="*45}

First Name: {F_name}    ||   Age: {age}
Last Name: {L_name}     ||   Field of Work: {job} 

{"="*45}

Monthly Salary: {salary:,.2f}
Tax (10%): {tax:,.2f}
Net Salary: {net_salary:,.2f}

{"="*45}

{"*"*10} Employee Information {"*"*10}
Please keep your information private.
{"*"*45}""")