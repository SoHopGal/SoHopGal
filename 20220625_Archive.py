#################################################################################
# Archive file.         		                               Date: 25/06/2022 #
# This is open source.			                                                #
# In this file there are examples, questions, etc.								#
# Written by Gal Argov Sofer for Handasaim School.								#
#################################################################################


# Turtle script example
# t = turtle.Turtle('turtle')


# print("א9.")
# str1 = "I loooove Handesaim"
# print(str1[:2:] + str1[2:4:] + str1[7:9:] + " " + str1[10::])


# print("ב1.")
# k = 0
# while k < 12:
#     print(k)
#     k = k + 3

# print("ב2.")
# k = 1
# while k < 12:
#     print(k)
#     k = k * 2

# print("ב3.")
# i = 1
# k = 1
# while k < 12:
#     print("k =", k)
#     print("i =", i)
#     k *=  2
#     i *=  k

# print("ב4.")
# sum = 0
# for i in range(5):
#     for j in range(4):
#         sum = sum + j + i
#         print("i =", i, " j =", j, " sum =", sum)
# print(sum)

# print("ג.")
# i = 9
# k = 0
# while k < 101:
#     if k % i == 0:
#         print(k)
#     k += 1

# myList = ['i', 'g', 'a', 'g', 'r']
# number = myList.count('g')
# print(number)

# print(myList.index('a'))

# myList.append('s')
# print(myList)

# print(myList[1].upper())


# myList.sort()
# print(myList)

# ['0123456789']
# ['FVOSLTRE-K']
# ['S-OXYEWUVL']
# ['4215842760790']
# ['LOVE-YOURSELF']

# numA = 1
# numB = 2
# if numA == numB:
#     print('TRUE')
# else:
#     print('FALSE')
    
# numC = 5
# numD = 2
# numE = numC ** numD
# print(numE)
# numE = numD ** numC
# print(numE)

# num = 5
# num += 4
# print(num)

# num = 9 
# def myFunc(num):
#     if num <= 1 or num >= 12:
#         print("Error Input")
#     else:
#         for i in range(101):
#             if i % num == 0:
#                 print(i)
# myFunc(5)
# num = 10

# for i in range(2, 101):
#     print("bbb")
#     if i % num == 0:
#         print(i)



# def func(num):
#     if 2 <= num and num <= 11 and type(num) == int:
#         # print("aaa")
#         result = []
#         for i in range(2, 101):
#             # print("bbb")
#             if i % num == 0:
#                 # print(i)
#                 result.append(i)
#         return result
#     else:
#         print("wrong Input")
# num = int(input("number"))
# print(func(num))

# number = int(input("enter number"))
# while number > 11 or number < 2:
#     number = int(input("enter number again"))
# for i in range(2, 101, 1):
#     if i % number == 0:
#         print(i)

# def func():
#     num = int(input("enter"))
#     new_num = 2
#     for number in range(2, 101):
#         if new_num % num == 0:
#             print(new_num)
#         new_num += 1
# func()

# def get_num():
#     x = int(input("enter"))
#     if (x) >=2 and x < 12:
#         for i in range(2, 101):
#             if ((i) % x == 0):
#                 print(i)
#         else:
#             print("invalid")
# get_num()

# num = int(input("enter"))
# if (num < 2) or (num > 11):
#     print("invalid")
# else:
#     for i in range(2, 101):
#         if i % num == 0:
#             print(i)

# def func(num):
#     if (num < 2) or (num > 11):
#         print("invalid")
#     else:
#         for i in range(2, 100):
#             if i % num == 0:
#                 print(i)
# func(10)

# num = int(input("enter"))
# for x in range(2, 100):
#     if (x % num) == 0:
#         print(x)

# def fun():
#     num = int(input("enter"))
#     if (num < 2) or (num > 11):
#         print("invalid")
#     else:
#         for i in range(2, 101):
#             if i % num == 0:
#                 print(i)
#             # else:
#             #     print("isnt good")
# fun()

# num = input("enter")
# # print(num.isdigit())
# # num = int(num)
# if (num.isdigit() and num >= 2) and (num <= 11):
#     num = int(num)
#     for i in range(2, 101):
#         if i % num == 0:
#             print(i)
# else:
#     "invalid"

# def func():
#     num = int(input("enter"))
#     if num > 11 or num < 2:
#         print("invalid")
#     else:
#         for i in range(num, 101, num):
#             print(i)
# func()

# num = int(input("enter"))
# while num < 2 or num > 11:
#     num = int(input("enter1"))
# for i in range(2, 101):
#     if i in range(2, 101):
#         if (i % num == 0):
#             print(i)

# def my_func():
#     num_1 = int(input("enter"))
#     if num_1 > 11 or num_1 < 2:
#         print("invalid")
#     else:
#         for i in range(2, 101):
#             if i % num_1 == 0:
#                 print(i)
# my_func()

# def recove_int(message):
#     string = input(message)
#     while string.isdigit() != True:
#         string = input("enter1")
#     return int(string)
# num = (recove_int("enter"))
# for i in range(2, 101):
#     if i % num == 0:
#         print(i)
#     else:
#         continue

