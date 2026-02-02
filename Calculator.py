operator = input("Enter an operator (+ - * /): ")

try:
    num_1 = float(input("Enter the first number: "))
    num_2 = float(input("Enter the second number: "))
except ValueError:
    print("Please enter valid numbers.")
    exit()

if operator == "+":
    result = num_1 + num_2

elif operator == "-":
    result = num_1 - num_2

elif operator == "*":
    result = num_1 * num_2

elif operator == "/":
    if num_2 == 0:
        print("Error: Division by zero is not allowed.")
        exit()
    result = num_1 / num_2

else:
    print(f"'{operator}' is an invalid operator.")
    exit()

print("Result:", round(result, 2))
