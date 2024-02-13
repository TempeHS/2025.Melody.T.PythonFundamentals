# ask user for name
name = input("What's your name? ")
name = name.strip().title()

# split name into first & last
first, last = name.split(" ")

# say hello to user
print(f"hello, {first}")
