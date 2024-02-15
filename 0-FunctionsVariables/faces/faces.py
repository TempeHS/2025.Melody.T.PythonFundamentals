def convert(parameter):
    print(parameter.replace(":)", "🙂"))
    print(parameter.replace(":(", "🙁"))


def main():
    given = input("Convert an emoticon: ")
    convert(given)


main()
