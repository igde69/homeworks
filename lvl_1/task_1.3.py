# Задача 1.3.

# Напишите скрипт, который принимает от пользователя номер месяца, 
# а возвращает количество дней в нем.
# Результат проверки вывести на консоль
# Допущение: в феврале 28 дней
# Если номер месяца некорректен - сообщить об этом

# Например,
    # Введите номер месяца: 3
    # Вы ввели март. 31 дней

    # Введите номер месяца: 2
    # Вы ввели февраль. 28 дней

    # Введите номер месяца: 15
    # Такого месяца нет!

import datetime
number = input("Введите номер месяца: ")
month = int(number)
if int(number) < 1 or int(number) > 12:print("Такого месяца нет!")
else:
    date = datetime.datetime.strptime(number, "%m")
    # Код форматирования функции .strptime() - месяц в виде десятичного числа (%m)
    month_name = date.strftime("%B")
    # Код форматирования функции .strptime() - месяц как полное название (en_US) (%B)
    print("Название месяца: ",month_name)
days={1:31,
2:28,
3:31,
4:30,
5:31,
6:30,
7:31,
8:31,
9:30,
10:31,
11:30,
12:31
}
if month in days:
    print('Дней', days[month])
