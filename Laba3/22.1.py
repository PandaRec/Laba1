def encrypt_caesar(msg='', shift=3):
    rez = ''
    for i in msg:
        if 1040 <= ord(i) <= 1103:
            if 'А' <= i <= 'Я':
                if ord((i)) + shift > 1071:
                    i = chr(1040 + abs(shift - (1071 - ord(i)) - 1))
                elif ord((i)) + shift < 1040:
                    i = chr(1071 - abs(shift - (1040 - ord(i)) + 1))
                else:
                    i = chr(ord(i) + shift)

            elif 'а' <= i <= 'я':
                if ord((i)) + shift > 1103:
                    i = chr(1072 + abs(shift - (1103 - ord(i)) - 1))
                elif ord((i)) + shift < 1072:
                    i = chr(1103 - abs(shift - (1072 - ord(i)) + 1))
                else:
                    i = chr(ord(i) + shift)
            else:
                i = chr(ord(i) + shift)
        rez += i

    return rez


def decrypt_caesar(msg='', shift=-3):
    return encrypt_caesar(msg, -shift)


msg = "Да здравствует салат Цезарь!"
shift = 5
encrypted = encrypt_caesar(msg, shift)
decrypted = decrypt_caesar(encrypted, shift)
print(encrypted)
print(decrypted)
