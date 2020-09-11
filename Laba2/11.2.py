count_of_rows = int(input())
for i in range(count_of_rows):
    temp_str = input()
    if len(temp_str) >= 2:
        if temp_str[0] == '%' and temp_str[1] == '%':
            print(temp_str[2:])
        elif len(temp_str) >= 4:
            if temp_str[0] != '#' and temp_str[1] != '#' and temp_str[2] != '#' and temp_str[3] != '#':
                print(temp_str)
        else:
            print(temp_str)
    else:
        print(temp_str)
