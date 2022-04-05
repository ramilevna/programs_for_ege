f = open('26.txt','r')
n = int(f.readline())
a = []
k = 0
sum = 0
for i in range(n):
    s = f.readline().split()
    a.append((int(s[0]),int(s[1])))
for i in range(n - 1):
    for j in range(i + 1, n):
        if a[i][0] >= 1634515200 or a[i][0] == 0:
            if a[i] == a[j]:
                k += 1
                sum += (a[i][1]-a[i][0]) * 2
print(k, sum)