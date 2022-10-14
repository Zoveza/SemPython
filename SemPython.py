# 1.По двум заданным числам проверить является ли одно квадратом второго
# a=int(input("Введите число A = "))
# b=int(input("Введите число B = "))
# print((a**2==b)or(b**2==a))

# 2.Найти максимальное из пяти чисел

# lst = []
# for i in range(5):
#     num = int(input("Введите число: "))
#     lst.append(num)

# res = lst[0]
# for i in range(1, 5):
#     if lst[i] > res:
#         res = lst[i]
# print(res)

# 3. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

# n = int(input("Введите число n: "))
# for i in range(-n, n+1):
#     print(i, end=" ")

# 4. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа

# number = float(input("Введите число : "))
# number = int((number*10)%10)
# print(number)

# 5. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.
# n= int(input("Введите число: "))
# print (n%5==0 and n%10==0 or n%15==0 and n%30!=0)

# 6. Сложить числа вещественного числа

# n = input("Введите число : ")
# res = 0
# for i in n:
#     if i !="." and i !=",":
#         res +=int(i)
# print(res)

# 7. Написать программу проверки, является ли строка палиндромом

# n="abba"
# count = 0
# for i in range(len(n)//2):
#     if n[i]==n[-1-i]:
#         count+=1
# if count==(len(n)//2):
#     print("Polindrom")
# else:
#     print("Not polindrom")

# 8. Напишите программу, которая выводит нечетные числа из заданного списка и останавливается, если встречает число 554.

# lst = [23,4,67,-2,5,554,765]
# for i in lst:
#     if i%2!=0:
#         print(i, end=" ")
#     elif i ==554:
#         break

# Homework1 

# 1) Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

# day = int(input("Введите день недели от 1 до 7 : "))
# if day == 6 or day == 7:
#     print("Этот день является выходным")
# else:
#     print("Этот день не выходной")

# 2) Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             print(f'{x,y,z} : {(not(x or y or z)) == (not x and not y and not z)}')

# 3) Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# x = int(input("Введите значение X : "))
# y = int(input("Введите значение Y : "))
# if x>0 and y>0:
#     print("1 четверть")
# if x<0 and y>0:
#     print("2 четверть")
# if x<0 and y<0:
#     print("3 четверть")
# if x>0 and y<0:
#     print("4 четверть")
# else:
#     print("Точка не находится в определенной четверти")

# 4) Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# n = int(input("Введите номер четверти от 1 до 4 : "))
# if n>4 or n<1:
#     print("Такой четверти не существует")
# elif n==1:
#     print("x>0 and y>0")
# elif n==2:
#     print("x<0 and y>0")
# elif n==3:
#     print("x<0 and y<0")
# elif n==4:
#     print("x>0 and y<0")

# 5) Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# xA = int(input("Введите координату xA : "))
# xB = int(input("Введите координату xB : "))
# yA = int(input("Введите координату yA : "))
# yB = int(input("Введите координату yB : "))
# import math
# print("Расстояние между точками в 2D пространстве равна: ",math.sqrt((xA - xB)**2 + (yA - yB)**2), 2)

# Семинар 2
# 1. Посчитайте, сколько раз символ встречается в строке.

# string = "Посчитайте, сколько раз символ встречается в строке."
# res = 0
# simb = input("Введите символ: ")
# for i in string:
#     if i == simb:
#         res+=1
# print(res)

# 2. Дано количество секунд. Вывести результат в виде: дни:часы:минуты:секунды

# sec = int(input(''))
# min, sec = sec // 60, sec % 60
# hour, min = min // 60, min % 60
# day, hour = hour // 24, hour % 24
# print(f"{day}:{hour}:{min}:{sec}")

# 3. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.

# Пример:

# Для N = 5: 1, -3, 9, -27, 81

# a = int(input("Введите число: "))
# for i in range(a):
#     print((-3) ** i, end=" ")

# Homework 2

# 1) Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.

# Пример:
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# n = int(input("Введите натуральное число: "))
# d = {i : 3*i + 1 for i in range(1,n+1)}
# print(d)

# 2) Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# n = int(input("Введите натуральное число: "))
# nums = []
# candies = 1
# for i in range(1, n + 1):
#     nums.append(candies)
#     candies *= i + 1
# print(nums)

# 3) Задайте список из n чисел последовательности (1+ (1/n))^n и выведите на экран их сумму.

