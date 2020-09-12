count_of_rows = int(input())
numbers = []
for i in range(count_of_rows):
    numbers.append(int(input()))
numbers.sort(reverse=True)
for i in numbers:
    print(i)
