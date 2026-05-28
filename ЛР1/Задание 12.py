# Напишите генератор get_frames(), который производит «оконную
# декомпозицию» сигнала: на основе входного списка генерирует набор
# списков – перекрывающихся отдельных фрагментов сигнала размера
# size со степенью перекрытия overlap. Пример вызова:
# for frame in get_frames(signal, size=1024, overlap=0.5):
# print(frame)

def get_frames(signal, size, overlap):
    
    #То, насколько за одну пачку числе, за один массив, сдвигается текущая позиция
    step = int(size * (1-overlap))
    current_position = 0
    while (current_position + size) <= len(signal):
        batch = []
        
        # Берем size элементов для нового массива
        for i in range(current_position, current_position + size):
            batch.append(signal[i])
        current_position += step
        yield batch
    remainings = []
    
    # Выдаём оставшейся массив, в котором меньше чем size элементов
    for i in range(current_position, len(signal)):
        remainings.append(signal[i])
    yield remainings
        
    
my_signal = [2, 10, 42, 80, 12, 34, 91, 0, 3, 7, 6, 9, 11]

print(*get_frames(my_signal, 5, 0.2))

