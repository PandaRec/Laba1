login = input()
email = input()
if login.find("@") != -1:
    print("Некорректный логин")
elif email.find("@") == -1:
    print("Некорректный адрес")
else:
    print("OK")
