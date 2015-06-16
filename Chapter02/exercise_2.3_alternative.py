# Exercise 2.15, assignment 2.3

# Exercise 2.3 Write a program to prompt the user for hours and rate per hour to
#              compute gross pay.
#               Enter Hours: 35
#               Enter Rate: 2.75
#               Pay: 96.25


# We won't worry about making sure our pay has exactly two digits after the decimal
# place for now. If you want, you can play with the built-in Python round function
# to properly round the resulting pay to two decimal places.

# this program is basic, so does not perform any error checking
# the advanced version will do the same #TODO

hours = raw_input("Enter Hours: ")
rate = raw_input("Enter Rate: ")

# type conversion

hours = float(hours)
rate = float(rate)

pay = hours * rate

#usage of in-bulit round() function

#print upto two digit

paytwo = round (pay, 2)
print 'paytwo: ', paytwo
print str(type(paytwo))
print '\n'
#print upto one digit

payone = round (pay, 1)
print 'payone: ', payone
print str(type(payone))
print '\n'

#print upto three digit

paythree = round (pay, 3)
print 'paythree: ', paythree
print str(type(paythree))
print '\n'

#print upto zero digit

payzero = round (pay, 0)
print 'payzero: ', payzero
print str(type(payzero))
print '\n'

#print upto zero digit, ommitting the second argument itself

paynone = round (pay)
print 'paynone: ', paynone
print str(type(paynone))
print type(paynone).__name__   #alternate way to print the type as a string
print '\n'
