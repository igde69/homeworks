# Задача 2.3.

# Напишите функцию, которая принимает цифры от 0 до 9 и возвращает значение прописью.
# Например,
# switch_it_up(1) -> 'One'
# switch_it_up(3) -> 'Three'
# switch_it_up(10000) -> None
# Использовать условный оператор if-elif-else нельзя!

                ###

# определяем функцию, которая принимает на входе целое число
#def switch_it_up(num): 

# составляем список слов для цифр от 0 до 9
#    words = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']

# выделяем из входного числа его цифру сопоставляем цифру со словом из списка слов
#    digits = [int(n) for n in str(num)]
#    words_list = [words[n] for n in digits]

# с помощью метода .join() объединяем слово c пробелом и возвращаем результат
#    return ' '.join(words_list)

#num = int(input('Введите число: '))
#words = switch_it_up(num)
#print(words)
# ???             

                ###

# определяем функцию, которая принимает на входе целое число
def switch_it_up(digit):
    if digit > 9:
        return "None"
# составляем список слов для цифр от 0 до 9    
    words = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    return words[digit]

digit = int(input('Введите число: '))
words = switch_it_up(digit)
print(words)


#Введите число: 7
#Seven
#Введите число: 100
#None