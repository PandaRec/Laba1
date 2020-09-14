all_sentences = []
to_print = []


def print_only_new(row):
    if not row in all_sentences:
        to_print.append(row)
        all_sentences.append(row)


print_only_new('Шутка номер 15')
print_only_new('Шутка номер 23')
print_only_new('Шутка номер 24')
print_only_new('Шутка номер 24')
print_only_new('Шутка номер 100')
print_only_new('Шутка номер 24')
print_only_new('Шутка номер 99')
print_only_new('Шутка номер 15')
print_only_new('Шутка номер 100')

print(*to_print, sep='\n')
