import sys
from random import randint

def verify():
	print()
	ccnum = str(input("Please enter the number to be verified [16 digits]: "))

	if(len(ccnum) != 16):
		print("Error: Invalid length")
		exit()
	else:
		total = 0
		for x in range(1, 16, 2):
			print(x)
			total += int(ccnum[x])
		for y in range(0, 15, 2):
			print(y)
			if(int(ccnum[y]) * 2 > 9):
				total += ((int(ccnum[y]) * 2) - 9)
			else:
				total += int(ccnum[y]) * 2
		print(total)
		if total % 10 != 0:
			print("Card isn't valid")
		else:
			print("Card passes luhn test")
def check():
	print
	ccnum = str(input("Please enter CC number: "))	
	if(ccnum[0:2] == "34" or ccnum[0:2] == "37"):
		print("Card may be from American Express")
	if(ccnum[0:4] == "6759" or ccnum[0:6] == "676770" or ccnum[0:6] == "676774" or ccnum[0:2] == "50" or (int(ccnum[0:2]) >55 and int(ccnum[0:2]) < 70)):
		print("Card may be from Maestro")
	if((int(ccnum[0:4]) > 2220 and int(ccnum[0:4]) < 2721) or (int(ccnum[0:2]) > 50 and int(ccnum[0:2]) < 56)):
		print("Card may be from Mastercard")
	if(int(ccnum[0:1]) == 4):
		print("Card may be from Visa")

def checksum():
	partial = str(input("Please enter 12 digits: "))
	if(len(partial) != 12):
		print("Error: incorrect length")
	else:
		a = randint(0, 10)
		b = randint(0, 10)
		c = randint(0, 10)
		partial += str(a) + str(b) + str(c)
		total = 0
		for x in range(1, 14, 2):
			total += int(partial[x])
		for x in range(0, 15, 2):
			if(int(partial[x]) * 2 < 10):
				total += int(partial[x]) * 2
			else:
				total += (int(partial[x]) * 2) - 9
		partial += str(10 - total % 10)
		print(partial)
def randomnum():
	print("")
	print("#################################################")
	print("#                                               #")
	print("#  1. Maestro                                   #")
	print("#  2. Mastercard                                #")
	print("#  3. Visa                                      #")
	print("#                                               #")
	print("#################################################")
	print("")
	choice = input("Please make a choice [1-3]: ")
	print("")
	if choice == 1:
		num = str(randint(56, 70))
		while(len(num) != 15):
			num += str(randint(0,10))
		total = 0
		for x in range(1, 14, 2):
			total += int(num[x])
		for x in range(0, 15, 2):
			if(int(num[x]) * 2 > 9):
				total = (int(num[x]) * 2) - 9
			else:
				total = int(num[x]) * 2
		num += str(10 - (total % 10))
		print num
	if choice == 2:
		num = str(randint(51, 56))
		while(len(num) != 15):
                        num += str(randint(0,10))
                total = 0
                for x in range(1, 14, 2):
                        total += int(num[x])
                for x in range(0, 15, 2):
                        if(int(num[x]) * 2 > 9):
                                total = (int(num[x]) * 2) - 9
                        else:
                                total = int(num[x]) * 2
                num += str(10 - (total % 10))
                print num
	if choice == 3:
		num = "4"
		while(len(num) != 15):
                        num += str(randint(0,10))
                total = 0
                for x in range(1, 14, 2):
                        total += int(num[x])
                for x in range(0, 15, 2):
                        if(int(num[x]) * 2 > 9):
                                total = (int(num[x]) * 2) - 9
                        else:
                                total = int(num[x]) * 2
                num += str(10 - (total % 10))
                print num


if __name__ == "__main__":
	print("#################################################")
	print("#                                               #")
	print("#  1. Verify a card number	               #")
	print("#  2. Check the vendor			       #")
	print("#  3. Generate the checksum                     #")
	print("#  4. Generate a random credit card number      #")
	print("#					       #")
	print("#################################################")
	print("")
	choice = input("Please select your choice [1-4]: ")

	if(choice == 1):
		verify()
	elif(choice == 2):
		check()
	elif(choice == 3):
		checksum()
	elif(choice == 4):
		randomnum()
