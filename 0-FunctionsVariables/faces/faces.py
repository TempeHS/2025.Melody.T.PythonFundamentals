def convert(parameter):
    parameter = parameter.replace(":)", "🙂")
    parameter = parameter.replace(":(", "🙁")
    return parameter


def main():
    given = input("Convert an emoticon: ")
    print(convert(given))


main()
