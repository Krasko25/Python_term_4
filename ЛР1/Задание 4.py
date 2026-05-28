#Напишите скрипт, который разделяет введенный с клавиатуры 
# текст на слова и выводит сначала те слова, длина которых 
# превосходит 7 символов, затем слова размером от 4 до 7 символов, 
# затем – все остальные.

user_input = input("Введите текст: ")
my_list = user_input.split()
my_list7 = []
my_list456 = []
my_list_others = []

for word in my_list:
    if len(word) > 7:
        my_list7.append(word)
        continue
    if 4 <= len(word) <= 7:
        my_list456.append(word)
        continue
        
    my_list_others.append(word)
 
print("\n")    

print(*my_list7)
print(*my_list456)
print(*my_list_others)
