a = "ABABAABACACAC"
max = 0
k = 0
for i in range(len(a)):
    if a[i] == "A":
        for j in range(i, len(a) - 1, 2):
            if (a[j] == "A" and a[j + 1] == "B") or (a[j] == "A" and a[j + 1] == "C"):
                k += 1
            else:
                k = 0
                break
            if k > max:
                max = k
                k = 0
print(max)