
# Assignment 6.1

# Exercise 6.1 Write a while loop that starts at the last character in the string and
#               works its way backwards to the first character in the string, printing each letter on
#               a separate line, except backwards.


input = 'Late Goodbye'
length = len(input)

while(length):
    length = length -1
    print input[length]
    
