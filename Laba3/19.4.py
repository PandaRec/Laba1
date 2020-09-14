def palindrom(s=''):
    s = s.replace(' ', '').lower()
    return 'Палиндром' if s == s[::-1] else 'Не палиндром'


print(palindrom('Палиндром'))
