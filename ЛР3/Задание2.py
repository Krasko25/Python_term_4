# Напишите классы «Книга» (с обязательными полями: название, автор,
# код), «Библиотека» (с обязательными полями: адрес, номер) и
# корректно свяжите их. Код книги должен назначаться автоматически
# при добавлении книги в библиотеку (используйте для этого
# статический член класса). Если в конструкторе книги указывается в
# параметре пустое название, необходимо сгенерировать исключение
# (например, ValueError). Книга должна реализовывать интерфейс
# Taggable с методом tag(), который создает на основе строки набор тегов
# (разбивает строку на слова и возвращает только те, которые
# начинаются с большой буквы). Например, tag() для книги с названием
# ‘War and Peace’ вернет список тегов [‘War’, ‘Peace’]. Реализуйте классы
# таким образом, чтобы корректно выполнялся следующий код:
# lib = Library(1, ’51 Some str., NY’)
# lib += Book(‘Leo Tolstoi’, ‘War and Peace’)
# lib += Book(‘Charles Dickens’, ‘David Copperfield’)
# for book in lib:
# # вывод в виде: [1] L.Tolstoi ‘War and Peace’
# print(book)
# # вывод в виде: [‘War’, ‘Peace’]
# print(book.tag())

# все классы, которые наследуют этот должны иметь метод tag
class Taggable:
    def tag(self):
        pass

class Book(Taggable):
    _next_code = 1  # статический счётчик

    def __init__(self, author, title):
        self.__author = author
        self.__title = title
        self.__code = Book._next_code
        Book._next_code += 1

    def __str__(self):
        parts = self.__author.split()
        initials = parts[0][0] + "." # первая буква имени
        last_name = parts[-1] # фамилия
        return f"[{self.__code}] {initials}{last_name} '{self.__title}'"

    def tag(self):
        tags = []
        for word in self.__title.split():
            if word[0].isupper():
                tags.append(word)
        return tags


class Library:
    def __init__(self, number, address):
        self.__number = number
        self.__address = address
        self.__books = []

    def __iadd__(self, book):
        self.__books.append(book)
        return self

    def __iter__(self):
        return iter(self.__books)


lib = Library(1, '51 Some str., NY')
lib += Book('Leo Tolstoi', 'War and Peace')
lib += Book('Charles Dickens', 'David Copperfield')

for book in lib:
    # вывод в виде: [1] L.Tolstoi ‘War and Peace’
    print(book)
    # вывод в виде: [‘War’, ‘Peace’]
    print(book.tag())