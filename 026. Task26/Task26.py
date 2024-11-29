# Орел и решка
# Дана строка текста, состоящая из букв русского алфавита "О" и "Р".
# Буква "О" – соответствует выпадению Орла, а буква "Р" – соответствует выпадению Решки.
# Напишите программу, которая подсчитывает наибольшее количество подряд выпавших Решек.
#
# Формат входных данных:
# На вход программе подается строка текста, состоящая из букв русского алфавита "О" и "Р".
#
# Формат выходных данных:
# Программа должна вывести наибольшее количество подряд выпавших Решек.
#
# Примечание. Если выпавших Решек нет, то необходимо вывести число 0.
# Входные данные 
# ОРРОРОРООРРРО 3
# ООООООРРРОРОРРРРРРР 7
# ООООРРРРОРОРРРРРРРРООРОРОРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРР 31
#
# Выходные данные
# 3
# 7
# 31

stroka = 'ООООООРРРОРОРРРРРРР'

count_p = 0

for i in range (0, len(stroka),1):
    if stroka[i] =='Р':
        if i > 0:
            if stroka[i] == stroka[i-1]:
                count_p += 1
            else:
                count_p = 1
        else:
            count_p += 1
    

print ('В заданной строке - ' + stroka)
print ('Решка выпадала подряд максимально ' + str(count_p) + ' раз(а)')