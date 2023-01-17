pre_1 = 0
pre_2 = 1

for _ in range(30):
    pre_1, pre_2 = pre_2, pre_1+pre_2
    print(pre_1, end=" ")