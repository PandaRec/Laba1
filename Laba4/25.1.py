# 1 0 o O l I
import string
import random


def generate_password(m=0):
    rez = ''
    all_symbols = string.ascii_letters + string.digits
    all_symbols = all_symbols.replace('O', '')
    all_symbols = all_symbols.replace('o', '')
    all_symbols = all_symbols.replace('0', '')
    all_symbols = all_symbols.replace('1', '')
    all_symbols = all_symbols.replace('l', '')
    all_symbols = all_symbols.replace('I', '')

    for i in range(m):
        temp_choice = random.choice(all_symbols)
        rez += temp_choice
        all_symbols = all_symbols.replace(temp_choice, '')  # если повторяющимеся считаются одна буква в заглавном
        # и прописном, то удалять по ловеркейсу и апперкейсу
    return rez


def main(n, m):
    rez = []
    for i in range(n):
        rez.append(generate_password(m))
    return rez


print("Случайный пароль из 7 символов:", generate_password(7))
print("10 случайных паролей длиной 15 символов:")
print(*main(10, 15), sep="\n")
