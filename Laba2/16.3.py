count_of_rows = int(input())
bacterium = []
antibiotic = []
temp_arr = []
for i in range(count_of_rows):
    for j in range(count_of_rows):
        temp_arr.append(int(input()))
    bacterium.append(temp_arr)
    temp_arr = []
temp_arr = []
count_of_rows = int(input())
for i in range(count_of_rows):
    antibiotic.append([int(input()), int(input())])

for i in range(len (antibiotic)):
    bacterium[antibiotic[i][0]][antibiotic[i][1]] -= 8
    if (antibiotic[i][0] == 0 and antibiotic[i][1] == 0) or (
            antibiotic[i][0] == 0 and antibiotic[i][1] == len(bacterium[0])) or (
            antibiotic[i][0] == len(bacterium[0]) and antibiotic[i][1] == 0) or (
            antibiotic[i][0] == len(bacterium[0]) and antibiotic[i][1] == len(bacterium[0])):
        try:
            bacterium[antibiotic[i][0] + 1][antibiotic[i][1]] -= 4
        except:
            pass
        try:
            if antibiotic[i][0] - 1>=0:
                bacterium[antibiotic[i][0] - 1][antibiotic[i][1]] -= 4
        except:
            pass
        try:
            bacterium[antibiotic[i][0]][antibiotic[i][1] + 1] -= 4
        except:
            pass
        try:
            if antibiotic[i][1] - 1>=0:
                bacterium[antibiotic[i][0]][antibiotic[i][1] - 1] -= 4
        except:
            pass
        try:
            if antibiotic[i][0] - 1 >= 0 and antibiotic[i][1] - 1 >= 0:
                bacterium[antibiotic[i][0] - 1][antibiotic[i][1] - 1] -= 4
        except:
            pass
        try:
            if antibiotic[i][0] - 1 >= 0:
                bacterium[antibiotic[i][0] - 1][antibiotic[i][1] + 1] -= 4
        except:
            pass
        try:
            bacterium[antibiotic[i][0] + 1][antibiotic[i][1] + 1] -= 4
        except:
            pass
        try:
            if antibiotic[i][1] - 1 >= 0:
                bacterium[antibiotic[i][0] + 1][antibiotic[i][1] - 1] -= 4
        except:
            pass
        break

    try:
        bacterium[antibiotic[i][0] + 1][antibiotic[i][1]] -= 4
    except:
        pass
    try:
        if antibiotic[i][0] - 1 >= 0:
            bacterium[antibiotic[i][0] - 1][antibiotic[i][1]] -= 4
    except:
        pass
    try:
        bacterium[antibiotic[i][0]][antibiotic[i][1] + 1] -= 4
    except:
        pass
    try:
        if antibiotic[i][1] - 1 >= 0:
            bacterium[antibiotic[i][0]][antibiotic[i][1] - 1] -= 4
    except:
        pass
    try:
        if antibiotic[i][0] - 1 >= 0 and antibiotic[i][1] - 1>=0:
            bacterium[antibiotic[i][0] - 1][antibiotic[i][1] - 1] -= 4
    except:
        pass
    try:
        if antibiotic[i][0] - 1 >= 0:
            bacterium[antibiotic[i][0] - 1][antibiotic[i][1] + 1] -= 4
    except:
        pass
    try:
        bacterium[antibiotic[i][0] + 1][antibiotic[i][1] + 1] -= 4
    except:
        pass
    try:
        if antibiotic[i][1] - 1 >= 0:
            bacterium[antibiotic[i][0] + 1][antibiotic[i][1] - 1] -= 4
    except:
        pass

for i in range(len(bacterium)):
    for j in range(len(bacterium)):
        if bacterium[i][j]<0:
            bacterium[i][j]=0
        print(bacterium[i][j],end=' ')
    print()

