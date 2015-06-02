#exercise 5.1

# Exercise 5.1 Write a program which repeatedly reads numbers until the user enters
#              “done”. Once “done” is entered, print out the total, count, and average of
#               the numbers. If the user enters anything other than a number, detect their mistake
#               using try and except and print an error message and skip to the next number.

#### Sample Run, Input and output

#		Enter a number: 4
#		Enter a number: 5
#		Enter a number: bad data
#		Invalid input
#		Enter a number: 7
#		Enter a number: done
#		16 3 5.33333333333

def take_user_input():
	num = 0
	input = raw_input("Enter a Number:")
	if input == 'done':
		return -1
	try:
		num = float(input)
	except:
		print "Bad Data"
	return num
		
		
#### The main function body start here

sum = 0
counter = 0
average =0

while (1):

	temp = take_user_input();

	if temp > 0:
		sum += temp
		counter += 1
	elif temp != -1:
		continue
	else:
		break

try:
	average = sum / counter;
	print int(sum), counter, average
except:
	print "Nothing to do here, Goodbye!!!"
