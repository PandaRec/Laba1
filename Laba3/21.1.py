a = [77, 'abc']


def from_string_to_list(row, a):
    temp = row.split()
    for i in temp:
        a.append(int(i))


from_string_to_list('', a)
print(*a)
