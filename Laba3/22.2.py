def partial_sums(*args):
    rez = []
    temp_sum = 0
    for i in range(len(args) + 1):
        for j in range(i):
            temp_sum += args[j]
        rez.append(temp_sum)
        temp_sum = 0
    return rez


print(partial_sums(13))
