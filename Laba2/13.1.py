count_of_thimbles = int(input())
thimbles = []
combinations = []
for i in range(count_of_thimbles):
    thimbles.append(input())
count_of_shifts = int(input())
for j in range(count_of_shifts):
    remain = int(input())
    if remain < len(thimbles):
        del thimbles[remain:]
    for i in range(remain):
        number = int(input())
        if str(i) + str(number - 1) not in combinations and str(number - 1) + str(i) not in combinations:
            thimbles[i], thimbles[number - 1] = thimbles[number - 1], thimbles[i]
            combinations.append(str(i) + str(number - 1))
    combinations = []
for i in thimbles:
    print(i)
