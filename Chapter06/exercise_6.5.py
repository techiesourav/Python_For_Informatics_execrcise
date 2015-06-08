# Exercise 6.5

# Exercise 6.5 Take the following Python code that stores a string:
#
#					str = 'X-DSPAM-Confidence: 0.8475'
#
#			Use find and string slicing to extract the portion of the string after the colon
#			character and then use the float function to convert the extracted string into a
#			floating point number.

str = 'X-DSPAM-Confidence: 0.8475'

delimiter = ':'
start_index = str.find(delimiter)

# assuming the float goes all the way till end of the string

substring = str[ start_index+1: ]

#remove any possbile trainling space ot TAB

substring_final = substring.rstrip()

try:
	float_num = float(substring_final)
	print "The float value is %g" % float_num
except:
	print "There is some issue in extracting th floating point number."
