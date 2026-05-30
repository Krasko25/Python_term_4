# Напишите скрипт, который читает текстовый файл и выводит символы
# в порядке убывания частоты встречаемости в тексте. Регистр символа
# не имеет значения. Программа должна учитывать только буквенные
# символы (символы пунктуации, цифры и служебные символы слудет
# игнорировать). Проверьте работу скрипта на нескольких файлах с
# текстом на английском и русском языках, сравните результаты с
# таблицами, приведенными в wikipedia.org/wiki/Letter_frequencies.
import os

filename = input("Введите имя txt файла: ")

with open(filename, "r", encoding="utf-8") as f:
    file_content = f.read()
    
allowedSymbols = "abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя"

noExtraSymbolsText = ''.join(ch for ch in file_content.lower() if ch in allowedSymbols)

noExtraSymbolsTextLen = len(noExtraSymbolsText)

symbolsFrequency = {}

for symbol in noExtraSymbolsText:
    symbolsFrequency[symbol] = symbolsFrequency.get(symbol, 0) + 1

for key, value in sorted(symbolsFrequency.items(), key=lambda x: x[1], reverse = True):
    print(f"{key}: {round(value/noExtraSymbolsTextLen * 100, 4)}%") # для красоты округлил число


