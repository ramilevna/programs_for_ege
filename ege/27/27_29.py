f = open('27-A.txt','r')
n = int(f.readline())
arr = [0]*10
s = 0
k = 0
mx = 0
for i in range(n):
    a = int(f.readline())
    s += a
    if a % 2 == 0:
        k += 1
    if a % 2 == 0 and k < 10:
        arr[k] = s
    elif k >= 10:
        mx = max(mx, s - arr[k % 10])
print(mx)


# Дана последовательность натуральных чисел. Необходимо найти максимально возможную сумму её непрерывной
# подпоследовательности, в которой количество чётных элементов кратно k = 10.