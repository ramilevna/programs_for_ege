a = [0] * (68 * 5)
for i in range(68 * 5):
    if i + 1 >= 68 or i + 4 >= 68 or i * 5 >= 68:
        a[i] = 1
while a[1] == 0:
    for i in range(68):
        if a[i] == 0:
            if a[i + 1] > 0 and a[i + 4] > 0 and a[i * 5] > 0:
                a[i] = - max(a[i + 1], a[i + 4], a[i * 5])
            elif a[i + 1] < 0 or a[i + 4] < 0 or a[i * 5] < 0:
                a[i] = -min(a[i + 1], a[i + 4], a[i * 5]) + 1
for i in range(68):
    if a[i] == -2:
        print(i)