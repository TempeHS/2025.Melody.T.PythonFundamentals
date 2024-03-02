#  prompts the user for a greeting. “hello”, output $0. starts with an “h”, output $20. Otherwise, output $100.
# Ignore whitespace, case-insensitively.

payment = input("Greet me: ").lower

if payment == str.startswith("h"):
    print("$20")
elif payment == str.startswith("hello"):
    print("$0")
else:
    print("$200")
