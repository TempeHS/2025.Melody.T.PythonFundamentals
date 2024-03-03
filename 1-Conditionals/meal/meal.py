# prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time
# 7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00

def main():
	time = input("What time is it? ")
	hours, minutes = time.split(":")
	
    if 7.00 <= beep <= 8.00:
        print("brekkie")
	elif 12.00 <= beep <= 13.00:
        print("lunch")
	elif 18.00 <= beep <= 19.00:
        print("dinner")
	
def convert(time):
	beep = float(hours)
	boop = float(minutes / 60)
	
    



main()






