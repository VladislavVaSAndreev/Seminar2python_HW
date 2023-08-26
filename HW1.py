# На столе лежат n монеток. 
# Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть.

import random

def coins_var(coins_var):
    orel = 0
    reshka = orel
    for i in range(coins_var):
        coins_num = random.randrange(0,2)
        print(coins_num, end = " ")
        if coins_num < 1:
            reshka +=1
        else:
            orel += 1
        if reshka > orel:
            print(end = "\n")
            return orel
    else:
        print(end = "\n")
        return reshka

number = int(input("Введите количество монет: "))
print(coins_var(number))

