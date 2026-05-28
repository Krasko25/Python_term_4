# Напишите скрипт, который обрабатывает список строк-адресов
# следующим образом: сначала определяет, начинается ли каждая строка
# в списке с префикса «www». Если условие выполняется, то скрипт
# должен вставить в начало этой строки префикс «http://», а затем
# проверить, что строка заканчивается на «.com». Если у строки другое
# окончание, то скрипт должен вставить в конец подстроку «.com». В
# итоге скрипт должен вывести на консоль новый список с измененными
# адресами. Используйте генераторы списков.

adresses = ["www.site", "www.school48.com", "nowww.ru", "www.anothersite"]

new_adresses = [(adress + ".com") 
                if not adress.endswith(".com") and adress.startswith("http://")
                else adress
               for adress in [("http://" + adress) if adress[0:3] == "www" else adress
                for adress in adresses ]]

print(*new_adresses, sep="\n")
