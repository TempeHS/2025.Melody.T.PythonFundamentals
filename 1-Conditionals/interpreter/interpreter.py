# prompts the user for an arithmetic expression and outputs result as a floating-point value

expression = input("Calculate: ")
x, y, z = expression.split(" ")

if y == "+":
    result = float(x) + float(z)
elif y == "-":
    result = float(x) - float(z)
elif y == "*":
    result = float(x) * float(z)
elif y == "/":
    result = float(x) / float(z)

print("Your answer is", (result))
