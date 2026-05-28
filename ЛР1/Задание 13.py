# Напишите собственную версию генератора enumerate под названием
# extra_enumerate. Пример вызова:
# for i, elem, cum, frac in extra_enumerate(x):
# print(elem, cum, frac)
# 5
# В переменной cum хранится накопленная сумма на момент текущей
# итерации, в переменной frac – доля накопленной суммы от общей
# суммы на момент текущей итерации. Например, для списка x=[1,3,4,2]
# вывод будет таким:
# (1, 1, 0.1) (3, 4, 0.4) (4, 8, 0.8) (2, 10, 1)

def extra_enumerate(the_list):
    element = 0
    full_sum = 0
    current_sum = 0
    fraction = 0
    
    for num in the_list:
        full_sum += num
    
    for i in range(len(the_list)):
        result = [i, the_list[i]]
        current_sum += the_list[i]
        result.append(current_sum)
        result.append(current_sum / full_sum)
        yield result

x = [1, 3, 4, 2]

for i, elem, cum, frac in extra_enumerate(x):
    print("(", elem, " ", cum, " ", frac, ")", sep="", end=" ")
    