# num = input("enter")
# # print(num.isdigit())
# # num = int(num)
# if (num.isdigit()) and num >= 2 and (num <= 11):
#     num = int(num)
#     for i in range(2, 101):
#         if i % num == 0:
#             print(num)
# else:
#     "invalid"

# num = int(input("enter"))
# if num >= 2 and num <= 11:
#     for i in range(2, 101):
#         if(i % num == 0):
#             print(i)
# else:
#     print("invalid")


# num = int(input("enter"))
# for x in range(2, 101):
#     if (x % num) == 0:
#         print(x)

# num = int(input("enter"))
# while num < 2 or num > 11:
#     num = int(input("enter1"))
# for i in range(0, 101, num):
#     if i < 2:
#         continue
#     else:
#         print(i)

# def myfunc(num):
#     for i in range(2, 101):
#         if (i % num == 0):
#             print(i)
# num = input()
# num = int(num)
# myfunc(num)

# def ex():
#     num = int(input("enter"))
#     if num >= 2 and num <= 11:
#         for i in range(2, 101):
#             if i % num == 0:
#                 print(i)
# ex()

# num = int(input("enter"))
# if num > 1 and num < 12:
#     for i in range(2, 100):
#         if i % num == 0:
#             print(i)

# number = int(input("enter"))
# if (number < 2 or number > 11) or (number.isdigit() == False):
#     print("Invalid")
#     number = int(input("enter1"))
#     while (number < 2 or number > 11):
#         number = int(input("enter2"))
# number = int(number)
# for i in range(2, 101):
#     if i % number == 0:
#         print(i)

# def my_f(number):
#     while number % 1 != 0:
#         number = input("enter")
#     number = int(number)
#     for i in range(2, 101):
#         if i % number == 0:
#             print(i)
# my_f(1)

# def reciveNatureNum():
#     _input = input("enter")
#     while (_input.isdigit() == False) or not (_input.isdigit() == True and (int(_input) >= 2 and int(_input) <= 11)):
#         _input = input("enter1")
#     return int(_input)
# num = reciveNatureNum()
# for i in range(2, 101, 1):
#     if i % num == 0:
#         print(i)

# num = int(input("enter"))
# if num > 2 and num < 11:
#     for j in range(2, 101):
#         for i in range(100 // num):
#             print(num, j, i, j * num)

# num = float(input("enter"))
# if num < 12 and num > 1:
#     while (100 // num < 12 and 100 // num > 1):
#         print(float(100 // num))
#         num = num + num
# else:
#     print("Invalid")


# def func(num):
#     x = 2
#     if ((num >= 2) and (num <=11)):
#         while x <= 100:
#             if (x % num == 0):
#                 print(x)
#             x = x + 1
#     else:
#         print("Invalid")
# num = int(input("Enter"))
# func(num)


# sum = []
# num = int(input("Enter"))
# while num < 2 or num > 11:
#     print("Enter1")
#     num = int(input("Enter"))
# for i in range(2, 100):
#     if i % num == 0:
#         sum.append(i)
# print(sum)

# def super_gal(num):
#     assert 11 >= num  >= 2, "Enter"
#     nums = []
#     for n in range(2, 101):
#         if n % num == 0:
#             nums.append(n)
#     return nums
# num = int(input("Enter"))
# print(super_gal(num))

# def func1(num):
#     for i in range(2, 101):
#         if i % num == 0:
#             print(i)
# num = input("Enter")
# if (int(num) >= 2 and int(num) <= 11):
#     num = int(num)
#     func1(num)
# else:
#     print("Invalid")

# def job(num):
#     if num.isdigit and num.count(".") == 0:
#         num = int(num)
#         if num >= 2 and num <= 11:
#             for i in range(2, 101):
#                 if i % num == 0:
#                     print(i)
#         else:
#             print("Invalid")
#     else:
#         print("Invalid2")
# job(input("Enter"))

# num = 0
# num1 = int(input("Enter"))
# num2 = 0
# while num <= 100:
#     num2 = num2 + 1
#     print(num * num2)
#     num = num1 * num2

# k = " "
# def ex():
#     if num < 2 or num > 11:
#         print("Invalid")
#     for i in range(2, 101,):
#         if i % num == 0:
#             print(i, ",")
# num = int(input("Enter"))
# ex()

# def func(num):
#     if (num < 2) or (num > 11):
#         print("invalid")
#     else:
#         for i in range(2, 100):
#             if i % num == 0:
#                 print(i)
# func(10)

# def ex3(num):
#     if (num.isdigit() == True):
#         num = int(num)
#         if (2 <= num <= 100):
#             for i in range(2, 101):
#                 if i % num == 0:
#                     print(i)
# num = input("Enter")
# ex3(num)

# def func(num):
#     num = int(input("Enter"))
#     if (2 <= num and 11 >= num):
#         i = 2
#         while (i <= 100):
#             i += 1
#             if (i % num == 0):
#                 print(i)
#     else:
#         print("Invalid")
# num = 0
# func(num)

# def ex(number):
#     if number <= 1 or number >= 12:
#         print("Invalid")
#     else:
#         new = 0
#         counter = 0
#         while new <= 100:
#             for i in range(2, 101):
#                 new = number * i
#                 print(new)
# ex(7)

