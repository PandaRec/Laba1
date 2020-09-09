width = int(input())
height = int(input())
symbol = input()
for i in range(height):
    for j in range(width):
        if i == 0 or i == height - 1:
            print(symbol, end="")
        elif j == 0 or j == width - 1:
            print(symbol, end="")
        else:
            print(" ", end="")
    print()
