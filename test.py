def is_num(number):
    sum = 0
    num = int(number)
    for i in str(number):
        sum += int(i) ** 3
        if num == sum:
            return num
        else:
            continue
for i in range(100,1000):
    if is_num(i):
        print(i)