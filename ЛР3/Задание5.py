# Напишите скрипт с графическим интерфейсом пользователя для
# демонстрации работы класса StringFormatter. Примеры окон приведены
# на рис. 4 (все элементы управления необходимо обязательно
# реализовать те же, что присутствуют на рисунке). Разные комбинации
# отмеченных чекбоксов приводят к разным цепочкам операций
# форматирования задаваемой в верхнем поле строки с разными
# результатами:

import sys
from PyQt5.QtWidgets import *

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


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("StringFormatter Demo")
        self.setGeometry(200, 200, 500, 300)

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        mainLayout = QVBoxLayout(centralWidget)
        mainLayout.setContentsMargins(15, 15, 15, 15)
        mainLayout.setSpacing(8)  # отступ между элементами 

        topLayout = QHBoxLayout()
        topLayout.addWidget(QLabel("Строка:"))
        topLayout.addSpacing(16)  # расстояние между надписью и полем
        self.inputLineEdit = QLineEdit()
        topLayout.addWidget(self.inputLineEdit)
        mainLayout.addLayout(topLayout)

        # Группа чекбоксов
        checkBoxLayout = QVBoxLayout()
        checkBoxLayout.setContentsMargins(70, 0, 0, 0)

        cbShortWordsLayout = QHBoxLayout()
        self.cbShortWords = QCheckBox("Удалить слова размером меньше")
        self.spinBox = QSpinBox()
        self.spinBox.setMinimum(2)
        self.spinBox.setValue(4)
        self.spinBox.setMaximum(20)
        cbShortWordsLayout.addWidget(self.cbShortWords)
        cbShortWordsLayout.addWidget(self.spinBox)
        cbShortWordsLayout.addWidget(QLabel("букв"))
        cbShortWordsLayout.addStretch()
        checkBoxLayout.addLayout(cbShortWordsLayout)

        self.cbReplaceDigits = QCheckBox("Заменить все цифры на *")
        checkBoxLayout.addWidget(self.cbReplaceDigits)

        self.cbInsertSpaces = QCheckBox("Вставить по пробелу между символами")
        checkBoxLayout.addWidget(self.cbInsertSpaces)

        self.cbSort = QCheckBox("Сортировать слова в строке")
        checkBoxLayout.addWidget(self.cbSort)

        mainLayout.addLayout(checkBoxLayout)

        # Радиокнопки
        radioLayout = QVBoxLayout()
        radioLayout.setContentsMargins(85, 0, 0, 0)
        self.radioSortLength = QRadioButton("по размеру")
        self.radioSortLex = QRadioButton("лексикографически")
        self.radioSortLength.setChecked(True)
        radioLayout.addWidget(self.radioSortLength)
        radioLayout.addWidget(self.radioSortLex)
        radioLayout.addStretch()
        # Радиокнопки неактивны если сортировка не включена
        self.radioSortLength.setEnabled(False)
        self.radioSortLex.setEnabled(False)
        mainLayout.addLayout(radioLayout)

        # Связь чекбокса сортировки с радиокнопками
        self.cbSort.toggled.connect(self.toggleRadioButtons)

        self.formatButton = QPushButton("Форматировать")
        self.formatButton.clicked.connect(self.applyFormatting)
        buttonLayout = QHBoxLayout()
        buttonLayout.setContentsMargins(71, 0, 0, 0)
        buttonLayout.addWidget(self.formatButton)
        mainLayout.addLayout(buttonLayout)

        # Результат
        resultLayout = QHBoxLayout()
        resultLayout.addWidget(QLabel("Результат:"))
        self.resultLineEdit = QLineEdit()
        self.resultLineEdit.setReadOnly(True)
        resultLayout.addWidget(self.resultLineEdit)
        mainLayout.addLayout(resultLayout)
        
        #Чтобы не было интервала горизонтального посреди элементов
        mainLayout.addStretch() 

    def toggleRadioButtons(self, checked):
        self.radioSortLength.setEnabled(checked)
        self.radioSortLex.setEnabled(checked)

    def applyFormatting(self):
        text = self.inputLineEdit.text()
        if not text:
            self.resultLineEdit.setText("")
            return
        sf = StringFormatter(text)
        
        if self.cbShortWords.isChecked():
            n = self.spinBox.value()
            sf.remove_short_words(n)

        if self.cbReplaceDigits.isChecked():
            sf.replace_digits()

        if self.cbInsertSpaces.isChecked():
            sf.insert_spaces_between_chars()

        if self.cbSort.isChecked():
            if self.radioSortLength.isChecked():
                sf.sort_words_by_length()
            else:
                sf.sort_words_lexicographically()

        self.resultLineEdit.setText(str(sf))


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())