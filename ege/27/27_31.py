f = open('C:\\Users\\renat\\Downloads\\27-B.txt','r')
n = int(f.readline())
ost = [0]*30
s = 0
k = 0
mx = 0
for i in range(n):
    a = int(f.readline())
    s += a
    if a % 2 == 0 and a > 0:
        k += 1
    if k % 30 == 0:
        mx = max(s, mx)
    if not(ost[k % 30]):
        ost[k % 30] = s
    else:
        mx = max(mx, s - ost[k % 30])
        ost[k % 30] = min(s, ost[k % 30])
print(mx)



# Дана последовательность целых чисел. Необходимо найти максимально возможную сумму её непрерывной
# подпоследовательности, в которой количество положительных чётных элементов кратно k = 30.
