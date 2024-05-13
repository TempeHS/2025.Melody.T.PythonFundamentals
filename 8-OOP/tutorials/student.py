def main():
    name, house = get_student()
    print(f"{name} from {house}")


def get_student():
    n = input("Name: ")
    h = input("House: ")
    return n, h


# if __name__ == "__main__":
main()
