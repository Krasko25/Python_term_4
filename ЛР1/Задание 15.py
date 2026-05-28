# Напишите параметризированный декоратор pre_process, который
# осуществляет предварительную обработку (цифровую фильтрацию)
# списка по алгоритму: s[i] = s[i]–a∙s[i–1]. Параметр а можно задать в
# коде (по умолчанию равен 0.97). Пример кода:
# @pre_process(a=0.93)
# def plot_signal(s):
# for sample in s:
# print(sample)

# Первый слой функции, так как именно функция-декоратор принимает параметр a
def pre_process(a = 0.97):
    # Второй слой принимает именно саму декорируемую функцию
    def decorator(func):
        # Этот слой уже обрабатывает данные перед передачей их в декорируемую функцию
        def result_func(s):
            filtered = s[:] #копируем, чтобы не менять оригинал
            if (len(filtered) > 1):
                for i in range(1, len(filtered)):
                    filtered[i] -= a * filtered[i-1]
            return func(filtered)
        return result_func
    return decorator

@pre_process(a=0.93)
def plot_signal(s):
    for sample in s:
        print(sample)


my_list = [6, 10, 2, 5, 9, 32, 19, 20, 10]

plot_signal(my_list)