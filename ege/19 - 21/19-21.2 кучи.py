a = [[0] * 68  for i in range(5, 126)]
for i in range(5, 35):
    for j in range(1, 64):
        if i + 1 + j >= 69 or i * 2 + j >= 69 or j * 2 + i >= 69:
            a[i][j] = 1
while a[5][0] == 0:
    for i in range(5, 35):
        for j in range(1, 64):
            if a[i][j] == 0:
                if a[i + 1][j] > 0 and a[i][j + 1] > 0 and a[i * 2][j] > 0 and a[i][j * 2] > 0:
                    a[i][j] = - (max(a[i + 1][j], a[i][j + 1], a[i * 2][j], a[i][j * 2]))
                elif a[i + 1][j] < 0 or a[i][j + 1] < 0 or a[i * 2][j] < 0 or a[i][j * 2] < 0:
                    a[i][j] = - (min(a[i + 1][j], a[i][j + 1], a[i * 2][j], a[i][j * 2])) + 1
for i in range(5, 35):
    print(a[i][1:64])