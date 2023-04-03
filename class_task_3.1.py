# Задача 3.1.
# Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступны следующие методы матрицы:
#       * принимать новые значения, 
#       * заменять существующие значения, 
#       * выводить число строк и колонок.

# Пример матрицы 10 на 10 из единиц:
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Примечание! 
#   - новый класс не запрещено строить на базе существующих типов данных: списков, словарей и тд.
#   - отображать в таблице/матрице название колонки не обязательно!
#   - проявите фантазию :)

from pprint import pprint
class Matrix:
    def __init__(self, lines, columns):
        self.lines = lines
        self.columns = columns
        self.matrix = [[8 for j in range(columns)] for i in range(lines)]
    
    
m = Matrix(12, 12)
pprint(m.matrix)
print('Количество строк:',m.lines, 'Количество столбцов:', m.columns)
                ###
from pprint import pprint
class Matrix:
    def __init__(self, lines, columns):
        self.lines = lines
        self.columns = columns
        self.matrix = [[1 for j in range(columns)] for i in range(lines)]
        
    def set_cell(self, line, column,value):
        self.matrix[line][column] = value

m = Matrix(8, 8)
m.set_cell(4, 4, 8)

pprint(m.matrix)
print('Количество строк:',m.lines, 'Количество столбцов:', m.columns)
