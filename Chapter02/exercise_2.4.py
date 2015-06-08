# Exercise 2.4

# Exercise 2.4 Assume that we execute the following assignment statements:
#
#		width = 17
#		height = 12.0
#
#		For each of the following expressions, write the value of the expression and the
#		type (of the value of the expression).
#
#		1. width/2
#		2. width/2.0
#		3. height/3
#		4. 1 + 2 * 5		

# Ans ::  Writing python script file insteard of using chevron prompt

width = 17
height = 12.0

# First Expression

val1 = width/2
type1 =  type(val1)

print "Case 1: The value " + str(val1) + " is of  " + str(type1)

# Second Expression

val2 = width/2.0
type2 =  type(val2)

print "Case 2: The value " + str(val2) + " is of  " + str(type2)

# Third Expression

val3 = height/3
type3 =  type(val3)

print "Case 3: The value " + str(val3) + " is of  " + str(type3)

# Fourth Expression

val4 = 1 + 2 * 5
type4 =  type(val4)

print "Case 4: The value " + str(val4) + " is of  " + str(type4)
