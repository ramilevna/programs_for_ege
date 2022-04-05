for a in range(10 ** 3, 0, -1):
    k = 0
    for x in range(0, 100):
        for y in range(0, 100):
            if ((x <= 9) <= (x * x <= a)) and ((y * y <= a) <= (y <= 9)):
                k += 1
    if k == 100 * 100:
        print(a)
        break
