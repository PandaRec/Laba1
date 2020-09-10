row = input()
number = int(input())
if number > len(row) or number < 0:
    print("ошибка")
else:
    print(row[number - 1])
