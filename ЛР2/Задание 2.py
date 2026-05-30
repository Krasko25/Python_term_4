# Напишите скрипт, позволяющий искать в заданной директории и в ее
# подпапках файлы-дубликаты на основе сравнения контрольных сумм
# (MD5). Файлы могут иметь одинаковое содержимое, но отличаться
# именами. Скрипт должен вывести группы имен обнаруженных файлов-
# дубликатов.

import hashlib
import os

foldername = "ПапкаСДубликатами"

# root - корневая папка
# dirs - подпапки в ней
# files - файлы в ней

dublicateFiles = {}

for root, dirs, files in os.walk(foldername):
    for file in files:
        fullPath = os.path.join(root, file)
        
        with open(fullPath, "rb") as f: # бинарный режим rb
            content = f.read()
            md5 = hashlib.md5(content).hexdigest()
            
            if md5 not in dublicateFiles:
                dublicateFiles[md5] = []
            
            dublicateFiles[md5].append(fullPath)

print("Дубликаты:")
for dublicate in dublicateFiles:
    if len(dublicateFiles[dublicate]) > 1:
        print("---")
        for i in range(len(dublicateFiles[dublicate])):
            print(f"{dublicateFiles[dublicate][i]},")
        print()
