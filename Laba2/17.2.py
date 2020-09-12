count_of_phones=int(input())
dict={}
requests=[]
for i in range(count_of_phones):
    number_name=input()
    dict[number_name.split(' ')[0].strip()] = number_name.split(' ')[1].strip()
count_requests=int(input())
for i in range(count_requests):
    requests.append(input())
for i in range(count_requests):
    if requests[i] in dict.values():
        for j in dict:
            if dict[j].__eq__(requests[i]):
                print(j,end=' ')

        print()
    else:
        print('Нет в телефонной книге')
