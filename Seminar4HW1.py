#    Даны два неупорядоченных набора целых чисел (может быть, с
#  повторениями). Выдать без повторений в порядке возрастания все
#  те числа, которые встречаются в обоих наборах.
#    Пользователь вводит 2 числа. n — кол-во элементов первого
#  множества. m — кол-во элементов второго множества. Затем
#  пользователь вводит сами элементы множеств.

from random import randint
range_list1 = int(input('введите длинну первой последовательности '))
range_list2 = int(input('введите длинну второй последовательности '))
random_list1 = []
random_list2 = []
for i in range(range_list1):
    random_list1.append(randint(0, 10))
for i in range(range_list2):
    random_list2.append(randint(0, 10))
print(random_list1)
print(random_list2)
set1 = set(random_list1)
set2 = set(random_list2)
print(set1.intersection(set2))
