#! /usr/env python

import cmath

a = int(input('Enter a number (>0) :'))
b = int(input('Enter a number :'))
c = int(input('Enter a number :'))

dis = a**2 + 4*a*c

root1 = (-b-cmath.sqrt(dis))/(2*a)
root2 = (-b+cmath.sqrt(dis))/(2*a)

print(f'the roots are {root1} and {root2}')