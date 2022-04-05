f = open('27-26b.txt', 'r')
n = int(f.readline())
a_cur = [0] * 16
a, b = map(int, f.readline().split())
a_cur[a % 16] = a
a_cur[b % 16] = b
for i in range(n - 1):
    a, b = map(int, f.readline().split())
    a_copy = [0] * 16
    for j in range(16):
        if a_cur[j] != 0:
            sa = a_cur[j] + a
            sb = a_cur[j] + b
            if a_copy[sa % 16] == 0:
                a_copy[sa % 16] = sa
            elif a_copy[sa % 16] != 0 and sa < a_copy[sa % 16]:
                a_copy[sa % 16] = sa
            if a_copy[sb % 16] == 0:
                a_copy[sb % 16] = sb
            elif a_copy[sb % 16] != 0 and sb < a_copy[sb % 16]:
                a_copy[sb % 16] = sb
    a_cur = a_copy.copy()
print(a_cur[15])

# Имеется набор данных, состоящий из пар положительных целых чисел. Необходимо выбрать из каждой пары ровно одно число
# так, чтобы сумма всех выбранных чисел в шестнадцатеричной системе счисления оканчивалась на F и при этом была
# минимально возможной. Гарантируется, что искомую сумму получить можно. Программа должна напечатать одно число –
# минимально возможную сумму, соответствующую условиям задачи.