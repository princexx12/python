#! /usr/env python
prime_number = []
from_interval = int(input('Enter from interval :'))
to_interval = int(input('Enter to interval :'))

for num in range(from_interval,to_interval+1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                prime_number.append(num)

print(f'Prime Number in {from_interval, to_interval}interval are :')
print(prime_number)
