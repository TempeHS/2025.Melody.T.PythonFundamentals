# prompts the user for an arithmetic expression and outputs result as a floating-point value

expression = input("Calculate: ")
x, y, z = expression.split(" ")

if y == "+":
    print(x - z)

elif y == "-":
    print("hehe")
elif y == "*":
    print("hehe")
else:
    print("divide")
