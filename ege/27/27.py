f = open('C:\\Users\\renat\\Downloads\\27-B.txt', 'r')
a = list(map(int, f.readlines()))
a.sort(reverse=True)
num0 = []
num1 = []
num2 = []
for i in range(len(a)):
    if a[i] % 3 == 0:
        num0.append(a[i])
        if len(num0) == 3:
            break
for i in range(len(a)):
    if a[i] % 3 == 1:
        num1.append(a[i])
        if len(num1) == 3:
            break
for i in range(len(a)):
    if a[i] % 3 == 2:
        num2.append(a[i])
        if len(num2) == 3:
            break
print(max(sum(num0), sum(num1), sum(num2), (num0[0] + num1[0] + num2[0])))