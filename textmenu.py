# textmenu

x = True
while x == True:
    print("1. First Item", end="\n")
    print("2. Second Item", end="\n")
    print("3. Third item", end="\n")
    print("4. Exit", end="\n")
    w = input("What do you want to do? ")
    x = False

    if w == "1":
        print("You picked: the first item!")
        x = True

    if w == "2":
        print("You picked: the second item!")
        x = True

    if w == "3":
        print("You picked: the third item!")
        x = True

    if w == "4":
        print("You picked: Exit! Thank you for playing.")
