# Напишите генератор frange как аналог range() с дробным шагом.
# Пример вызова:
# for x in frange(1, 5, 0.1):
# print(x)
# # выводит 1 1.1 1.2 1.3 1.4 … 4.9

def frange2(start, end, step):
    # Это необходимо из-за накопляющейся погрешности в float числах
    precision = len(str(step).split('.')[1])
    
    i = 0
    while (start + step*i) < (end-step):
        i += 1      
        yield round(start + step*i, precision)

print(*frange2(1, 5, 0.1))