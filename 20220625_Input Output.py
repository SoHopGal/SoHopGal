#################################################################################
# Input Output session.   		                               Date: 25/06/2022 #
# This algorithm is open source.                                                #
# In this file there are example questions for using input output commands.     #
# Written by Gal Argov Sofer for 8th Grade (KITA HET) exam in Handasaim School. #
#################################################################################


# Ex 1
num = input("enter")
# print(num.isdigit())
# num = int(num)
if (num.isdigit() and num >= 2) and (num <= 11):
    num = int(num)
    for i in range(2, 101):
        if i % num == 0:
            print(i)
else:
    "invalid"


# Ex 2
num = int(input("enter"))
while num < 2 or num > 11:
    num = int(input("enter1"))
for i in range(2, 101):
    if i in range(2, 101):
        if (i % num == 0):
            print(i)


# Ex 3
num = input("enter")
# print(num.isdigit())
# num = int(num)
if (num.isdigit()) and num >= 2 and (num <= 11):
    num = int(num)
    for i in range(2, 101):
        if i % num == 0:
            print(num)
else:
    "invalid"


# Ex 4
num = 0
num1 = int(input("Enter"))
num2 = 0
while num <= 100:
    num2 = num2 + 1
    print(num * num2)
    num = num1 * num2


# Ex 5
num = int(input("Enter"))
for i in range(2, 101):
    if i % num == 0:
        print(i)


# Ex 6
num = int(input("Enter"))
if (num >= 2) and (num <= 11):
    # if num == int:
        div_num = num
        while div_num < 101:
            print(div_num)
            div_num = div_num + num


# Ex 7
num = input("Enter")
# while (num < 2 or num > 11):
#     num = int(input("Enter1"))
while num.isdigit() != True and (num < 2 or num > 11):
    num = int(input("Enter1"))
num = int(num)
for number in range(2, 100):
    if number % num == 0:
        print(number)


# Ex 8
number = int(input("Enter"))
if number <= 11 and number >= 2:
    for i in range(2, 101):
        if i % number == 0:
            print(i)
else:
    print("Invalid")


# Ex 9
num1 = int(input("Enter"))
while (num1 < 2 or num1 > 11):
    num1 = int(input("Enter1"))
for number in range(101):
    if (number % num1 == 0):
        print(number)


# Ex 10
num = int(input("Enter"))
if (num > 1) and (num < 12):
    for i in range(2, 101):
        if i % num == 0:
            print(i)
else:
    print("Invalid")


# Ex 11
num = input("Enter")
if (num.isdigit() == True) and (int(num) >= 2) and (int(num) <= 11):
    for i in range(2, 101):
        if i % int(num) == 0:
            print(i)
else:
    print("Invalid")


# Ex 12
num = int(input("Enter"))
if (num > 1) and (num < 12):
    for i in range(2, 101):
        if i % num == 0:
            print(i)
else:
    print("Invalid")


# Ex 13
num = 2
number = int(input("Enter"))
if 11 >= number >= 2:
    while num <= 100:
        if num % number == 0:
            print(num)
        # print(number / num)
        # print(num / number)
        num = num + 1
else:
    print("Invalid")


# Ex 14
num = int(input("enter"))
if num >= 2 and num <= 11:
    for i in range(2, 101):
        if(i % num == 0):
            print(i)
else:
    print("invalid")


# Ex 15
num = int(input("enter"))
for x in range(2, 101):
    if (x % num) == 0:
        print(x)


# Ex 16
num = int(input("enter"))
while num < 2 or num > 11:
    num = int(input("enter1"))
for i in range(0, 101, num):
    if i < 2:
        continue
    else:
        print(i)


# Ex 17
num = int(input("enter"))
if num > 1 and num < 12:
    for i in range(2, 100):
        if i % num == 0:
            print(i)


# Ex 18
number = int(input("enter"))
if (number < 2 or number > 11) or (number.isdigit() == False):
    print("Invalid")
    number = int(input("enter1"))
    while (number < 2 or number > 11):
        number = int(input("enter2"))
number = int(number)
for i in range(2, 101):
    if i % number == 0:
        print(i)


# Ex 19
num = int(input("enter"))
if num > 2 and num < 11:
    for j in range(2, 101):
        for i in range(100 // num):
            print(num, j, i, j * num)


# Ex 20
num = float(input("enter"))
if num < 12 and num > 1:
    while (100 // num < 12 and 100 // num > 1):
        print(float(100 // num))
        num = num + num
else:
    print("Invalid")


# Ex 21
sum = 0
result = 0
    
for i in range(5):
    num = int(input("Enter num"))
    result = num % 10
    sum += result
    print(sum, num, result)
print(sum)


# Ex 22
count = 0
for i in range(5):
    num = int(input("Enter num"))
    if (num % 2 == 0):
        count += 1
    else:
        count -= 1
print(count)



# Ex 23
number = int(input("enter number"))
while number > 11 or number < 2:
    number = int(input("enter number again"))
for i in range(2, 101, 1):
    if i % number == 0:
        print(i)


# Ex 24
num = int(input("enter"))
if (num < 2) or (num > 11):
    print("invalid")
else:
    for i in range(2, 101):
        if i % num == 0:
            print(i)


# Ex 25
num = int(input("enter"))
for x in range(2, 100):
    if (x % num) == 0:
        print(x)


# Ex 26
rishoni = 0
num = int(input("Enter"))

if (num < 2 or num > 100):
    print("Error1")
else:
    for i in range(2, num):
        if (num % i != 0):
            for j in range(num + 1, 101):
                if (num % i != 0):
                    rishoni = 1
print(rishoni)


# Ex 27
first = 1
second = 1
counter = 3
print("Fibo item 1 is ", first)
print("Fibo item 2 is ", second)
while counter <= 25:
    third = first + second
    first = second
    second = third
    print("Fibo item", counter, "is", third)
    counter = counter + 1


# EOF