# prompts the user, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.

x = input(
    "What is the answer to the Great Question of Life, the Universe and Everything? "
)

if x == "42" or "forty-two" or "forty two":
    print("Yes")
else:
    print("No")
