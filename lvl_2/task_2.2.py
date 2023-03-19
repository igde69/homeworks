# Задача 2.2. 

# Напишите функцию, которая возвращает номер квартала по номеру месяца
# Например: 
# месяц 2 (февраль) является частью первого квартала; 
# месяц 6 (июнь) является частью второго квартала; 
# месяц 11 (ноябрь) является частью четвертого квартала.

def quarter_of(month):
    pass

#       ***

import datetime
import locale
number = input("Введите номер месяца: ")
month = int(number)

if int(number) < 1 or int(number) > 12:
    print("Такого месяца нет!")
    exit()
else:
    date = datetime.datetime.strptime(number, "%m")
# Код форматирования функции .strptime() - месяц в виде десятичного числа (%m)
    locale.setlocale(category = locale.LC_ALL,locale = "Russian")
# Здесь локализуем язык 
    month_name = date.strftime("%B")
# Код форматирования функции .strptime() - полное название месяца (%B)
# Интересно до названия месяца можно добраться непосредственно без даты ?

def quaters(months):
    if months in [1,2,3]:
        return 'первого'
    elif months in [4,5,6]:
        return 'второго'
    elif months in [7,8,9]:
        return 'третьего'
    else:
        return 'четвёртого'

print('Месяц', month, '(',month_name,')', 'является частью',quaters(month), 'квартала')     

# Вывод
# Введите номер месяца: 7
# Месяц 7 ( Июль ) является частью третьего квартала
