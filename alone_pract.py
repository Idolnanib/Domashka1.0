# Задание по переводу рублей в доллары.
# План выполнения: наинпутить рубли с курсом доллара и запринтовать ответ

# Rubl = float(input('Введи сколько рублей хочешь перевести в баксы, бро : '))
# print('17.10.2021 курс был такой: за 1$ дают 70.99 рублей')
# Kurs = float(input('Введи курс баксов к рублю , бро : '))
# import math
# print('Столько франклинов ты получишь за свои рубли :', round(Rubl/Kurs,2),' $')

# Зaдание 2 на print и input.

# productName1 = input('Что купил сперва ты седня? : ')
# price1 = int(input('Назови цену этого чуда, только давай без копеек, я уже int поставил : '))
# productName2 = input('Что второе ты купил? : ')
# price2 = int(input('Назови цену этого чуда, только без копеек,ty : '))
# print('давай сделаем итог вышенаписанного :', productName1, '- ', price1, 'and', productName2, '- ',price2 )
# print('Чувак, то что ты сегодня накупил вышло на', price1+price2 , " рублей")

# Задание 3 , которое я еще не читал

# balanc = int(input('Сколько денег на карте? : '))
# roznica = int(input('Напиши цену за товар(1 шт.) '))
# cena = int(input('Друг, какая цена этого товара? '))
# print('друг, там цена на все товары ', roznica * cena,', а баланс на карте останется : ',balanc - roznica * cena)

# Try part №4

# day_of_the_week = int(input('Напиши плс номер дня недели (номера начинаются с понедельника)) : '))
# if day_of_the_week == 1:
#     print('На понедельник запланирована(барабанная дробь) РАбоТА.Поздравляю!!')
# elif day_of_the_week == 2:
#     print('Во вторник спорт зал. ну мы же знаем, что работа, верно?? ;) ')
# elif day_of_the_week == 3:
#     print('В среду хобби. Т.е. идем на работу. Усиление ж ')
# elif day_of_the_week == 4:
#     print('В четверг выходной. За который дадут переработку, т.к. идешь на работу ')
# elif day_of_the_week == 5:
#     print('В пятницу плавание.Плавание в рутине на работе хе-хе ')
# elif day_of_the_week == 6:
#     print('Обучение рабочим моментам . Соре бро ')
# elif day_of_the_week == 7:
#     print('В воскресенье выходной только у христиан.А у нас работа ')
# else :
#     print('попробуй другую цифру')

# Задача 5 - ноутбук.- не работает правильно

# voper = int(input('Сколько оперативки на компе? : '))
# wind = input('экран IPS или LED? : ')
# price = int(input('Назови цену устройства : '))
# core = int(input('Сколько ядер ? '))
#
# if ((voper == 8 or 16) and (wind == 'IPS' or "LED") and (price <= 50000) and (core == 4 or 6 or 8)):
#     print('Бери его не глядя.')
# else:
#     print('Параметры не подходят или ты хулиганишь.Трай эгейн ')

# 6. Время суток


# time = float(input('Сколько время?? '))
# if 6 <= time < 12:
#     print('утро')
# elif 12 <= time < 18:
#     print('день')
# elif 18 <= time < 22:
#     print('вечер')
# elif 22 <= time <= 24 or 1 <= time < 6:
#     print('ночь')
# else:
#     print('Введи число со значением из промежутка [1:24]')

# 7 задание.

# number = int(input('Введи количество зведочек, которое ты хотел бы видеть )) '))
# z = '*'
# n = 0
# while n != number:
#     print(z,end='')
#     n = n + 1

# 8. массив , который список(28.10.2021)
# import math

# вариант 1 - цикл по списку через индекс i
# myList = [5, -3, 4, -6, 1]
# for i in range(len(myList)):
#     if myList[i] > 0: # если число положительное
#         print('+', myList[i])
#     else:
#         print(myList[i])
# print()

# вариант 2 - цикл по списку без индексов, сразу по элементам
# myList = [5, -3, 4, -6, 1]
# for elem in myList:
#     if elem > 0: # если число положительное
#         print('+', elem)
#     else:
#         print(elem)
# print()

# 10.11.2021
# ЗАДАЧА 1.
#  Создать список на 10 элементов, заполнить его числами в диапазоне от 0 до 100, вывести элементы списка в вместе с их индексами.
# К примеру, есть с {1,8,4}, тогда программа должна вывести:
# 0: 1
# 1: 8
# 2: 4

# import math
# import random
#
# my_glist = []
#
# for i in range(10):
#     my_glist.append(random.randint(0, 100))
#     print(i,': ',my_glist[i] )
#     print()
# print(my_glist)

# Задача 2 Создать список на 5 элементов,
# заполнить его числами в диапазоне от -10 до 100,
# вывести элементы списка в одну строку.
# Найти минимальный элемент.

# import math
# import random
#
# mega_list  = []
#
# for i in range(5):
#     mega_list.append(random.randint(-10, 100))
#     print(mega_list[i],end=' ')
#
# min_value = min(mega_list)
# print()
# print(min_value)

# Задача 3 Создать список на 15 элементов,
# заполнить его числами в диапазоне от 0 до 20,
# вывести элементы массива в одну строку. Найти максимальный элемент.

import math
import random

list_listok = []

for i in range(15):
    list_listok.append(random.randint(0, 20))
    print(list_listok[i],end=' ')
max_value = max(list_listok)
print()
print(max_value)