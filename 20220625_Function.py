#################################################################################
# Function session.         		                           Date: 25/06/2022 #
# This algorithms are open source.                                              #
# In this file there are example questions for using functions.                 #
# Written by Gal Argov Sofer and his students for 8th and 9th Grade (KITA HET   #
# and KITA TET) for students exams in Handasaim School.                       	#
#################################################################################

# Ex 1
def test(x, y, z):
    val = x + y + z
    
    if x < -3:
        if y < z:
            val = x * y
        else:
            val = y * z
    elif x > 2:
        val = x * z
    return val


print(test(3, 4, 5))


# Ex 2
def rational(n):
    if (n % 2 == 0):
        print('0')
    else:
        a = 3
        while a < 100:
            if (n % a == 0):
                print('0')
            a += 2
        print('1')

rational(25)


# Ex 3
def func():
    num = int(input("enter"))
    if num > 11 or num < 2:
        print("invalid")
    else:
        for i in range(num, 101, num):
            print(i)
func()


# Ex 4
def my_func():
    num_1 = int(input("enter"))
    if num_1 > 11 or num_1 < 2:
        print("invalid")
    else:
        for i in range(2, 101):
            if i % num_1 == 0:
                print(i)
my_func()


# Ex 5
def recove_int(message):
    string = input(message)
    while string.isdigit() != True:
        string = input("enter1")
    return int(string)
num = (recove_int("enter"))
for i in range(2, 101):
    if i % num == 0:
        print(i)
    else:
        continue


# Ex 6
def myfunc(num):
    for i in range(2, 101):
        if (i % num == 0):
            print(i)
num = input()
num = int(num)
myfunc(num)


# Ex 7
def ex():
    num = int(input("enter"))
    if num >= 2 and num <= 11:
        for i in range(2, 101):
            if i % num == 0:
                print(i)
ex()


# Ex 8
def reciveNatureNum():
    _input = input("enter")
    while (_input.isdigit() == False) or not (_input.isdigit() == True and (int(_input) >= 2 and int(_input) <= 11)):
        _input = input("enter1")
    return int(_input)

num = reciveNatureNum()

for i in range(2, 101, 1):
    if i % num == 0:
        print(i)


# Ex 9
def func(num):
    x = 2
    if ((num >= 2) and (num <=11)):
        while x <= 100:
            if (x % num == 0):
                print(x)
            x = x + 1
    else:
        print("Invalid")
num = int(input("Enter"))
func(num)


# Ex 10
def super_gal(num):
    assert 11 >= num  >= 2, "Enter"
    nums = []
    for n in range(2, 101):
        if n % num == 0:
            nums.append(n)
    return nums
num = int(input("Enter"))
print(super_gal(num))


# Ex 11
def func1(num):
    for i in range(2, 101):
        if i % num == 0:
            print(i)
num = input("Enter")
if (int(num) >= 2 and int(num) <= 11):
    num = int(num)
    func1(num)
else:
    print("Invalid")


# Ex 12
def job(num):
    if num.isdigit and num.count(".") == 0:
        num = int(num)
        if num >= 2 and num <= 11:
            for i in range(2, 101):
                if i % num == 0:
                    print(i)
        else:
            print("Invalid")
    else:
        print("Invalid2")
job(input("Enter"))


# Ex 13
def ex():
    if num < 2 or num > 11:
        print("Invalid")
    for i in range(2, 101,):
        if i % num == 0:
            print(i, ",")
num = int(input("Enter"))
ex()


# Ex 14
def func(num):
    if (num < 2) or (num > 11):
        print("invalid")
    else:
        for i in range(2, 100):
            if i % num == 0:
                print(i)
func(10)


# Ex 15
def ex3(num):
    if (num.isdigit() == True):
        num = int(num)
        if (2 <= num <= 100):
            for i in range(2, 101):
                if i % num == 0:
                    print(i)
num = input("Enter")
ex3(num)


# Ex 16
def func(num):
    num = int(input("Enter"))
    if (2 <= num and 11 >= num):
        i = 2
        while (i <= 100):
            i += 1
            if (i % num == 0):
                print(i)
    else:
        print("Invalid")
num = 0
func(num)


# Ex 17
def func(num):
    # while num.isdigit() == False:
    #     num = int(input("Enter1"))
    while num < 2 or num > 11:
        num = int(input("Enter2"))
    for i in range(2, 101):
        if i % num == 0:
            print(i)
num = int(input("Enter"))
func(num)


# Ex 18
num = int(input("Enter"))
def func(num):
    if (11 < num or num < 2):
        print("Invalid")
    else:
        num2 = 2
        while (num2 <= 100):
            if (num2 % num == 0):
                print(num2)
            num2 += 1
func(num)


# Ex 19
def NaturalNumbers(int1):
    int_check = int(input(int1))
    if (int_check < 2 or int_check > 11):
        print("Invalid")
    # elif (int_check.count(".") > 0):
    #     print("Invalid")
    else:
        # int_check = int(int_check)
        for index in range(2, 101):
            if (index % int_check == 0):
                print(index)
            else:
                continue
