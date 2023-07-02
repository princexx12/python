#! /usr/env python

num = int(input('Enter a number :'))
a = 0
b = 1

print(f'{a} \n{b}')
for i in range(2,num):
    c = a+b
    a = b
    b = c
    print(c)