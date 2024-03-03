# prompts the user for an arithmetic expression and outputs result as a floating-point value

expression = input("Calculate: ")
x, y, z = expression.split(" ")

if y == "+":
    result = x + z

elif y == "-":
    result = x - z
elif y == "*":
    result = x * z
elif y == "/":
    result = x / z

print("Your answer is", result)
