#Find PI to the Nth Digit Using Gauss Legendre algorithm

from __future__ import division
import math

def square(x):
	return x*x

#Algorithm initial setting via Wikipedia
a = 1
b = 1/(math.sqrt(2)) 
t = 1/4
p = 1

print ('Enter the number of digits you want to find Pi to(less than 20 please):')
user_choice = raw_input()
if(int(user_choice) < 20):
	for i in user_choice:
		y = a
		a = (a+b)/2
		b = math.sqrt(y*b)
		t = t - p * square(y-a)
		p = 2*p
		
pi = (square(a+b))/(4*t)
print pi


