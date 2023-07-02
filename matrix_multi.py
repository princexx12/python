
a = [
    [
        2, 6, 9
    ]
]

b = [
    [
        3, 7, 6
    ]
]

res = [
    [
        0, 0, 0
    ]
]

for i in range(len(a)):
    for j in range(len(a[0])):

        res[i][j] = a[i][j] * b[i][j]

for r in res:
    print(r)