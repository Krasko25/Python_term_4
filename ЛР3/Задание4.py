# Напишите простой класс StringFormatter для форматирования строк со
# следующим функционалом:
# – удаление всех слов из строки, длина которых меньше n букв;
# – замена всех цифр в строке на знак «*»;
# – вставка по одному пробелу между всеми символами в строке;
# – сортировка слов по размеру;
# – сортировка слов в лексикографическом порядке.
# Примечание. Разделители слов можно задавать отдельно. По
# умолчанию в качестве разделителя принимается только символ
# пробела.

class StringFormatter:
    def __init__(self, string):
        self.string = string
        self.separator = " "

    #Задать разделитель слов
    def set_separator(self, sep):
        self.separator = sep

    #Получить список слов, разделённых нужным разделителем
    def get_words(self):
        return self.string.split(self.separator)

    #Собрать строку из слов через разделитель
    def set_string_from_words(self, words):
        self.string = self.separator.join(words)

    #Удаление всех слов, длина которых меньше n букв
    def remove_short_words(self, n):
        words = self.get_words()
        words = [w for w in words if len(w) >= n]
        self.set_string_from_words(words)

    # Замена всех цифр
    def replace_digits(self):
        new_str = ""
        for ch in self.string:
            if ch.isdigit():
                new_str += "*"
            else:
                new_str += ch
        self.string = new_str

    # Вставка пробела между символами
    def insert_spaces_between_chars(self):
        self.string = " ".join(self.string)

    #Сортировка слов по размеру
    def sort_words_by_length(self):
        words = self.get_words()
        words.sort(key=len)
        self.set_string_from_words(words)

    # Сортировка слов в лексикографическом порядке
    def sort_words_lexicographically(self):
        words = self.get_words()
        words.sort()
        self.set_string_from_words(words)

    def __str__(self):
        return self.string


sf = StringFormatter("Вот какой-то 1287 текст для Тестирования программы")
print("Исходная строка:", sf)

sf.remove_short_words(5)
print("После удаления слов менее 5 символов:", sf)

sf = StringFormatter("Вот какой-то 1287 текст для Тестирования программы")
sf.replace_digits()
print("Замена цифр на '*':", sf)

sf = StringFormatter("Вот какой-то 1287 текст для Тестирования программы")
sf.insert_spaces_between_chars()
print("Пробелы между символами:", sf)

sf = StringFormatter("Вот какой-то 1287 текст для Тестирования программы")
sf.sort_words_by_length()
print("Сортировка по длине:", sf)

sf = StringFormatter("Вот какой-то 1287 текст для Тестирования программы")
sf.sort_words_lexicographically()
print("Лексикографическая сортировка:", sf)