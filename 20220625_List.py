#################################################################################
# List session.                                                Date: 25/06/2022 #
# This algorithm is open source.                                                #
# In this file there are example questions for using list data stracture.       #
# Written by Gal Argov Sofer for 9th Grade (KITA TET) exam in Handasaim School. #
#################################################################################


# Ex 1
fruit = ['pear', ['apple', 'pear'], 'grapefruit', 'apple']
print(fruit.index('apple'))


# Ex 2
grocery_list = ['software', 'computer', 'engineering']
for idx, val in enumerate(grocery_list):
    print("%s: %s" % (idx, val))


# Ex 3
def func(x = []):
    x.append("SE")
    print(x)

    
func()
func()
func()


# Ex 4
fruit = ['pear', ['apple', 'pear'], 'grapefruit', 'apple']
fruit.reverse()
print(fruit)


# Ex 5 - Check if there is sum of 2 elements thatequal to element between them
myList = [2, 5, 6, 9, 3, 1, 7]
myBool = False

for i in range(len(myList) - 2):
    print(i, ":", myList[i] + myList[i + 2] - myList[i + 1])
    if myList[i] + myList[i + 2] - myList[i + 1] == 0:
        myBool = True

print(myBool)


# Ex 6
myList = ['i', 'g', 'a', 'g', 'r']
number = myList.count('g')
print(number)
print(myList.index('a'))
myList.append('s')
print(myList)
print(myList[1].upper())
myList.sort()
print(myList)


# Ex 7 - Print multiplications from 2 to 100 for the input
sum = []
num = int(input("Enter"))
while num < 2 or num > 11:
    print("Enter1")
    num = int(input("Enter"))
for i in range(2, 100):
    if i % num == 0:
        sum.append(i)
print(sum)


# EOF