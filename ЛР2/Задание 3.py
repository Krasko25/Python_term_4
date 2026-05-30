# Задан путь к директории с музыкальными файлами (в названии
# которых нет номеров, а только названия песен) и текстовый файл,
# хранящий полный список песен с номерами и названиями в виде строк
# формата «01. Freefall [6:12]». Напишите скрипт, который корректирует
# имена файлов в директории на основе текста списка песен.
import os

folder = "Песни"
filename = folder + "/" + "Song_list.txt"

with open(filename, "r", encoding="utf-8") as f:
    songList = f.read()
    
songList = songList.split("\n")
songListNamesOnly = songList.copy()

for i in range(len(songListNamesOnly)):
    titleBeginning = songListNamesOnly[i].find(". ") + 2 #индекс начала названия
    titleEnding = songListNamesOnly[i].find(" [")
    songListNamesOnly[i] = songListNamesOnly[i][titleBeginning:titleEnding]

songTitles = os.listdir(folder)

for songFileTitleIndex in range(len(songTitles)):
    for songTitleInTheListIndex in range(len(songListNamesOnly)):
        if songListNamesOnly[songTitleInTheListIndex].lower() in songTitles[songFileTitleIndex].lower():
            extention = os.path.splitext(songTitles[songFileTitleIndex])[1] #берём разрешение файла
            
            old_path = os.path.join(folder, songTitles[songFileTitleIndex])
            new_path = os.path.join(folder, songList[songTitleInTheListIndex].strip() + extention)
            os.rename(old_path, new_path)
            break


        