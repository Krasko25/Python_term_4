# Создайте графическую оболочку для скрипта, написанного в ходе
# выполнения задания № 4 лабораторной работы № 2, в виде диалогового
# окна (рис. 2). Рекомендуется использовать wxPython или PyQt.

# Требования к окну и скрипту:
# 18
# - всю область окна должен занимать список с результатами поиска
# строк по шаблону в файле и указанием даты и времени поиска.
# Поиск производится автоматически при каждом открытии какого-
# либо файла, при этом список не очищается, а пополняется новыми
# результатами. При запуске скрипта список изначально должен быть
# пустым (из файла лога данные подгружать не нужно);
# - строка меню содержит пункты «Файл» (с подпунктом «Открыть...»
# для открытия файла, в котором необходимо искать строки) и «Лог»
# (с подпунктами «Экспорт...», «Добавить в лог», «Просмотр»). Файл
# лога находится в рабочей папке скрипта и называется script18.log.
# Если файл отсутствует, скрипт при запуске должен выдать
# диалоговое окно с информацией «Файл лога не найден. Файл будет
# создан автоматически» и кнопкой «ОК». При выборе пункта меню
# «Экспорт...» содержимое списка должно сохраниться в файле,
# который укажет пользователь. При выборе пункта «Добавить в лог»
# содержимое списка приписывается в конец файла script18.log. При
# выборе пункта «Просмотр» текущее содержимое списка удаляется,
# и список заполняется данными из лога. Перед этим действием скрипт
# должен выдать диалоговое окно с вопросом «Вы действительно
# хотите открыть лог? Данные последних поисков будут потеряны!»
# и кнопками «Да» и «Нет»;
# - статусная строка должна состоять из двух полей: в первом поле (60%
# ширины окна), в зависимости от последнего произведенного
# действия, выводится либо текст «Открыт лог», либо текст
# «Обработан файл <полное_имя_файла>»; второе поле (40%
# ширины окна) служит для отображения размера последнего
# обработанного файла в байтах. Эта строка форматируется: выводятся
# пробелы между степенями тысячи (например, «2 036 231 байт»);
# - файлы нужно открывать и сохранять с помощью стандартного
# диалогового окна (рис. 3).

import sys
import re
import os
from datetime import datetime
from PyQt5.QtWidgets import *

def test():
    print()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Скрипт. Искатель строк")
        self.setGeometry(100, 100, 700, 500)

        # Список
        self.listWidget = QListWidget()
        self.setCentralWidget(self.listWidget)

        # Строка меню
        menubar = self.menuBar()
        fileMenu = menubar.addMenu("Файл")
        openAction = QAction("Открыть...", self)
        openAction.triggered.connect(self.openFile)
        fileMenu.addAction(openAction)

        logMenu = menubar.addMenu("Лог")
        exportAction = QAction("Экспорт...", self)
        exportAction.triggered.connect(self.exportLog)
        logMenu.addAction(exportAction)

        appendAction = QAction("Добавить в лог", self)
        appendAction.triggered.connect(self.appendToLog)
        logMenu.addAction(appendAction)

        viewAction = QAction("Просмотр", self)
        viewAction.triggered.connect(self.viewLog)
        logMenu.addAction(viewAction)

        # Статусная строка
        self.statusBarWidget = QStatusBar()
        self.setStatusBar(self.statusBarWidget)

        self.statusLabelAction = QLabel("Готов")
        self.statusLabelAction.setMinimumWidth(int(self.width() * 0.6))
        self.statusBarWidget.addPermanentWidget(self.statusLabelAction)

        self.statusLabelSize = QLabel("")
        self.statusLabelSize.setMinimumWidth(int(self.width() * 0.4))
        self.statusBarWidget.addPermanentWidget(self.statusLabelSize)

        # Проверка лог-файла
        self.logPath = os.path.join(os.getcwd(), "script18.log")
        if not os.path.exists(self.logPath):
            QMessageBox.information(self, "Информация", "Файл лога не найден. Файл будет создан автоматически")
            #Пустой файл
            with open(self.logPath, 'w', encoding='utf-8') as f:
                pass

    def openFile(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Открыть файл", filter="Text files (*.txt);;All files (*)")
        if not filePath:
            return
        with open(filePath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Поиск номеров
        pattern = r"\(\d{3}\)\d{3}-?\d{2}-?\d{2}"
        matches = []
        lines = content.splitlines()
        for i in range(len(lines)):
            line = lines[i]
            lineNum = i + 1
            for match in re.finditer(pattern, line):
                pos = match.start()
                found = match.group()
                matches.append((lineNum, pos, found))

        # Добавляем в список
        now = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        self.listWidget.addItem(f"--- Поиск в файле '{os.path.basename(filePath)}' [{now}] ---")
        for lineNum, pos, found in matches:
            self.listWidget.addItem(f"Строка {lineNum}, позиция {pos} : найдено '{found}'")

        # Статусная строка
        self.statusLabelAction.setText(f"Обработан файл {filePath}")
        sizeBytes = os.path.getsize(filePath)
        self.statusLabelSize.setText(f"{self.formatBytes(sizeBytes)} байт")

    def exportLog(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Экспорт результатов", filter="Text files (*.txt);;All files (*)")
        if not filePath:
            return
        try:
            with open(filePath, 'w', encoding='utf-8') as f:
                for i in range(self.listWidget.count()):
                    f.write(self.listWidget.item(i).text() + "\n")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось сохранить: {e}")

    def appendToLog(self):
        with open(self.logPath, 'a', encoding='utf-8') as f:
            for i in range(self.listWidget.count()):
                f.write(self.listWidget.item(i).text() + "\n")

    def viewLog(self):
        reply = QMessageBox.question(self, "Подтверждение",
                                     "Вы действительно хотите открыть лог? "
                                     "Данные последних поисков будут потеряны!",
                                     QMessageBox.Yes | QMessageBox.No)
        if reply != QMessageBox.Yes:
            return

        self.listWidget.clear()
        with open(self.logPath, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.rstrip('\n')
                if line:
                    self.listWidget.addItem(line)

        self.statusLabelAction.setText("Открыт лог")
        sizeBytes = os.path.getsize(self.logPath)
        self.statusLabelSize.setText(f"{self.formatBytes(sizeBytes)} байт")

    @staticmethod
    def formatBytes(n):
        s = str(n)
        result = ""
        while len(s) > 3:
            result = " " + s[-3:] + result
            s = s[:-3]
        result = s + result
        return result.strip()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())