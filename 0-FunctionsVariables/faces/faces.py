def main():
    noses = input("Convert an emoticon: ")
    convert(noses)


def convert(para):
    print(para.replace(":)", "🙂"))
    print(para.replace(":(", "🙁"))


main()
