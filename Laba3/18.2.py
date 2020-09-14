def __ask_password():
    row = input()
    cc = 1
    while not row.__eq__('password') and cc < 3:
        row = input()
        cc += 1
    if cc <= 3 and row.__eq__('password'):
        print('Пароль принят')
        while True:
            input()
    else:
        print('В доступе отказано')
        while True:
            input()


__ask_password()
