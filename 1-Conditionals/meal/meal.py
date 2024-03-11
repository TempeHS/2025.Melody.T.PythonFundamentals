"""
prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time
7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00
"""


def main():
    time = input("What time is it? ")
    hours, minutes = time.split(":")
    hours = float(hours)
    if 7.00 <= hours <= 8.00:
        print("time for brekkie")
    elif 12.00 <= hours <= 13.00:
        print("time for lunch")
    elif 18.00 <= hours <= 19.00:
        print("time for dinner")
    else:
        print("nothing")


main()
