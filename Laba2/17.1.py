row = input()
dictionary = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i',
              'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
              'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'tc', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'y', 'э': 'e',
              'ю': 'iu', 'я': 'ia', 'ь': '', 'ъ': ''}
for i in row:
    if i.lower() in dictionary.keys():
        if i.isupper():
            i = dictionary[i.lower()].title()
        else:
            i = dictionary[i.lower()]
    print(i, end='')
