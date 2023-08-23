'''
Задача 10: 
На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
а некоторые – гербом. Определите минимальное число монеток, 
которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть
'''

n = int(input("Введите кол-во монеток: "))
count_1 = 0
count_0 = 0

for i in range(n):
    coin = int(input('Введите кол-во монет вверх орлом - "1", решкой - "0": ' ))
    if coin == 1:
        i += 1
        count_1 += 1
    else:
        count_0 = n - count_1
    
print(f'{count_1} монет лежат орлом, {count_0} монет лежат решкой')

if count_1 < count_0:
    print(f'Нужно перевернуть {count_1} монет')
else:
    print(f'Нужно перевернуть {count_0} монет')
