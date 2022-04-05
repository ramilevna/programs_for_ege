from math import sqrt as sq

for i in range(35 * 10 ** 6, 40 * 10 ** 6 + 1):
    x = i
    while x % 2 == 0:
        x = x / 2
    sqrt = int(sq(sq(x)))
    if sqrt ** 4 == x:
        simple = True
        for j in range(3, int(sq(sqrt)) + 1):
            if sqrt % j == 0:
                simple = False
                break
        if simple:
            print(i)
