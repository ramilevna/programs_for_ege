for x1 in range(100, 10**3):
    x = x1
    L = 2*x-30
    M = 2*x+30
    while L != M:
        if L > M:
            L = L - M
        else:
            M = M - L
    if M == 30:
        print(x1)
        break