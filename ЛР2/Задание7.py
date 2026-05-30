# Написать скрипт trackmix.py, который формирует обзорный трек-микс альбома 
# (попурри из коротких фрагментов mp3-файлов в пользовательской директории). Для 
# -манипуляций со звуковыми файлами можно использовать сторонние утилиты, например, FFmpeg.
# Пример вызова и работы скрипта:
# trackmix --source "C:\Muz\Album" --count 5 --frame 15 -l -e
# --- processing file 1: 01 - Intro.mp3
# --- processing file 2: 02 - Outro.mp3
# --- done!
# Параметры скрипта:
# --source (-s) – имя рабочей директории с треками, обязателен;
# --destination (-d) – имя выходного файла, необязателен (если не указан,
# то имя выходного файла – mix.mp3 в директории source);
# --count (-c) – количество файлов в "нарезке", необязателен (если он не
# указан, то перебираются все mp3-файлы в директории source);
# --frame (-f) – количество секунд на каждый файл, необязателен (если не
# указан, скрипт вырезает по 10 секунд из произвольного участка каждого
# файла);
# --log (-l) – необязательный ключ (если этот ключ указывается, то скрипт
# должен выводить на консоль лог процесса обработки файлов, как в
# примере);
# --extended (-e) – необязательный ключ (если этот ключ указывается, то
# каждый фрагмент попурри начинается и завершается небольшим
# fade in/fade out).__

import subprocess
import argparse # аргументы командной строки
import os
from random import randint # для случайного фрагмента песни
import shutil # Для удаления папки и всего содержимого

from random import sample

ffprobe_path = os.path.join("ffmpeg", "bin", "ffprobe.exe")
ffmpeg_path = os.path.join("ffmpeg", "bin", "ffmpeg.exe")

#Объект парсер, который читает и разбирает аргументы командной строки
# parser - инструмент
parser = argparse.ArgumentParser()
parser.add_argument("--source", "-s", required=True)
parser.add_argument("--destination", "-d", default=None)
parser.add_argument("--count", "-c", default=None)
parser.add_argument("--frame", "-f", default=10)
parser.add_argument("--log", "-l", action="store_true")
parser.add_argument("--extended", "-e", action="store_true")
# Читает аргументы и разбирает их 
# args - результат
args = parser.parse_args()

if args.destination == None:
    args.destination = os.path.join(args.source, "mix.mp3")

frameInt = int(args.frame)

#Названия файлов в папке, принимается только mp3
musicTitles = [file for file in os.listdir(args.source) if file.endswith(".mp3")]

# Если count пустой, то берём все мелодии
if args.count != None:
    # Берём в случайном порядке мелодии. Если команда просит больше мелодий, чем есть в папке, то выдаём все мелодии
    musicTiles = sample(musicTitles, min(int(args.count), len(musicTitles))) 

tempFolderPath = os.path.join(args.source, "TempFolder")
os.makedirs(tempFolderPath, exist_ok=True)

fileListPath = os.path.join(tempFolderPath, "fileList.txt")

# По ходу обрезания мелодий будем составлять файл со списком для объединения
with open(fileListPath, "w", encoding="utf-8") as f:
    for songNum in range(len(musicTiles)):     
        if (args.log == True):
            print(f"--- processing file {songNum+1}: {musicTitles[songNum]}")
        
        tempSongPath = os.path.join(tempFolderPath, musicTitles[songNum])
        currentSongPath = os.path.join(args.source, musicTitles[songNum])
        
        # Добавления пути к обрезанной песни в файл, чтобы после объединять их
        f.write(f"file '{os.path.abspath(tempSongPath)}'\n")
        
        #Узнать длину песни
        ffprobeResult = subprocess.run([
            ffprobe_path,
            "-v", "error",                           # только ошибки
            "-show_entries", "format=duration",       # показать длительность
            "-of", "default=noprint_wrappers=1:nokey=1",  # только число, без текста
            currentSongPath
        ], capture_output=True, text=True)
        
        songLength = float(ffprobeResult.stdout.strip())
        
        fragmentStart = randint(0, int(songLength) - frameInt)
        if fragmentStart < 0:
            fragmentStart = 0
        
        #сохранение обрезанных кусков мелодий
        if args.extended:
            subprocess.run([
            ffmpeg_path,
                "-i", currentSongPath, # входной файл
                "-ss", str(fragmentStart), # начало фрагмента
                "-t", str(args.frame), # длительность
                "-c", "copy", # без перекодирования
                tempSongPath # выходной файл
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            subprocess.run([
            ffmpeg_path,
                "-i", currentSongPath, # входной файл
                "-ss", str(fragmentStart), # начало фрагмента
                "-t", str(args.frame), # длительность
                "-af", f"afade=t=in:d=2,afade=t=out:st={float(args.frame) - 2}:d=2",
                tempSongPath # выходной файл
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

#объединение фрагментов
subprocess.run([
    ffmpeg_path,
    "-f", "concat",
    "-safe", "0",
    "-i", fileListPath,
    "-c", "copy",
    args.destination
], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
if (args.log == True):
    print("Объединение фрагментов завершено")

#Удаляем папку с временными файлами
if os.path.exists(tempFolderPath):
    shutil.rmtree(tempFolderPath)
    if (args.log == True):
        print("Папка с временными файлами удалена")