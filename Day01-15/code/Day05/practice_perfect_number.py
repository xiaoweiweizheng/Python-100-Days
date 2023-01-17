for num in range(10000):
    temp = 0
    for i in range(1, num//2+1):
        if num%i == 0:
            temp += i
    if num == temp:
        print(num, end=" ")