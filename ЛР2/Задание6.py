# Напишите скрипт reorganize.py, который в директории --source создает
# две директории: Archive и Small. В первую директорию помещаются
# файлы с датой изменения, отличающейся от текущей даты на
# количество дней более параметра --days (т.е. относительно старые
# файлы). Во вторую – все файлы размером меньше параметра --size байт.
# Каждая директория должна создаваться только в случае, если найден
# хотя бы один файл, который должен быть в нее помещен. Пример
# вызова:
# reorganize --source "C:\TestDir" --days 2 --size 4096

import argparse # аргументы командной строки
import os
from datetime import date
import shutil # перемещение файла

#Объект парсер, который читает и разбирает аргументы командной строки
# parser - инструмент
parser = argparse.ArgumentParser()
parser.add_argument("--source")
parser.add_argument("--days", type=int)
parser.add_argument("--size", type=int)
# Читает аргументы и разбирает их 
# args - результат
args = parser.parse_args()

today = date.today()

#Названия файлов в папке
filesTitles = os.listdir(args.source)

archive_path = os.path.join(args.source, "Archive")
small_path = os.path.join(args.source, "Small")

for file in filesTitles:
    #Сколько секунд прошло с 1970 года до последнего редактирования файла
    fullPath = os.path.join(args.source, file)
    timestamp = os.path.getmtime(fullPath)
    #Преобразование в дату
    fileDate = date.fromtimestamp(timestamp)
    
    fileSize = os.path.getsize(fullPath)
    
    if (today - fileDate).days > args.days:
        os.makedirs(archive_path, exist_ok=True)
        newFilePath = os.path.join(archive_path, file)
        shutil.move(fullPath, newFilePath)
    elif fileSize < args.size:
        os.makedirs(small_path, exist_ok=True)
        newFilePath = os.path.join(small_path, file)
        shutil.move(fullPath, newFilePath)
        
        
        
        

