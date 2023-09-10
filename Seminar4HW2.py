#    В фермерском хозяйстве в Карелии выращивают чернику. Она растёт
#  на круглой грядке, причём кусты высажены только по окружности.
#  Таким образом, у каждого куста есть ровно два соседних. Всего
#  на грядке растёт N кустов.
#    Эти кусты обладают разной урожайностью, поэтому ко времени
#  сбора на них выросло различное число ягод — на i-ом кусте
#  выросло ai ягод.
#    В этом фермерском хозяйстве внедрена система автоматического
#  сбора черники. Эта система состоит из управляющего модуля и
#  нескольких собирающих модулей. Собирающий модуль за один заход,
#  находясь непосредственно перед некоторым кустом, собирает ягоды
#  с этого куста и с двух соседних с ним.
#    Напишите программу для нахождения максимального числа ягод,
#  которое может собрать за один заход собирающий модуль, находясь
#  перед некоторым кустом заданной во входном файле грядки.


quantity = int(input('введите число кустов '))
bush_list = []
for i in range(quantity):
    bush = int(input('введите число '))
    bush_list.append(bush)
bush_list.append(bush_list[0])
bush_list.append(bush_list[1])
sum_result = 0
for i in range(quantity):
    sum_bush = bush_list[i]+bush_list[i+1]+bush_list[i+2]
    if sum_bush > sum_result:
        sum_result = sum_bush
print(sum_result)
