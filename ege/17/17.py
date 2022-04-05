f = open('C:\\Users\\renat\\Downloads\\17 (6).txt', 'r')
arr = list(map(int, f.readlines()))
max = 0
k = 0
for i in range(len(arr) - 2):
    a = arr[i]
    b = arr[i + 1]
    c = arr[i + 2]
    if a ** 2 + b ** 2 > c ** 2 and b ** 2 + c ** 2 > a ** 2 and a ** 2 + c ** 2 > b ** 2:
        k += 1
        if a + b + c > max:
            max = a + b + c
print(k, max)
