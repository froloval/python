# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше
# заданного максимума)

from random import randint
mas_len = int(input('Введите длинну последовательности '))
random_list = []
for i in range(mas_len):
    random_list.append(randint(-10, 10))
start_delta = int(input('Введите нижнюю ганицу диапазона '))
end_delta = int(input('Введите верхнюю ганицу диапазона'))
if start_delta > end_delta:
    temp_delta = start_delta
    start_delta = end_delta
    end_delta = temp_delta
index_list = []
for i in range(mas_len):
    if random_list[i] >= start_delta and random_list[i] <= end_delta:
        index_list.append(i)
print(random_list)
print(index_list)
