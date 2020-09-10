step = int(input())
row = input()
for i in row:
    if i == 'я' or i == 'Я':
        i = chr(ord('а') + step)
    elif 'А' <= i <= 'я':
        i = chr(ord(i) + step)
        print(i, end='')
    else:
        print(i, end='')
