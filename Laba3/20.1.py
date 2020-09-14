def translate(text=''):
    rez = ''
    to_del = ['а', 'я', 'о', 'е', 'у', 'ю', 'ы', 'и', 'э', 'ё', '.', ',', '-', ';', '?', '!']
    for i in text:
        if not i.lower() in to_del:
            rez += i

    return ' '.join(rez.split())


translatedText = translate('Удивительный факт, но текст на языке НЕРАЗБОРЧИВО оказывается довольно просто читать. '
                           'Достаточно небольшой тренировки - и вы сможете это делать.')
print(translatedText)