# def func(num):
#     # while num.isdigit() == False:
#     #     num = int(input("Enter1"))
#     while num < 2 or num > 11:
#         num = int(input("Enter2"))
#     for i in range(2, 101):
#         if i % num == 0:
#             print(i)
# num = int(input("Enter"))
# func(num)

# num = int(input("Enter"))
# for i in range(2, 101):
#     if i % num == 0:
#         print(i)

# num = int(input("Enter"))
# def func(num):
# if (11 < num or num < 2):
#     print("Invalid")
# else:
#     num2 = 2
#     while (num2 <= 100):
#         if (num2 % num == 0):
#             print(num2)
#         num2 += 1
# func(num)

# num = int(input("Enter"))
# if (num >= 2) and (num <= 11):
#     # if num == int:
#         div_num = num
#         while div_num < 101:
#             print(div_num)
#             div_num = div_num + num

# def NaturalNumbers(int1):
#     int_check = int(input(int1))
#     if (int_check < 2 or int_check > 11):
#         print("Invalid")
#     # elif (int_check.count(".") > 0):
#     #     print("Invalid")
#     else:
#         # int_check = int(int_check)
#         for index in range(2, 101):
#             if (index % int_check == 0):
#                 print(index)
#             else:
#                 continue
# NaturalNumbers(5)

# num = input("Enter")
# # while (num < 2 or num > 11):
# #     num = int(input("Enter1"))
# while num.isdigit() != True and (num < 2 or num > 11):
#     num = int(input("Enter1"))
# num = int(num)
# for number in range(2, 100):
#     if number % num == 0:
#         print(number)


# str1 = (int(input("Enter")))
# for i in range(2, 12):
#     if str1 != i:
#         print("Invalid")
#     else:
#         for i in range(2, 101):
#             if i % str1 == 0:
#                 print(i, end=" ")

# def func():
#     num = int(input("Enter"))
#     # if num.isdigit() == "False":
#     #     print("Invalid")
#     if num > 11 or num < 2:
#         print("Invalid1")
#     else:
#         for i in range(2, 101):
#             num = int(num)
#             if i % num == 0:
#                 print(i)
#             else:
#                 continue
# func()

# def a1():
#     num = int(input("Enter"))
#     if num / 1 != 0:
#         x = 2
#         while x <= 100:
#             if x / num == x // num:
#                 print(x)
#             x += 1
# a1()

# def ex():
#     num = int(input("Enter"))
#     if (num % 1 == 0) and (num >= 2) and (num <= 11):
#         n = 2
#         for i in range(2, 101):
#             if n % num == 0:
#                 print(n)
#             n += 1
#             if n == 101:
#                 break()
#     else:
#         print("Invalid")
# ex()

# number = int(input("Enter"))
# if number <= 11 and number >= 2:
#     for i in range(2, 101):
#         if i % number == 0:
#             print(i)
# else:
#     print("Invalid")

# def ex(num):
#     num = input("Enter")
#     while num.isdigit() != True:
#         num = input("Enter1")
#     return int(num)
# ex(num)
# if num >= 0:
#     new_num = num
#     for i in range(2, 101):
#         if i % num == 0:
#             print(i)
#             # new_num = new_num + i
#     # print(new_num)
# else:
#     print("Invalid")

# def algo(natural):
#     countdown = 100
#     while countdown >= 2:
#         if countdown % natural == 0 and natural <= 11 and natural >= 2:
#             print(countdown)
#         countdown = countdown - 1

# natural = int(input("Enter"))
# algo(natural)
# # x = algo(natural)
# # print(x)

# num1 = int(input("Enter"))
# while (num1 < 2 or num1 > 11):
#     num1 = int(input("Enter1"))
# for number in range(101):
#     if (number % num1 == 0):
#         print(number)

# def func(num):
#     if(str(num).isdigit()):
#         if int(num) in range(2, 12):
#             num = int(num)
#             for i in range(2, 101):
#                 if i % num == 0:
#                     print(i)
#         else:
#             print("Invalid")
#     else:
#         print("Invalid")
# func("g")

# num = int(input("Enter"))
# if (num > 1) and (num < 12):
#     for i in range(2, 101):
#         if i % num == 0:
#             print(i)
# else:
#     print("Invalid")

# num = input("Enter")
# if (num.isdigit() == True) and (int(num) >= 2) and (int(num) <= 11):
#     for i in range(2, 101):
#         if i % int(num) == 0:
#             print(i)
# else:
#     print("Invalid")

# num = int(input("Enter"))
# if (num > 1) and (num < 12):
#     for i in range(2, 101):
#         if i % num == 0:
#             print(i)
# else:
#     print("Invalid")

# def ex():
#     number = int(input("Enter"))
#     while number.isdigit != True:
#         n = 10
#     if (10 / 100):
#         print("true")
#     n = n + 1
# ex()

# num = 2
# number = int(input("Enter"))
# if 11 >= number >= 2:
#     while num <= 100:
#         if num % number == 0:
#             print(num)
#         # print(number / num)
#         # print(num / number)
#         num = num + 1
# else:
#     print("Invalid")



