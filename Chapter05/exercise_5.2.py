# Assignment 5.2

# Exercise 5.2 Write another program that prompts for a list of numbers as above
#              and at the end prints out both the maximum and minimum of the numbers instead
#              of the average.

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
max = None
min = None

while (1):

	temp = take_user_input();

	if temp > 0:
		sum += temp
		counter += 1
		if max is None or temp > max:
			max = temp;
		if min is None or temp < min:
			min = temp;
	elif temp != -1:
		continue
	else:
		break

try:
#	average = sum / counter;
	print int(sum), counter, int(max) , int(min)
except:
	print "Nothing to do here, Goodbye!!!"
