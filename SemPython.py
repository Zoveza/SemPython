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