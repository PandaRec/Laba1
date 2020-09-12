count_of_white_requests = int(input())
white_requests = []
requests = []

for i in range(count_of_white_requests):
    white_requests.append(input())

count_of_requests = int(input())

for i in range(count_of_requests):
    requests.append(input())

for i in requests:
    if i in white_requests:
        print(i)
