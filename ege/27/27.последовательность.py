f = open('27-75a.txt', 'r')
n = int(f.readline())
a_cur = [(0, 0)] * 43
a_copy = [(0, 0)] * 43
a = int(f.readline())
a_cur[a % 43] = (1, a)
max, lenmin = 0, 0
for i in range(n - 1):
    a = int(f.readline())
    for j in range(43):
        if a_cur[j][1] != 0:        # можно убрать
            a_copy[(a_cur[j][1] + a) % 43] = (a_cur[j][0] + 1, a_cur[j][1] + a)
    if a_copy[a % 43][1] == 0:
        a_copy[a % 43] = (1, a)     # тоже можно убрать
    if a_copy[0][1] > max:
        max = a_copy[0][1]
        lenmin = a_copy[0][0]
    elif a_copy[0][1] == max and a_copy[0][0] < lenmin:
        lenmin = a_copy[0][0]
    a_cur = a_copy.copy()
    a_copy = [(0, 0)] * 43
print(lenmin, max)


# Дана последовательность из N натуральных чисел. Рассматриваются все её непрерывные подпоследовательности, такие что
# сумма элементов каждой из них кратна k = 43. Найдите среди них подпоследовательность с максимальной суммой, определите
# её длину. Если таких подпоследовательностей найдено несколько, в ответе укажите количество элементов самой короткой
# из них.