count_of_rows=int(input())
rez_str=''
for i in range(count_of_rows):
    row=input()
    if not row.__contains__('лук'):
        rez_str+=row.join(', ')
print(rez_str[1:])