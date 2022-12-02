n = 33
a = []
count = 0
for i in range(2, n // 2):
    for j in range(2, i):
        if i % j == 0:
            count += 1
    if count == 0:
        a.append(i)
    count = 0
b = []
for i in range(len(a)):
    if n % a[i] == 0:
        b.append(a[i])
print(*b, "--- Это простые множители числа -->", n)





