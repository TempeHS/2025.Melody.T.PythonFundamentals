class Studen: ...


print("bonk")


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


# class
def get_student():
    student = Studen()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student


# if __name__ == "__main__":
main()
