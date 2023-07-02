#! /usr/env python

data = [1, 2, 3, 4, 5, 6, 7, 8, 10, 13, 30, 45]
while True:
    n = int(input('Enter element to search :'))
    lo = 0
    u = len(data)
    mid = 0
    for i in range(len(data)):
        if lo <= u:
            mid = (lo + u) // 2
            if data[mid] == n:
                res = data[mid]
                print(f'{data[mid]} Found at {data.index(res)}')
                break
            else:
                if data[mid] < n:
                    lo = mid
                else:
                    u = mid
        i += 1
    else:
        print('Element not in list')
