import math

num_digit = int(raw_input("Enter # of digits you want\n "))

while num_digit > 20:
	print "Too Large"
	num_digit = int(raw_input("Enter # of digits you want\n"))
else:
	print '%.*f' % (num_digit, math.pi)