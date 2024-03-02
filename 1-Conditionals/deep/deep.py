# prompts the user, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.

x = input(
    "What is the answer to the Great Question of Life, the Universe and Everything? "
)

match x:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")
