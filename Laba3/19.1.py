import calendar
import locale


def month_name(number=1, language=''):
    if language.__eq__('ru'):
        locale.setlocale(locale.LC_ALL, '')
        print(calendar.month_name[number])
    elif language.__eq__('en'):
        print(calendar.month_name[number])


month_name(3, 'en')
