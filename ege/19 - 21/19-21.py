def f(x, y, p):
    if x + y >= 223 or p > 3:
        return p == 3
    if p % 2 == 0:
        return f(x + 1, y, p + 1) or f(x, y + 1, p + 1) or f(x * 2, y, p + 1) or f(x, y * 2, p + 1)
    elif p % 2 == 1:
        return f(x + 1, y, p + 1) and f(x, y + 1, p + 1) and f(x * 2, y, p + 1) and f(x, y * 2, p + 1)


for s in range(1, 206):
    if f(17, s, 1):
        print(s)