# Пример:
# Для n = 5: сумма = 11,55

# n = int(input("Введите число n: "))
# s = 0
# for i in range(1,n+1):
#     s += (1+(1/i))**i
# print(f"Cумма последовательности (1+(1/n))^n = {round(s,2)}")

# Семинар 3

# 1. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.

# my_text = 'привет мир привет друзья'
# my_text_1 = 'привет'
# my_list = my_text.split(" ")
# current_e = 0
# for i in my_list:
#     if i == my_text_1:
#         current_e += 1
# print(current_e)

# 2. Сгенерировать рандомное число
# import datetime
# print(datetime.datetime.now().microsecond % 100)

# 3. Определить, присутствует ли в заданном списке строк, некоторое число
# text_1 = ["hi", "my", "name", "is", "Anton", "1"]
# def find_digit(new_text):
#     for i in range(len(new_text)):
#         if new_text[i].isdigit():
#             print(i)

# find_digit(text_1)

# text_1 = ["5", "8", "32", "55", "7", "8"]
# num = 8
# def find_digit(new_text, num):
#     for i in range(len(new_text)):
#         if new_text[i].isdigit():
#             if int(new_text[i]) == num:
#                 print(i)
# find_digit(text_1, num)

# 4. Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

# text_1 =["qwe", "asd", "zxc", "ertqwe"]
# key_word = "qwe"
# def find_coincidence(new_text, key):
#     count = 0
#     for i in range(len(new_text)):
#         if new_text[i] == key:
#             count += 1
#             if count == 2:
#                 print(i)
#             break
#     if count < 2:
#         print("-1")

# find_coincidence(text_1, key_word)

# Homework 3

# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# list = [4, 8, 12, 55, 28, 2, 7]
# list_length = len(list)
# sum = 0
# for i in range(1, len(list), 2):
#         sum += list[i]       
# print(f"{list} - сумма элементов на нечётных позициях = {sum}")

# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# from random import randint

# number = int(input('Введите размер списка '))
# list = []
# list2 = []

# for i in range(number):
#     list.append(randint(1, 10))

# for i in range(len(list)):
#     while i < len(list)/2 and number > len(list)/2:
#         number = number - 1
#         a = list[i] * list[number]
#         list2.append(a)
#         i += 1

# print(list)
# print(list2)

# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# my_list = [1.1, 1.2, 3.1, 5, 10.01]
# min = 1
# max = 0
# for i in my_list:
#     if (i - int(i)) <= min:
#         min = i - int(i)
#     if (i - int(i)) >= max:
#         max = i - int(i)
#         itog= max-min 
# print(itog)

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# number = int(input("Введите число которое хотите преобразовать: "))
# print(bin(number))
# n = int(input())
# print('{0:b}'.format(n))

# Семинар 4

#1. Ax² + Bx + C = 0

# a, b, c = map(int,input().split())
# d = b**2 - 4*a*c
# if d > 0:
#     print(f'x1 = {round((-b+d**0.5)/(2*a), 2)}, x2 = {round((-b-d**0.5)/(2*a), 2)}')
# elif d == 0:
#     print(f'x1 = {round(-b/(2*a), 2)}')
# else:
#     print('Корней нет')

# 2. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

# a, b = map(int, input().split())
# nod = 2
# while True:
#     if a % nod == 0 and b % nod == 0:
#         break
# else:
#     nod += 1

# nok = int(a * b / nod)
# print(f'nod: {nod}, nok: {nok}')

# Homework 4

# 1. Вычислить число c заданной точностью d

# Пример:

# - при d = 0.001, π = 3.141    10^{-1} ≤ d ≤10^{-10}
# d= int(input("введите число с заданной точностью: "))
# import math
# d = math.pi
# print(f'Число с заданной точностью равно: {d}')

# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# import math

# number=int(input("Введите натуральное число : "))
# for i in range(2, int(math.sqrt(number)) + 1):
#     while (number % i == 0):
#         print(i)
#         number //= i
# if (number != 1):
#     print (number)

# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# lst = list(map(int, input("Введите числа: ").split()))
# print(f"Полученный список: {lst}")
# new_lst = []
# [new_lst.append(i) for i in lst if i not in new_lst]
# print(f"Список неповторяющихся элементов: {new_lst}")

