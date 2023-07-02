data = [1, 2, 3, 4, 5, 7, 9, 10]

lwr = 0
upr = len(data)

ele = int(input('Enter a elemet to search :'))
for i in range(len(data)):
    if lwr <= upr:
        mid = (lwr + upr) // 2
        if data[mid] == ele:
            loc = data[mid]
            print(f'POSTION ={data.index(loc)}')
            break
        else:
            if data[mid] < ele:
                lwr = mid
            else:
                upr = mid
    i +=1
else:
    print('Element not found')

