# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно
# ввести с клавиатуры. Формула для получения n-го члена
# прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
from unittest import result


ferst_el = int(input('Введите первый элемент '))
step = int(input('Введите шаг '))
mas_len = int(input('Введите количество элементов '))
result_mas = [ferst_el]
for i in range(1,mas_len):
    result_mas.append(result_mas+i*step)
print(result_mas)