# ==============כיתות ז===============
# # Q1_A
# num1 = 5
# num2 = 6
# num3 = 7
# # Q1a
# if ((num1 < num2) or (num2 < num3)):
#     print("1.True")
# else:
#     print("1.False")
# # Q1b
# if ((num1 < num2) and (num3 < num2)):
#     print("2.True")
# else:
#     print("2.False")
# # Q1c
# if ((num2 % 2 == 0) and (not (num1 > num3))):
#     print("3.True")
# else:
#     print("3.False")
# # Q1d
# if ((num3 + 1 == 8) and (num3 % 2 == 0)):
#     print("4.True")
# else:
#     print("4.False")
# # Q1e
# if ((num2 == 7) or (num1 > 5)):
#     print("5.True")
# else:
#     print("5.False")

# # Q1_B
# status = 1
# level = 7

# if status == 1:
#     if status > level:
#         print("one")
#     else:
#         print("two")
#     print("three")
# else:
#     print("four")
# print("five")

# # Q2_A
# word1 = "lo"
# word2 = "han"
# word3 = "v"
# word1 = word1 + word3[0]
# print(word1)
# if (len(word1) % 3 == 0):
#     word1 = word1 + "e"
# else:
#     word1 = word1 + "a"
# if (len(word2) < 4):
#     word2 = word2 + "dasa"
# else:
#     word2 = word2 + "ing"
# print(word1, word2)

# # Q2_B
# secret = ""
# if (len("comp") == len("uter")):
#     secret = "computer"
# else:
#     secret = "secret"
# if (len("science") % 2 == 0):
#     secret = secret + "secret"
# else:
#     secret = secret + "science"
# if ("a" in "scratch"):
#     secret = secret + "1"
# else:
#     secret = secret + "2"
# print(secret)

# # Q3
# count = 0
# for i in range(5):
#     num = int(input("Enter num"))
#     if (num % 2 == 0):
#         count += 1
#     else:
#         count -= 1
# print(count)

# # Q4
# sum = 0
# result = 0
    
# for i in range(5):
#     num = int(input("Enter num"))
#     result = num % 10
#     sum += result
#     print(sum, num, result)
# print(sum)

# # Q5
# def draw(size):
#     for i in range(4):
#         t.left(90)
#         t.forward(size)

# t.penup
# t.goto(0, 0)
# t.pendown
# draw(50)
# draw(100)
# draw(150)

# # Q6
# t.penup()
# t.goto(0, 100)
# t.pendown()
# t.goto(100, 100)
# t.goto(0, 0)
# t.goto(100, 0)

# num1 = 2
# num2 = num1 + 5
# num1 = num1 + num2 + 3
# print("num1 = ", num1, "num2 = ", num2)

# num = 3
# num = 10
# num = 3 + num
# print("num = ", num)

# string = "Yes We Can!!!"
# print(string[4])
# print(len(string))
# print(string[-3])
# print(string[::2])
# print(string[4:-3])
# print(string[:])

# def num_even():
#     count = 0
#     index = 0
#     while index < 10:
#         num = int(input("Enter"))
#         if num <= 99 and num >= 10:
#             count = count + 1
#         index = index + 1
#     print("count = ", count)
# num_even()

# t.shape("square")
# size = 100
# t.pendown()
# for index in range(4):
#     for item in range(4):
#         t.forward(size)
#         t.left(90)
#     size = size - 20

# first = 1
# second = 1
# counter = 3
# print("Fibo item 1 is ", first)
# print("Fibo item 2 is ", second)
# while counter <= 25:
#     third = first + second
#     first = second
#     second = third
#     print("Fibo item", counter, "is", third)
#     counter = counter + 1

# def exs8():
#     counter = 0
#     for k in range(5):
#         gradeA = int(input("Enter A"))
#         gradeB = int(input("Enter B"))
#         if (gradeB >= gradeA):
#             counter += 1
#     if counter > 2:
#         print("good")
#     else:
#         print("bad")
# exs8()

# for row in range(4):
#     for col in range(4):
#         if ((row + col) % 2 == 0):
#             print("O")
#         else:
#             print("X")
#     print("\n")

# print("ב4.")
# sum = 0
# for i in range(8):
#         sum = sum + i
#         print("i =", i, " sum =", sum)
# print(sum)

# =============================================================================
# כיתה ח'
# Part A

# Q2
# x = 30.1
# print(type(x))
# y = 301
# print(type(y))

# Q5
# num = 5 ** 2
# print(num)
# num2 = 2 ** 5
# print(num2)

# Q6
# num = 5
# num += 4
# num = 5
# num *= 2

# Q7
# checkChar = 'l'
# myStr = "Hello"
# print(myStr.count(checkChar))

# Q8
# numA = 1
# numB = 2
# if numA == numB:
#     print('TRUE')
# else:
#     print('FALSE')

# Q9
# str1 = "I loooooove Handasaim"
# print(str1[:2:] + str1[2:4:] + str1[7:9:] + " " + str1[10::])
# print(str1[:4:] + str1[9:12:] + str1[12::])

# Q10
# num = 100 % 9
# print(num)
# num = 100 % 12
# print(num)


# Q11
# t = turtle.Turtle('turtle')
# n = 6
# m = 3

# t.width(5)
# t.color('red')

# for i in range(n):
#     t.forward(100)
#     t.left(180 - (180 * (n - 2)) /  n)

# for i in range(m):
#     t.forward(100)
#     t.left(180 - (180 * (m - 2)) /  m)