# Лекция
# def select(f, col):
#  return [f(x) for x in col]
# def where(f, col):
#  return [x for x in col if f(x)]
# data = '1 2 3 5 8 15 23 38'.split()
# data = select(int, data)
# data = where(lambda e: not e % 2, data)
# data = list(select(lambda e: (e, e**2), data))
# print(data)

# Упрощенный вариант
# data = '1 2 3 5 8 15 23 38'.split()
# data = list(map(int, data))
# data = list(filter(lambda e: not e % 2, data))
# data = list(map(lambda e: (e, e**2), data))
# print(data)

# Семинар 5
#1. Напишите программу, удаляющую из текста все слова, содержащие "абв"

# text = 'этого абв текста все вабвс слова, содерабващие содержащие "абв"'
# newText = ' '.join(list(filter(lambda w: 'абв' not in w, text.split())))
# print(newText)

#2. В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число
# num = list(map(int, "0 1 2 3 4 5 7 8 9 10".split(" ")))
# for i in range(1, len(num)):
#     if num[i]-1 != num[i-1]:
#         print(num[i]-1)
#         break
# сокращенный вариант цикла for
# print([num[i]-1 for i in range(1,len(num)) if num[i]-1 != num[i-1]][0])

# Homework 5.

# 1. Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# from random import randint

# def input_dat(name):
#     x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, введите корректное количество конфет: "))
#     return x


# def p_print(name, k, counter, candies):
#     print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {candies} конфет.")

# player1 = input("Введите имя первого игрока: ")
# player2 = input("Введите имя второго игрока: ")
# candies = int(input("Введите количество конфет на столе: "))
# gamer = randint(0,2)
# if gamer:
#     print(f"Первый ходит {player1}")
# else:
#     print(f"Первый ходит {player2}")

# counter1 = 0 
# counter2 = 0

# while candies > 28:
#     if gamer:
#         k = input_dat(player1)
#         counter1 += k
#         candies -= k
#         gamer = False
#         p_print(player1, k, counter1, candies)
#     else:
#         k = input_dat(player2)
#         counter2 += k
#         candies -= k
#         gamer = True
#         p_print(player2, k, counter2, candies)

# if gamer:
#     print(f"Выиграл {player1}")
# else:
#     print(f"Выиграл {player2}")


# 2.Создайте программу для игры в ""Крестики-нолики"".

# maps = [1,2,3,
#         4,5,6,
#         7,8,9]
 
# victories = [[0,1,2],
#              [3,4,5],
#              [6,7,8],
#              [0,3,6],
#              [1,4,7],
#              [2,5,8],
#              [0,4,8],
#              [2,4,6]]
 
# def print_maps():
#     print(maps[0], end = " ")
#     print(maps[1], end = " ")
#     print(maps[2])
 
#     print(maps[3], end = " ")
#     print(maps[4], end = " ")
#     print(maps[5])
 
#     print(maps[6], end = " ")
#     print(maps[7], end = " ")
#     print(maps[8]) 
# def step_maps(step,symbol):
#     ind = maps.index(step)
#     maps[ind] = symbol
# def get_result():
#     win = ""
#     for i in victories:
#         if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
#             win = "X"
#         if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
#             win = "O"   
             
#     return win
# game_over = False
# player1 = True
 
# while game_over == False:
#     print_maps()
#     if player1 == True:
#         symbol = "X"
#         step = int(input("Игрок 1, ваш ход: "))
#     else:
#         symbol = "O"
#         step = int(input("Игрок 2, ваш ход: "))
 
#     step_maps(step,symbol)
#     win = get_result()
#     if win != "":
#         game_over = True
#     else:
#         game_over = False
#     player1 = not(player1)               
# print_maps()
# print("Победил", win)

# 3.Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# def coding(txt):
#     count = 1
#     res = ''
#     for i in range(len(txt)-1):
#         if txt[i] == txt[i+1]:
#             count += 1
#         else:
#             res = res + str(count) + txt[i]
#             count = 1
#     if count > 1 or (txt[len(txt)-2] != txt[-1]):
#         res = res + str(count) + txt[-1]
#     return res

# def decoding(txt):
#     number = ''
#     res = ''
#     for i in range(len(txt)):
#         if not txt[i].isalpha():
#             number += txt[i]
#         else:
#             res = res + txt[i] * int(number)
#             number = ''
#     return res


# s = input("Введите текст для кодировки: ")
# print(f"Текст после кодировки: {coding(s)}")
# print(f"Текст после дешифровки: {decoding(coding(s))}")

