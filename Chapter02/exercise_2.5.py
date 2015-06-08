# Exercise 2.5

# Exercise 2.5 Write a program which prompts the user for a Celsius temperature,
#				convert the temperature to Fahrenheit and print out the converted temperature.

# need to import sys module to use the exit() method
import sys

def ask_user_input():
	inp = raw_input("Enter the temparature in Celsius : ")
	try:
		inp_float = float(inp)
	except:
		print "The input is not a number"
		sys.exit(0)
	
	return inp_float
	

cel = ask_user_input()
farenheit = ((cel * 9.0) / 5.0 ) + 32
 
print "%g celsius is equal to %g farenheit"% (cel, farenheit)
