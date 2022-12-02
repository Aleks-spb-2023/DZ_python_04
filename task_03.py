num = [1, 2, 6, 3, 7, 3, 2, 5, 7, 13, 3, 1, 54, 9, 13, 4]
num2 = []
for i in range(len(num)):
    if num[i] not in num2:
        num2.append(num[i])
print(num2)