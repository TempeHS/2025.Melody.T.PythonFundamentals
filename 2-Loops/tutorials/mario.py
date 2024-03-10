def main():
    print_square(3, 4)


def print_square(size, wid):
    # for the length of square
    for _ in range(size):
        # height of sqr
        for __ in range(wid):
            # print brick
            print("#", end="")
        # new line
        print()


main()
