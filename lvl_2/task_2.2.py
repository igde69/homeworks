# Задача 2.2. 

# Напишите функцию, которая возвращает номер квартала по номеру месяца
# Например: 
# месяц 2 (февраль) является частью первого квартала; 
# месяц 6 (июнь) является частью второго квартала; 
# месяц 11 (ноябрь) является частью четвертого квартала.

def quarter_of(month):
    pass

import datetime
number = input("Введите номер месяца: ")
month = int(number)
if int(number) < 1 or int(number) > 12:print("Такого месяца нет!")
else:
    date = datetime.datetime.strptime(number, "%m")
    # Код форматирования функции .strptime() - месяц в виде десятичного числа (%m)
    month_name = date.strftime("%B")
    # Код форматирования функции .strptime() - месяц как полное название (en_US) (%B)
    print("Название месяца:",month_name)

#quarter ={}
#if month in quarter:
#    print('Является частью', [])

