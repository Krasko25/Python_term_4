# Напишите программу, имитирующую работу банкомата. Выберите
# структуру данных для хранения купюр разного достоинства в заданном
# количестве. При вводе пользователем запрашиваемой суммы денег,
# скрипт должен вывести на консоль количество купюр подходящего
# достоинства. Если имеющихся денег не хватает, то необходимо
# напечатать сообщение «Операция не может быть выполнена!».
# Например, при сумме 5370 рублей на консоль должно быть выведено
# «5*1000 + 3*100 + 1*50 + 2*10».

banknotes = {
    5000: 5,
    1000: 10,
    500: 10,
    200: 10,
    100: 100,
    10: 10
}

banknotes_taken = {
    5000: 0,
    1000: 0,
    500: 0,
    200: 0,
    100: 0,
    10: 0
}

money_needed = int(input("Введите желаемую сумму: "))
what_is_left_to_give = money_needed

for nominal in sorted(banknotes.keys(), reverse=True):
    amount_taken = min(banknotes[nominal], what_is_left_to_give // nominal)
    
    banknotes_taken[nominal] += amount_taken
    banknotes[nominal] -= amount_taken
    what_is_left_to_give -= amount_taken * nominal

if what_is_left_to_give != 0:
    print("Операция не может быть выполнена!")
    for nominal in banknotes.keys():
        banknotes[nominal] = banknotes_taken[nominal]
        banknotes_taken[nominal] = 0
else:
    print(f"{banknotes_taken[5000]}*5000 + {banknotes_taken[1000]}*1000 + {banknotes_taken[500]}*500 + {banknotes_taken[200]}*200 + {banknotes_taken[100]}*100 + {banknotes_taken[10]}*10")
    

