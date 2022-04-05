for s1 in range(10**4, 0, -1):
    s = s1
    s = s // 10
    n = 1
    while s < 51:
        s = s + 5
        n = n * 2
    if n == 64:
        print(s1)
        break