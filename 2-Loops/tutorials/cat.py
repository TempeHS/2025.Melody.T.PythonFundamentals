def main():
    number = get_number()
    meow(number)


def get_number(n):
    while True:
        n = input("What's n? ")
        if n > 0:
            break
    return n


def meow(n):
    for _ in range(n):
        print("meow")


"""
count = 0
while count < 3:
    print("meow")
    count = count + 1
"""

"""
for i in [0, 1, 2]:
    print("meow")
"""
