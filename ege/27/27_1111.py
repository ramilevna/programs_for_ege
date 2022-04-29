ost = [0] * 1111
x = []
n = 1000
s = 0
ans = 0
for i in range(101):
    x.append(int(input()))
    s += x[i]
if s % 1111 == 0:
    ans += 1
    #ost[0] = 1

s1 = 0
s1 += x[0]
ost[s1 % 1111] += 1
k = 1
#ost[0] = 1
for i in range(101, n):
    a = int(input())
    s += a
    if s % 1111 == 0:
        ans += 1
    ans += ost[s % 1111]
    s1 += x[i-100]
    ost[s1 % 1111] += 1
    x.append(a)

