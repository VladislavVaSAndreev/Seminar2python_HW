# Требуется вывести все целые степени двойки (т.е. числа вида 2^k), 
# не превосходящие числа n.

n=int(input("Введите число: "))
degree=1
while degree<=n:
    print(degree,end=' ')
    degree=degree*2