# t.penup()

# turtle.done()

# Part B
# Q1
# k = 0
# while k < 14:
#     print(k)
#     k = k + 4
# k = 0
# while k < 15:
#     print(k)
#     k = k + 3

# # # Q2
# k = 1
# while k < 50:
#     print(k)
#     k = k * 3
# k = 1
# while k < 126:
#     print(k)
#     k = k * 5

# # Q3
# i = 1
# k = 1
# while k < 12:
#     print("k =", k)
#     print("i =", i)
#     k *= 2
#     i *= k
# i = 1
# k = 1
# while k < 28:
#     print("k =", k)
#     print("i =", i)
#     k *= 3
#     i *= k

# # Q4
# sum = 0
# for i in range(8):
#         sum = sum + i
#         print("i =", i, " sum =", sum)
# print(sum)

# sum = 0
# for i in range(1,9,1):
#         sum = sum + i
#         print(i < 9, "i =", i, " sum =", sum)
# print(sum)


# sum = 0
# for i in range(5):
#     for j in range(4):
#         sum = sum - j + i
#         print("i =", i, " j =", j, " sum =", sum)
# print(sum)


# ===========================================

# Q1_A
# num1 = 3
# num2 = 4
# num3 = 6
# if (num1 < num2) or (num2 < num3):
# 	print("True")
# else:
# 	print("False")

# if (num1 < num2) and (num3 < num2):
# 	print("True")
# else:
# 	print("False")

# if (num3 % 2 == 0) and (not (num3 < num1)):
# 	print("True")
# else:
# 	print("False")

# if (num1 * 2 == num3) and (num3 % 3 == 0):
# 	print("True")
# else:
# 	print("False")

# if (num2 == 7) or (num1 > 10):
# 	print("True")
# else:
# 	print("False")

# Q1_B
# status = 2
# level = 4

# if status <= 1:
#     if status < level:
#         print("one")
#     else:
#         print("two")
#     print("three")
# else:
#     print("four")
# print("five")


# rishoni = 0
# num = int(input("Enter"))

# if (num < 2 or num > 100):
#     print("Error1")
# else:
#     for i in range(2, num):
#         if (num % i != 0):
#             for j in range(num + 1, 101):
#                 if (num % i != 0):
#                     rishoni = 1
# print(rishoni)


# def rational(n):
#     if (n % 2 == 0):
#         print('0')
#     else:
#         a = 3
#         while a < 100:
#             if (n % a == 0):
#                 print('0')
#             a += 2
#         print('1')

# rational(25)


# def myFunc(num):
#     for i in range(2, 101):
#         if i % num == 0:
#             print(1)
#         else:
#             print(0)

# myFunc(99)


# def function():
#     num = int(input("Enter"))
#     if num < 2 or num > 100:
#         print("Error1")
#     else:
#         if (num % 2 == 0 or num % 5 == 0) and (num != 2 and num != 3):
#             print("0")
#         else:
#             print("1")
            
# function()



# def function():
#     num = int(input("Enter"))
#     if num < 2 or num > 100:
#         print("Error1")
#     else:
#         if (num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0):
#             print("0")
#         else:
#             print("1")
            
# function()

# Q2
# x = []
# print(type(x))

# # Q4
# myStr = "exam"
# print(myStr[2])

# # Q5
# y = 5
# if (y > 5 or y < 4):
#     print("True")
# else:
#     print("False")

# # Q6
# drawing a 6 point star using loops
# import turtle

# t = turtle.Turtle()
# polygon = 3
# a = 180 - (180 * (polygon - 2)) / polygon
# length = 100
# start = 1
# end = 4
# rightAngle = 90
# distance = 2 * 86

# for sides in range(start, end):
#     t.right(a)
#     t.forward(length)

# t.right(rightAngle)
# t.penup()
# t.forward(distance / polygon)
# t.pendown()
# t.right(rightAngle)

# for sides in range(start, end):
#     t.forward(length)
#     t.right(a)

# t.penup()

# t = turtle.Turtle()
# t.setheading(180)
# t.forward(100)

# # Q8
# word1 = "Hello World!"
# word2 = "hello world!"
# print(word1.lower() == word2)

# # Q9
# print("Red" > "Green")

# # Q10
# myVar = "G"
# print(myVar * 5)

# def calc(x, y):
#     summ = x + y
#     sub = x - y
#     mul = x * y
#     if y != 0:
#         div = x / y
#     return summ, sub, mul, div

# def calc1(x, y):
#     summ = x - y
#     sub = x + y
#     mul = x + y
#     if y > 0:
#         div = x - y
#     return summ, sub, mul, div
    
# def calc2(x, y):
#     summ = x / y
#     sub = x - y
#     mul = x + y
#     if y != 0:
#         div = x * y
#     return summ, sub, mul, div

# def calc3(x, y):
#     summ = x + y
#     sub = x - y
#     mul = x + y
#     if y != 0:
#         div = x + y
#     return summ, sub, mul, div
    
# def main():
#     a, b, c, d = calc(5.5, 2)
#     print(a, b, c, d)
#     print(c - b)

#     a, b, c, d = calc(5, 3)
#     print(a, b, c, d)
#     print(c / b)

