# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

n = int(input('Введите номер четверти: '))

if n > 0 and n <= 4:
    if n == 1:
        print('Диапазон возможных координат: x > 0 и y > 0')
    elif n == 2:
        print('Диапазон возможных координат: x < 0 и y > 0')
    elif n == 3:
        print('Диапазон возможных координат: x < 0 и y < 0')
    else:
        print('Диапазон возможных координат: x > 0 и y < 0')
else:
    print('Введитите правильный номер четверти(1,2,3,4)')

