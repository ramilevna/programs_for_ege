def f(x, finish):
    if x > finish:
        return 0
    if x == 29:
        return 0
    if x == finish:
        return 1
    if x < finish:
        return f(x + 1, finish) + f(x * 2, finish) + f(x * 3, finish)
print(f(2, 13))
