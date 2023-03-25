
# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции max и min использовать нельзя!

def minimum(arr):
    pass

def maximum(arr):
    pass
# заглушка = отсутствие действия 

                ###

integer_list = [12, 56, 87, 17, 35, 68, 73]
max_value = sorted(integer_list, reverse=True)[0]
sorted_list = sorted(integer_list, reverse=True)
print(sorted_list) 
print('max =', max_value)

min_value = sorted(integer_list)
min_value = min_value[0]
print('min =',min_value)

                ###


#integer_list = [4,6,2,1,9,63,-134,566]
#mx = max(integer_list)
#mn = min(integer_list)
#print('Наибольшее:', mx)
#print('Наименьшее:', mn)