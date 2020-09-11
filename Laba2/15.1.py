symbol = input()
row = input().split()
for i in row:
    if symbol in i.lower():
        print(i)
