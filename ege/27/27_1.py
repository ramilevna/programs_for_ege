f = open('27-61a.txt','r')
n = int(f.readline())
a_cur = [0] * 100
a_copy = [0] * 100
for i in range(n):
    a = int(f.readline())
    for j in range(100):                # если min то + условие на == 0 , то записываем сумму
        if a_cur[(a_cur[j] + a) % 100] < a_cur[j] + a:
            a_copy[(a_cur[j] + a) % 100] = a_cur[j] + a
    a_cur = a_copy.copy()
print(a_cur[50])