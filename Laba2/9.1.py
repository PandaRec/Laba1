home_books = list()
need_books = list()
count_home_books = int(input())
count_need_books = int(input())

for i in range(count_home_books):
    home_books.append(input())
for i in range(count_need_books):
    need_books.append(input())

for i in need_books:
    if i in home_books:
        print("YES")
    else:
        print("NO")
