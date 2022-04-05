for ss in range(2, 10):
    k = 0
    a = 50
    while a != 0:
        k += 1
        a = a // ss
    if k == 3:
        print(ss)