rows = list()
flag = False
enter = input()
while enter != "Стоп":
    rows.append(enter)
    enter = input()
for i in range(len(rows)):
    if rows[i].lower().__contains__("кот"):
        print(i+1)
        flag = True
        break
if not flag:
    print("-1")
