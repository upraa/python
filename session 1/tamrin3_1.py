num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

num1 = float(num1)
num2 = float(num2)

print(f""" {"*"*15} Math Operations {"*"*15}
{"="*45}
First Number: {num1:,.2f}
Second Number: {num2:,.2f}
{"="*45}
Addition: {num1 + num2:,.2f}
Type: {type(num1 + num2)}
{"-"*45}
Subtraction: {num1 - num2:,.2f}
Type: {type(num1 - num2)}
{"-"*45}
Multiplication: {num1 * num2:,.2f}
Type: {type(num1 * num2)}
{"-"*45}
Division: {num1 / num2:,.2f}
Type: {type(num1 / num2)}
{"="*45}
{"*"*15} End of Report {"*"*15}""")