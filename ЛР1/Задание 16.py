# Напишите скрипт, который на основе списка из 16 названий футбольных команд 
# случайным образом формирует 4 группы по 4 команды, а также выводит на консоль 
# календарь всех игр (игры должны проходить по средам, раз в 2 недели, начиная с 
# 14 сентября текущего года). Даты игр необходимо выводить в формате «14/09/2016, 
# 22:45». Используйте модули random и itertools.
from random import shuffle
from itertools import combinations
from datetime import datetime, timedelta

teams = ["Португалия", "Арсенал", "Бразилия", "Манчестер Сити", "Франция", "Ливерпуль", 
         "Реал Мадрид", "Бавария", "Челси", "Аргентина", "Милан", 
         "ПСЖ", "Ювентус", "Англия", "Интер", "Барселона"]


def teams16to4groups(teams):
    shuffle(teams)
    groups = [[], [], [], []]
    for i in range(4):
        for j in range(4):
            groups[i].append(teams[i * 4 + j])
    return groups

def groupsIntoMatches(groups):
    matches = []
    # внешний цикл - каждая группа
    for i in range(len(groups)):
        matches.append([])
        # внутренний цикл - комбинации команд в каждой группе
        for team1, team2 in combinations(groups[i], 2):
            matches[i].append([team1, team2])
    return matches
            
def setDatesForMatches(matches, startTimeHours, startTimeMinutes, timeForOneGameMinutes):
    for numOfCircle in range(len(matches[0])): # каждый день берётся по одному матчу из каждой группы
        for numOfGroup in range(len(matches)): # Проход по группам
            matchtime = datetime(2026, 9, 16, startTimeHours, startTimeMinutes) + timedelta(weeks = 2 * numOfCircle, minutes=timeForOneGameMinutes * numOfGroup) 
            print(f"{matches[numOfGroup][numOfCircle][0]} против {matches[numOfGroup][numOfCircle][1]}:", 
                  matchtime.strftime("%d/%m/%Y, %H:%M"))

            
all_groups = teams16to4groups(teams)
all_matches = groupsIntoMatches(all_groups)
setDatesForMatches(all_matches, 8, 30, 135)

