first_number = float(input())
second_number = float(input())
operation = input()
if operation.__eq__("-"):
    print(first_number - second_number)
elif operation.__eq__("+"):
    print(first_number + second_number)
elif operation.__eq__("/"):
    if second_number == 0:
        print("888888")
    else:
        print(first_number // second_number)

elif operation.__eq__("*"):
    print(first_number * second_number)