#     a, b, c, d = calc1(1.875, 1.875)
#     print(a, b, c, d)
#     print(c + b)

#     a, b, c, d = calc2(2.75, 0.25)
#     print(a, b, c, d)
#     print(c * b)
    
#     a, b, c, d = calc3(3.75, 3.75)
#     print(a, b, c, d)
#     print(c - b)

#     a, b, c, d = calc(12, 1.5)
#     print(a, b, c, d)
#     print(c - b)

# main()

# def test(x, y, z):
#     val = x + y + z
    
#     if x < -3:
#         if y < z:
#             val = x * y
#         else:
#             val = y * z
#     elif x > 2:
#         val = x * z
#     return val
    
# print(test(3, 4, 5))

# def getMiddleThreeChars(str1):
#     print("Original String is", str1)
#     mi = int(len(str1) / 2)
#     res = str1[mi - 1:mi + 2]
    
#     print(mi, "Middle three chars are:", res)

# getMiddleThreeChars("HANDASA")
# getMiddleThreeChars("HANDASAIM")

# ====================================================================

# fruit = ['pear', ['apple', 'pear'], 'grapefruit', 'apple']
# print(fruit.index('apple'))


# grocery_list = ['software', 'computer', 'engineering']
# for idx, val in enumerate(grocery_list):
#     print("%s: %s" % (idx, val))

# def func(x = []):
#     x.append("SE")
#     print(x)
    
# func()
# func()
# func()

# def azby(str):
#     abc = "abcdefghijklmnopqrstuvwxyz"
#     msg = ""
#     str = str.lower()
    
#     for letter in str:
#         if letter == ' ':
#             msg += letter
#         else:
#             p = abc.index(letter)
#             msg += abc[-1 * (p + 1)]
#     return msg

# def main():
#     txt = "Handasaim"
#     msg = azby(txt)
#     print("Encrypted:", msg)
    
#     msg1 = azby(txt)
#     print("Decrypted:", msg1)

# main()



# ####################################################### #
# AMAT test - Grade 4 (כיתה ח)
# # Q1
# # 1
# num1 = 3
# num2 = 10
# num1 = num2
# num2 = num1
# print("num1 = ", num1, "num2 = ", num2)

# # 2
# number = "12345"
# print("4" in number)

# # 3
# msg1 = "He" + "l"*2 +"o"
# msg2 = " world"
# print(msg1 + msg2)
# print(len(msg1))

# # 4
# number = 123
# print(number // 100)
# print(number % 100 % 10)
# print(number % 10)

# # Q2
# a = 10
# b = 15
# c = 0
# # 1
# print(a >= b or b == c)

# # 2
# print(a % 5 == 0 and b // 5 > c)

# # 3
# print(a < 0 or (b == c + 15 and a >= c))

# # 4
# print(a % 1 == c % 2 and b % 3 > a % 3)

# # 5
# print(a != b and b != c)

# # Q3
# # 1
# i = 1
# while i < 4:
#     print('wow')
#     i += 1

# # 2
# for item in range(6):
#     if item % 2 == 1:
#         print(item * item)
        
# # 3
# for item in range(9, 0, -3):
#     print(item)
    
# # 4
# x = 5
# i = 1
# while i < 4:
#     x -= 1
#     i += 1
# print(i, x)

# Q4
# # 1
# for x in range(100, 200, 2):
#     print(x)
# # 2
# for x in range(1, 10):
#     print(x - 1)
# # 3
# for x in range(4, 5):
#     print(x + 3)
# # 4
# for x in range(-5, 6):
#     print(x + 6)
# a
# x = 0
# while x < 9:
#     print(x)
#     x += 1
# # b
# for x in range(7, 8):
#     print(x)
# # c
# for x in range(100, 200):
#     if x % 2 == 0:
#         print(x)
# d
# x = 1
# while x < 12:
#     print(x)
#     x += 1
    
# # Q5
# def calc_avg():
#     sum = 0
#     count = 0
#     grade = int(input("Bla"))
#     while grade > 0:
#         sum += grade
#         count += 1
#         grade = int(input("Bla"))
#         avg = sum / count
#     print(avg)
# calc_avg()

# # Q6
# def perfect_number():
#     num = int(input("Please enter a number:"))
#     sum = 0
#     x = 1
#     while x < num:
#         if num % x == 0:
#             sum = sum + x
#         x = x + 1
#     if sum == num:
#         print("Perfect Number")
#     else:
#         print("Not Perfect Number")
# perfect_number()


# # Q6
# def perfect_number():
#     num = int(input("Please enter a number:"))
#     sum = 1 - num
#     x = 1
#     print("sum:", sum)
#     while x < num:
#         print("num:", num, "\tsum:", sum, "\tx:", x, "\tnum // x:", num // x, "\tnum / x:", num / x)
#         if num / x == num // x:
#             sum = sum + num / x
#         x = x + 1
#     if sum == num:
#         print("Perfect Number")
#     else:
#         print("Not Perfect Number")
# perfect_number()
    
# # Q7
# def find_location():
#     id_number = int(input("Please enter ID number:"))
#     digit = int(input("Please enter a digit:"))
#     found = False
#     for index in range(0, 10):
#         if id_number % 10 == digit:
#             print(index + 1)
#             found = True
#         id_number = id_number // 10
#     if found == False:
#         print("-1")
# find_location()

