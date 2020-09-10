columns = int(input())
rows = int(input())
for i in range(rows):
    for j in range(columns):
        print(float((j + 1) / (i + 1)), end=" ")
    print()
