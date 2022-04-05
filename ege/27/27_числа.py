f = open('27-54a.txt', 'r')
n = int(f.readline())
k0 = []
k1 = []
k2 = []
k3 = []
for i in range(n):
    a = int(f.readline())
    if a % 4 == 0:
        k0.append(a)
    elif a % 4 == 1:
        k1.append(a)
    elif a % 4 == 2:
        k2.append(a)
    elif a % 4 == 3:
        k3.append(a)
k0 = sorted(k0, reverse=True)[:min(4, len(k0))]
k1 = sorted(k1, reverse=True)[:min(4, len(k1))]
k2 = sorted(k2, reverse=True)[:min(4, len(k2))]
k3 = sorted(k3, reverse=True)[:min(4, len(k3))]
k = k0 + k1 + k2 + k3
max = 0
for i in range(len(k)):
    for j in range(i + 1, len(k)):
        for m in range(j + 1, len(k)):
            for l in range(m + 1, len(k)):
                if k[i] + k[j] + k[m] + k[l] > max and (k[i] + k[j] + k[m] + k[l]) % 4 == 0:
                    max = k[i] + k[j] + k[m] + k[l]
print(max)