# # Q8
# # 1
# for x in range(360):
#     t.left(1)
#     t.forward(1)

# # 2
# for index in range(3):
#     t.forward(100)
#     t.left(360 / 3)
    
# # 3
# t.left(180)
# t.forward(80)
# t.left(90)
# t.forward(70)
# for index in range(4):
#     t.forward(80)
#     t.left(90)
    
# # 4
# for index in range(4):
#     t.left(90)
#     t.forward(90)
#     t.right(90)
#     t.forward(50)
    
# # Q9
# def create_skip2str():
#     st = input("Please enter a string:")
#     skip2str = ""
#     for letter in range(0, len(st), 3):
#         skip2str = skip2str + st[letter]
#     print(skip2str)
# create_skip2str()
    
# ####################################################### #
# AMAT test - Grade 5 (כיתה ט)
# # Q1
# # 1
# arr = [32, 51, 13, 23, 30]
# arr.sort()
# tmp = arr[-1]
# print(tmp)

# # 2
# arr = [32, 51, 13, 23, 30]
# tmp = arr[0]
# for item in arr:
#     if item > tmp:
#         tmp = item
# print(tmp)

# # 3
# arr = [32, 51, 13, 23, 30]
# tmp = max(arr)
# print(tmp)

# # 4
# arr = [32, 51, 13, 23, 30]
# arr.sort(reverse = True)
# tmp = arr[0]
# print(tmp)

# # Q2
# # 1
# list1 = ['Israel', 'Japan', 'Italy', 'Jordan', 'Israel', 'Portugal']
# list1.remove('Israel')
# print(list1)
# print(len(list1))

# # 2
# list1 = ['Israel', 'Japan', 'Italy', 'Jordan', 'Israel', 'Portugal']
# for i in range(len(list1)):
#     if 'Israel' in list1:
#         list1.remove('Israel')
# print(list1)
# print(len(list1))

# # 3
# list1 = ['Israel', 'Japan', 'Italy', 'Jordan', 'Israel', 'Portugal']
# count1 = list1.count('Israel')
# for i in range(count1):
#     list1.remove('Israel')
# print(list1)
# print(len(list1))

# # 4
# list1 = ['Israel', 'Japan', 'Italy', 'Jordan', 'Israel', 'Portugal']
# count = list1.index('Israel')
# list1 = list1[count + 1:]
# print(list1)
# print(len(list1))

# # 5
# list1 = ['Israel', 'Japan', 'Italy', 'Jordan', 'Israel', 'Portugal']
# list2 = []
# for state in list1:
#     if not state == 'Israel':
#         list2.append(state)
# list1 = list2
# print(list1)
# print(len(list1))

# # Q3
# min = 10
# num = int(input("4 digit natural number:"))
# tmp = num % 10
# for i in range(4):
#     num = num // 10
#     if min > tmp:
#         min = tmp
#     tmp = num % 10
# print(min)

# # Q4
# # 1
# def f1(lst):
#     for x in lst:
#         if x < 0:
#             print(x)

# lst = [-7, 2, 10, 5, -2, 8, -1, 0]
# print("f1: ")
# f1(lst)

# # 2
# def f2(lst):
#     for x in lst[::-1]:
#         if x < 0:
#             print(x)

# lst = [-7, 2, 10, 5, -2, 8, -1, 0]
# print("f2: ")
# f2(lst)

# # 3
# def f3(lst):
#     for i in range(len(lst) - 1, -1, -1):
#         if lst[i] < 0:
#             print(lst[i])

# lst = [-7, 2, 10, 5, -2, 8, -1, 0]
# print("f3: ")
# f3(lst)

# # 4
# def f4(lst):
#     for i in range(len(lst)):
#         if lst[i] < 0:
#             print(i)

# lst = [-7, 2, 10, 5, -2, 8, -1, 0]
# print("f4: ")
# f4(lst)

# # Q5
# # 1
# import queue
# q1 = queue.Queue()
# q2 = queue.Queue()
# q1.put(10)
# q1.put(20)
# q1.put(30)
# q1.put(40)
# while not q1.empty():
#     q2.put(q1.get())
# while not q2.empty():
#     q1.put(q2.get())
# x = q1.get()
# print(x)

# # 2
# import queue
# q1 = queue.Queue()
# list1 = []
# q1.put(10)
# q1.put(20)
# q1.put(30)
# q1.put(40)
# while not q1.empty():
#     list1.append(q1.get())
# for item in list1:
#     q1.put(item)
# x = q1.get()
# print(x)

# # 3
# import queue
# q1 = queue.Queue()
# q1.put(10)
# q1.put(20)
# q1.put(30)
# q1.put(40)
# l = []
# s = 0;
# while not q1.empty():
#     x = q1.get()
#     l.append(x)
#     s = s + x
# print(s)

# # 4
# import queue
# q1 = queue.Queue()
# list1 = []
# q1.put(10)
# q1.put(20)
# q1.put(30)
# q1.put(40)
# temp = q1.get() + q1.get()
# q1.put(temp)
# temp = q1.get() + q1.get()
# q1.put(temp)
# print(q1.get())

