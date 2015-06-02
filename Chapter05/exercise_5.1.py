#exercise 5.1

#define a function to ask for user input and validation

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
