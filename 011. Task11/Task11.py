# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.

# Пример:

# Дано: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random

number = int(input('Введите количество элементов в списке: '))
if number == 0:
    print('Количество элементов в списке не может быть равно нулю')
    exit()
elif number == 1:
    print('В списке из одного элемента нет не чётных элементов')
    exit()    

# заполняем список
spisok = []
for i in range(1,number+1):
    spisok.append(random.randint(0,100)) 
    i += 1
print('Полученный список: ', spisok)

# складываем числа на нечётных позициях (индексах)
summa = 0
for i in range(1,number,2):
    summa +=spisok[i]
    
print('Сумма элементов на нечётных позициях равна: ', summa)
