'''
Задача 14: 
Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
'''
n = int(input("Введите число N: "))
res = 0
i = 0
while res <= n:
    res = 2**i
    i += 1
    if res > n:
        break
    print(res)