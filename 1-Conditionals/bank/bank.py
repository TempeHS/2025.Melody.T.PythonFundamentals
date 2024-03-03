#  prompts the user for a greeting. “hello”, output $0. starts with an “h”, output $20. Otherwise, output $100.
# Ignore whitespace, case-insensitively.

payment = input("Greet me: ").lower().strip()

if payment.startswith("hello"):
    print("$0")
elif payment.startswith("h"):
    print("$20")
else:
    print("$200")