# # Q6
# def change_password(password):
#     temp = password[0].capitalize()
#     temp = temp + password[1:]
#     temp = temp.replace('a', '@')
#     temp = temp.replace('i', '1')
#     print(temp)
# change_password('telaviv')
# change_password('mazaltov')

# # # Q7 - problam with this question
# # 1
# def is_exist(lst, tav):
#     for item in lst:
#         if tav not in item:
#             print('OUT')
#             return
#     print('IN')

# is_exist(['ai', 'bi', 'i'], 'i')

# def is_exist2(lst, tav):
#     for item in lst:
#         if tav not in item:
#             print('IN')
#             return
#     print('OUT')

# is_exist2(['ai', 'bi', 'i'], 'i')

# # 2

# # Q8
# # 1
# def select(lst1, party_time):
#     lst1_size = len(lst1)
#     return_lst = []
#     sum_time = 0
#     for item in lst1:
#         if (sum_time + item) < (party_time * 60):
#             return_lst.append(item)
#             sum_time = sum_time + item
#     print(return_lst)

# lst1 = [120, 150, 200, 300, 190, 170, 250, 210, 230]
# select(lst1, 10)
# lst2 = [190, 150, 240, 220, 20, 270]
# select(lst2, 14)

# # 2
# def shuffle(lst1):
#     import random
#     lst_size = len(lst1)
#     shift_size = int(lst_size * 10)
#     for i in range(shift_size):
#         random_index = random.randrange(0, lst_size)
#         item = lst1.pop(random_index)
#         lst1.append(item)
#     print(lst1)

# lst1 = [120, 150, 200, 300, 190, 170, 250, 210, 230]
# shuffle(lst1)

# x = "3x4m"
# print(type(x))

# myStr = "3x4m"
# print(myStr[2])

# word1 = "Hello World!"
# word2 = "hello world!"
# print(word1.upper() == word2)

# print("AAA" > "AA")

# myVar = "G"
# print(chr(ord(myVar) + 5))

# fruit = ['pear', ['apple', 'pear'], 'grapefruit', 'apple']
# fruit.reverse()
# print(fruit)

# x = "[]"
# print(type(x))


# t = turtle.Turtle('turtle')

# radius = 170
# angle = 45

# t.up()
# t.width(10)
# t.goto(0, -radius)
# t.down()

# t.circle(radius)
# t.left(angle * 2)
# t.forward(radius * 2)
# t.up()
# t.left(angle * 4)
# t.forward(radius)
# t.right(angle)
# t.down()
# t.forward(radius)
# t.up()
# t.backward(radius)
# t.left(angle * 2)
# t.down()
# t.forward(radius)
# t.up()

# t.goto(0, 0)

# turtle.done()

# def calc(x, y):
#     summ = x + y
#     sub = x - y
#     mul = x * y
#     if y != 0:
#         div = x / y
#     return summ, sub, mul, div

# def main():
#     a, b, c, d = calc(5, 2)
#     print(a, b, c, d)
#     print(a - d)

# main()



# def solve(s, t):
#     res = ""
#     i = 0
#     m = min(len(s), len(t))
#     print("res:", res, "\t\ti:", i, "\t", "m:", m, "\t", "len(res):", len(res))

#     while i < m:
#         res += s[i] + t[i]
#         i += 1
#         print("res:", res, "\ti:", i, "\t\t", "len(res):", len(res))
#     return res + s[i:] + t[i:]

# s = "abc"
# t = "xyz"

# print("The function returns:", solve(s, t))



# myList = [2, 5, 6, 9, 3, 1, 7]
# myBool = False

# for i in range(len(myList) - 2):
#     print(i, ":", myList[i] + myList[i + 2] - myList[i + 1])
#     if myList[i] + myList[i + 2] - myList[i + 1] == 0:
#         myBool = True

# print(myBool)

# import queue

# q1 = queue.Queue()
# q2 = queue.Queue()
  
# q1.put(11)
# q1.put(5)
# q1.put(3)
# q1.put(2)
# q1.put(9)

# print("Queue 1:", end = " ")
# while (q1.empty() == False):
#     print(q1.queue[0], end = " ")
#     q2.put(q1.get())
    
# n = q2.qsize()

# for i in range(n):
#     x = q2.get()
#     for j in range(n - 1):
#         y = q2.get()
#         if x > y:
#             q2.put(y)
#         else:
#             q2.put(x)
#             x = y
#     q2.put(x)

# print()
# print("Queue 2:", end = " ")
# while (q2.empty() == False):
#     print(q2.queue[0], end = " ")
#     q2.get()


# def albm(p_text):
#     atom = "abcdefghijklm"
#     ntoz = "nopqrstuvwxyz"
#     c_text = ""
#     for letter in p_text:
#         if letter in atom:
#             num_letter = atom.find(letter)
#             c_letter = ntoz[num_letter]
#         elif letter in ntoz:
#             num_letter = ntoz.find(letter)
#             c_letter = atom[num_letter]
#         else:
#             c_letter = letter
#         c_text += c_letter
#     return c_text


# def main():
#     txt = "Handasaim"
#     msg = albm(txt)
#     print("Encrypted:", msg)
    
#     msg1 = albm(msg)
#     print("Decrypted:", msg1)

# main()


# turtle.done()
