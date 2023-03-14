# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

#                ***
import random
my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

#just for myself:
#print (my_favorite_songs)
#for songs in my_favorite_songs:
#print(songs)
#n = my_favorite_songs.index(['Beautiful Day', 4.04])
#print(n)
#print(len(my_favorite_songs))
#songs =(random.sample (my_favorite_songs, 3))
#type(songs)

songs =(random.sample (my_favorite_songs, 3))
#print(songs)
time = 0
for song in songs:
       time += song[1]
# adds the right side operand’s value to the left side operand
# and assigns the result to the left operand       
print("Три песни списка звучат: {:.0f}".format(time), 'минут')
# форматирование time (Format float with no decimal places)        

#                ***

# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}
import random
keys = random.sample(list(my_favorite_songs_dict.keys()), 3)
#"DeprecationWarning: Sampling from a set deprecated since Python 3.9
#and will be removed in a subsequent version" occurs when using 
#the random.sample() function with a set as an argument in Python 3.9 or later versions
# программ дальше не работает - to fix this warning convert the set to a list. 
#print(keys)
time = 0
for key in keys:
    time += my_favorite_songs_dict[key]
print("Три песни словаря звучат: {:.0f}".format(time), 'минут')

#                ***

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

#                ***

import random
my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

songs = random.randint(0, len(my_favorite_songs) - 1)
# random.randint = возвращает псевдослучайное целое число
# в заданном диапазоне (0, len(my_favorite_songs) - 1)
# print(len(my_favorite_songs))
song_name = my_favorite_songs[songs]
print("Случайная песня из списка :",song_name)

#                ***

import random
my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

song = random.choice(list(my_favorite_songs_dict.keys()))
print("Случайная песня из словаря :",song)



# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 
#                ***

import random
import datetime
my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
songs =(random.sample (my_favorite_songs, 3))
#print(songs)
time = 0
for song in songs:
       time += song[1]
# получили время трех случайных песен
x = time
tseconds = int(x*60)
# перевели его в секунды
time_delta = datetime.timedelta(seconds = tseconds)
# создание объекта 
start = datetime.datetime(1900,1,1)
# начальное время (обязательно?)
result = start + time_delta
# суммируем с исследуемым интервалом
time_str = result.strftime('%H:%M:%S')
# форматирование 
print('Время звучания:', str(time_str)[3:]) 
# вывод без часов