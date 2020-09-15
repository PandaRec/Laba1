# 1 0 o O l I
import string
import random


def generate_password(m=0):
    lower_case = 'abcdefghijkmnpqrstuvwxyz'
    upper_case = 'ABCDEFGHJKLMNPQRSTUVWXYZ'
    digits = '23456789'
    rez = random.choice(lower_case) + random.choice(upper_case) + random.choice(digits)

    all_symbols = lower_case + upper_case + digits

    for i in range(m - 3):
        rez += random.choice(all_symbols)
    return rez


def main(n, m):
    rez = []
    for i in range(n):
        rez.append(generate_password(m))
    return rez


print("Случайный пароль из 7 символов:", generate_password(7))
print("10 случайных паролей длиной 15 символов:")
print(*main(10, 15), sep="\n")
