# Exercise 6.4

# Exercise 6.4 There is a string method called count that is similar to the function
#				in the previous exercise. Read the documentation of this method at docs.python.
#				org/library/string.html and write an invocation that counts the number of
#				times the letter a occurs in 'banana'.

word = 'banana'
searchFor = 'a'

count = word.count(searchFor)  #in-built metod invocation

print "The letter \"" +  searchFor + "\" appears " + str(count) + " times in the word " + word 
