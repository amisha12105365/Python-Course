# Identify an Operator

num1 = int(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
num2 = int(input("Enter the second number: "))

if operator == "+":
    print("Addition:", num1 + num2)

elif operator == "-":
    print("Subtraction:", num1 - num2)

elif operator == "*":
    print("Multiplication:", num1 * num2)

elif operator == "/":
    print("Division:", num1 / num2)

else:
    print("Invalid operator!")