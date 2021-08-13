def seidel(a, x, b):
    n = len(a)
    for j in range(0, n):
        d = b[j]
        for i in range(0, n):
            if(j != i):
                d -= a[j][i] * x[i]
        x[j] = d / a[j][j]
    return x


n = 3
a = []
b = []
x = [0, 0, 0]
a = [[5, -1, 1], [1, 6, 1], [1, 1, -8]]
b = [2, 12, 11]
print(x)


for i in range(0, 25):
    x = seidel(a, x, b)
    print(x)
