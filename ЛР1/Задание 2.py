#Написать скрипт, который выводит на экран «True», 
# если элементы программно задаваемого списка представляют 
# собой возрастающую последовательность, иначе – «False».

my_list = [1, 3, 6, 9, 12, 8, 10]
flag = 1

for i in range(1, len(my_list)):
    if my_list[i-1] >= my_list[i]:
        print("False")
        flag = 0
        break

if flag == 1:
    print("True")