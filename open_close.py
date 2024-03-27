with open("myText.txt", "r") as file:
    lines = file.readlines()
for line in lines:
    line.rstrip()

file = open("myText.txt", "a")
file.write(lines + 1)
    
with open("myText.txt", "r") as file:
    lines = file.readlines()
for line in lines:
    line.rstrip()

	file.close()