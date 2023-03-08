# Задача 1.1.

# Есть строка с перечислением песен

# my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.

# first easy solution
# my_favorite_songs.split(",") 
# print (my_favorite_songs[:14])
# print (my_favorite_songs[-13:])
# print (my_favorite_songs[16:30])
# print (my_favorite_songs[-26:-15])


# second solution
my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation' 
# my_favorite_songs.split(",")
five_songs = [x.strip() for x in my_favorite_songs.split(',')]

# Here,we apply strip() to the list obtained by splitting the string with split().
# The extra whitespace in a comma-separated string containing whitespace can be removed to make a list.
# https://from-locals.com/python-split-strip-list-join/

print (f'{five_songs[0]}\n') 
# https://skillbox.ru/media/base/formatirovannye-stroki-v-python-primery-ispolzovaniya/
print (f'{five_songs[-1]}\n')
print (f'{five_songs[1]}\n')
print (f'{five_songs[-2]}\n')