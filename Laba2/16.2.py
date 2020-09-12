# правильно ли я понял задание вообще
count_of_sentence = int(input())
arr = []
to_print = []
for i in range(count_of_sentence):
    row = input()
    arr.append([])
    arr[i].append(row.split(','))
count_of_print = int(input())
for i in range(count_of_print):
    to_print.append(input())
for i in range(count_of_print):
    aa = int(to_print[i].split(',')[0])
    bb = int(to_print[i].split(',')[1])

    print(arr[int(to_print[i].split(',')[0])][0][int(to_print[i].split(',')[1])])