NaturalNumbers(5)


# Ex 20
def func():
    num = int(input("Enter"))
    # if num.isdigit() == "False":
    #     print("Invalid")
    if num > 11 or num < 2:
        print("Invalid1")
    else:
        for i in range(2, 101):
            num = int(num)
            if i % num == 0:
                print(i)
            else:
                continue
func()


# Ex 21
def a1():
    num = int(input("Enter"))
    if num / 1 != 0:
        x = 2
        while x <= 100:
            if x / num == x // num:
                print(x)
            x += 1
a1()


# Ex 22
def ex():
    num = int(input("Enter"))
    if (num % 1 == 0) and (num >= 2) and (num <= 11):
        n = 2
        for i in range(2, 101):
            if n % num == 0:
                print(n)
            n += 1
            if n == 101:
                break
    else:
        print("Invalid")
ex()


# Ex 23
def func(num):
    if(str(num).isdigit()):
        if int(num) in range(2, 12):
            num = int(num)
            for i in range(2, 101):
                if i % num == 0:
                    print(i)
        else:
            print("Invalid")
    else:
        print("Invalid")
func(6)


# Ex 24
def myFunc(num):
    for i in range(2, 101):
        if i % num == 0:
            print(1)
        else:
            print(0)

myFunc(2)


# Ex 25
def function():
    num = int(input("Enter"))
    if num < 2 or num > 100:
        print("Error1")
    else:
        if (num % 2 == 0 or num % 5 == 0) and (num != 2 and num != 3):
            print("0")
        else:
            print("1")
            
function()


# Ex 26
def function():
    num = int(input("Enter"))
    if num < 2 or num > 100:
        print("Error1")
    else:
        if (num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0):
            print("0")
        else:
            print("1")
            
function()


# Ex 27
def ex(num):
    num = input("Enter")
    while num.isdigit() != True:
        num = input("Enter1")
    return int(num)
ex(num)
if num >= 0:
    new_num = num
    for i in range(2, 101):
        if i % num == 0:
            print(i)
            # new_num = new_num + i
    # print(new_num)
else:
    print("Invalid")

# Ex 28
def num_even():
    count = 0
    index = 0
    while index < 10:
        num = int(input("Enter"))
        if num <= 99 and num >= 10:
            count = count + 1
        index = index + 1
    print("count = ", count)
num_even()


# Ex 29
def exs8():
    counter = 0
    for k in range(5):
        gradeA = int(input("Enter A"))
        gradeB = int(input("Enter B"))
        if (gradeB >= gradeA):
            counter += 1
    if counter > 2:
        print("good")
    else:
        print("bad")
exs8()


# Ex 30
num = 9 
def myFunc(num):
    if num <= 1 or num >= 12:
        print("Error Input")
    else:
        for i in range(101):
            if i % num == 0:
                print(i)
myFunc(5)


# Ex 31
def func(num):
    if 2 <= num and num <= 11 and type(num) == int:
        # print("aaa")
        result = []
        for i in range(2, 101):
            # print("bbb")
            if i % num == 0:
                # print(i)
                result.append(i)
        return result
    else:
        print("wrong Input")
num = int(input("number"))
print(func(num))


# Ex 32
def func():
    num = int(input("enter"))
    new_num = 2
    for number in range(2, 101):
        if new_num % num == 0:
            print(new_num)
        new_num += 1
func()


# Ex 33
def get_num():
    x = int(input("enter"))
    if (x) >=2 and x < 12:
        for i in range(2, 101):
            if ((i) % x == 0):
                print(i)
        else:
            print("invalid")
get_num()


# Ex 34
def func(num):
    if (num < 2) or (num > 11):
        print("invalid")
    else:
        for i in range(2, 100):
            if i % num == 0:
                print(i)
func(10)

# Ex 35
def fun():
    num = int(input("enter"))
    if (num < 2) or (num > 11):
        print("invalid")
    else:
        for i in range(2, 101):
            if i % num == 0:
                print(i)
            # else:
            #     print("isnt good")
fun()


# Ex 36
# def my_f(number):
#     while number % 1 != 0:
#         number = input("enter")
#     number = int(number)
#     for i in range(2, 101):
#         if i % number == 0:
#             print(i)
# my_f(1)


# Ex 37
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


# Ex 38
# def algo(natural):
#     countdown = 100
#     while countdown >= 2:
#         if countdown % natural == 0 and natural <= 11 and natural >= 2:
#             print(countdown)
#         countdown = countdown - 1

# natural = int(input("Enter"))
# algo(natural)
# x = algo(natural)
# print(x)


# Ex 39
# def ex():
#     number = int(input("Enter"))
#     while number.isdigit != True:
#         n = 10
#     if (10 / 100):
#         print("true")
#     n = n + 1
# ex()


# Ex 40
# str1 = (int(input("Enter")))
# for i in range(2, 12):
#     if str1 != i:
#         print("Invalid")
#     else:
#         for i in range(2, 101):
#             if i % str1 == 0:
#                 print(i, end=" ")


# EOF