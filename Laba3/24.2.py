def decode_to_numbers(*args):
    rez = {}
    temp_sum = 0
    for i in args:
        for j in i:
            temp_sum += ord(j)
        if temp_sum in rez:
            rez[temp_sum] = [rez[temp_sum], i]
        else:
            rez[temp_sum] = i
        temp_sum = 0
    return rez


def print_by_geo(*args):
    rez = decode_to_numbers(*args)

    for i in rez:
        if type(rez[i]) != str:
            rez[i].sort()

    list_keys = list(rez.keys())
    list_keys.sort()
    for i in list_keys:
        if type(rez[i]) != str:
            for j in rez[i]:
                print(j)
        else:
            print(rez[i])


print_by_geo('mother', 'Daddy', 'sIster', 'abc', 'cba')
