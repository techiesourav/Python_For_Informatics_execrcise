
# Assignment 6.1

#Exercise 6.1 Write a while loop that starts at the last character in the string and
#               works its way backwards to the first character in the string, printing each letter on
#               a separate line, except backwards.

# same example, using negative index


input = 'Late Goodbye'
length = len(input)
neg_index = 1

while(neg_index <= length):
    print input[-neg_index]
    neg_index = neg_index + 1
