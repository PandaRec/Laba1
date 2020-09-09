count_of_rows = int(input())
rows = list()
flag = False
for i in range(count_of_rows):
    rows.append(input())
for txt in rows:
    if txt.lower().__contains__("кот"):
        print("МЯУ")
        flag = True
        break
if not flag:
    print("нет")
