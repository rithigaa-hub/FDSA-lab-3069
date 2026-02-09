def cal_average(num):
    total = 0
    for i in num:
        total += i
    return total / len(num)

print("The average is", cal_average([18, 25, 3, 41, 5]))
