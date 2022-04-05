f = open('26.txt','r')
k, m = map(int, f.readline().split())
s = []
for i in range(k):
    a = f.readline().split()
    s.append((int(a[0]),a[1]))
s.sort()
m1 = m
lasti = 0
for i in range(k):
    if m1 - s[i][0] >= 0:
        m1 -= s[i][0]
        lasti = i
    else:
        break
lasta = lasti
lastb = lasti + 1
while lasta >= 0 and lastb < n:
    while lasta >= 0 and s[lasta][1] != 'A':
        lasta -= 1
    while lastb < n and s[lastb][1] != 'B':
        lastb += 1
    if lasta >= 0 and lastb < n:
        if m -(m1 - s[lasta][0]) >= s[lastb][0]:
            m1 = m1 - s[lasta][0]
            lasta -= 1
            lastb += 1
b = 0
for i in range(lasti + 1):
    if s[i][1] == 'B':
        b += 1
print(b, m1)