#################################################################################
# Basic session.         		                               Date: 25/06/2022 #
# This algorithm is open source.                                                #
# In this file there are example questions for learning basics in computer		#
# science: Variables, Operators, Data Types, Boolean Expression, ASCII table,   #
# for loops, while loops, etc.                                                  #
# Written by Gal Argov Sofer for 8th Grade (KITA HET) exam in Handasaim School. #
#################################################################################


# Ex 1
x = []
print(type(x))
x = "[]"
print(type(x))


# Ex 2
myStr = "exam"
print(myStr[2])
myStr = "3x4m"
print(myStr[2])
x = "3x4m"
print(type(x))


# Ex 3
y = 5
if (y > 5 or y < 4):
    print("True")
else:
    print("False")


# Ex 4
print("Red" > "Green")
print("AAA" > "AA")


# Ex 5
word1 = "Hello World!"
word2 = "hello world!"
print(word1.lower() == word2)
word1 = "Hello World!"
word2 = "hello world!"
print(word1.upper() == word2)


# Ex 6
myVar = "G"
print(myVar * 5)
myVar = "G"
print(chr(ord(myVar) + 5))


# Ex 7
x = 30.1
print(type(x))
y = 301
print(type(y))


# Ex 8
num = 5 ** 2
print(num)
num2 = 2 ** 5
print(num2)


# Ex 9
num = 5
num += 4
print(num)

num = 5
num *= 2
print(num)


# Ex 10
checkChar = 'l'
myStr = "Hello"
print(myStr.count(checkChar))


# Ex 11
numA = 1
numB = 2
if numA == numB:
    print('TRUE')
else:
    print('FALSE')
numC = 5
numD = 2
numE = numC ** numD
print(numE)
numE = numD ** numC
print(numE)


# Ex 12
num = 100 % 9
print(num)
num = 100 % 12
print(num)


# Ex 13
k = 0
while k < 12:
    print(k)
    k = k + 3
k = 1
while k < 12:
    print(k)
    k = k * 2
i = 1
k = 1
while k < 12:
    print("k =", k)
    print("i =", i)
    k *=  2
    i *=  k
i = 9
k = 0
while k < 101:
    if k % i == 0:
        print(k)
    k += 1


# Ex 14
sum = 0
for i in range(5):
    for j in range(4):
        sum = sum + j + i
        print("i =", i, " j =", j, " sum =", sum)
print(sum)


# Ex 15
num = 10
for i in range(2, 101):
    if i % num == 0:
        print(i)


# Ex 16
num1 = 3
num2 = 4
num3 = 6
if (num1 < num2) or (num2 < num3):
    print("True")
else:
    print("False")

if (num1 < num2) and (num3 < num2):
    print("True")
else:
    print("False")

if (num3 % 2 == 0) and (not (num3 < num1)):
    print("True")
else:
    print("False")

if (num1 * 2 == num3) and (num3 % 3 == 0):
    print("True")
else:
    print("False")

if (num2 == 7) or (num1 > 10):
    print("True")
else:
    print("False")


# Ex 17
status = 2
level = 4

if status <= 1:
    if status < level:
        print("one")
    else:
        print("two")
    print("three")
else:
    print("four")
print("five")


# Ex 18
k = 0
while k < 14:
    print(k)
    k = k + 4
k = 0
while k < 15:
    print(k)
    k = k + 3



# Ex 19
k = 1
while k < 50:
    print(k)
    k = k * 3
k = 1
while k < 126:
    print(k)
    k = k * 5


# Ex 20
i = 1
k = 1
while k < 12:
    print("k =", k)
    print("i =", i)
    k *= 2
    i *= k
i = 1
k = 1
while k < 28:
    print("k =", k)
    print("i =", i)
    k *= 3
    i *= k


# Ex 21
sum = 0
for i in range(8):
    sum = sum + i
    print("i =", i, " sum =", sum)
print(sum)

sum = 0
for i in range(1, 9, 1):
    sum = sum + i
    print(i < 9, "i =", i, " sum =", sum)
print(sum)


sum = 0
for i in range(5):
    for j in range(4):
        sum = sum - j + i
        print("i =", i, " j =", j, " sum =", sum)
print(sum)


# Ex 22
num1 = 2
num2 = num1 + 5
num1 = num1 + num2 + 3
print("num1 =", num1, "num2 =", num2)

num = 3
num = 10
num = 3 + num
print("num =", num)


# Ex 23
num1 = 5
num2 = 6
num3 = 7

if ((num1 < num2) or (num2 < num3)):
    print("1.True")
else:
    print("1.False")

if ((num1 < num2) and (num3 < num2)):
    print("2.True")
else:
    print("2.False")

if ((num2 % 2 == 0) and (not (num1 > num3))):
    print("3.True")
else:
    print("3.False")

if ((num3 + 1 == 8) and (num3 % 2 == 0)):
    print("4.True")
else:
    print("4.False")

if ((num2 == 7) or (num1 > 5)):
    print("5.True")
else:
    print("5.False")


# Ex 24
for row in range(4):
    for col in range(4):
        if ((row + col) % 2 == 0):
            print("O")
        else:
            print("X")
    print("\n")


# Ex 25
sum = 0
for i in range(8):
        sum = sum + i
        print("i =", i, " sum =", sum)
print(sum)


# Ex 26
status = 1
level = 7

if status == 1:
    if status > level:
        print("one")
    else:
        print("two")
    print("three")
else:
    print("four")
print("five")


# EOF