def main():
    input("Convert an emoticon: ")
    convert(given)


def convert(para):
    print(para.replace(":)", "🙂"))
    print(para.replace(":(", "🙁"))


main()
