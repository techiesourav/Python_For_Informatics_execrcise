# Exercise 6.3

# The following program counts the number of times the letter a appears in a string:
#	word = 'banana'
#	count = 0
#	for letter in word:
#		if letter == 'a':
#			count = count + 1
#		print count

# This program demonstrates another pattern of computation called a counter. The
#	variable count is initialized to 0 and then incremented each time an a is found.
#	When the loop exits, count contains the result- the total number of a' s.

#	Exercise 6.3 Encapsulate this code in a function named count, and generalize it
#				so that it accepts the string and the letter as arguments.


#Generic function, accepting the string and the letter to search for

def count(str, let):
	count = 0
	for entry in str:
		if entry == let:
			count = count + 1
	
	return count
	
	
# main function, inputs are hardcoded, notu asked from user.

sentence = 'Is there anybody out there'
letterToSearch = 'e'
 
ret = count(sentence, letterToSearch)
 
print "The number of times [" + letterToSearch + "] occurs in (" + sentence + ") is " + str(ret)
