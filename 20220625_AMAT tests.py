#################################################################################
# AMAT tests.												  Date: 25/06/2022	#
# Credits to the algorithms for Ministery of Education and Technology - Israel.	#
# In this file there are questions from AMAT test.								#
# Written by Gal Argov Sofer for 8th and 9th Grade (KITA HET and KITA TET) to 	#
# check the students exams in Handasaim School. 								#
#################################################################################


# ###################### AMAT test KITA HET ################################### #

# Q1
# 1
num1 = 3
num2 = 10
num1 = num2
num2 = num1
print("num1 = ", num1, "num2 = ", num2)

# 2
number = "12345"
print("4" in number)

# 3
msg1 = "He" + "l"*2 +"o"
msg2 = " world"
print(msg1 + msg2)
print(len(msg1))

# 4
number = 123
print(number // 100)
print(number % 100 % 10)
print(number % 10)

# Q2
a = 10
b = 15
c = 0
# 1
print(a >= b or b == c)

# 2
print(a % 5 == 0 and b // 5 > c)

# 3
print(a < 0 or (b == c + 15 and a >= c))

# 4
print(a % 1 == c % 2 and b % 3 > a % 3)

# 5
print(a != b and b != c)

# Q3
# 1
i = 1
while i < 4:
    print('wow')
    i += 1

# 2
for item in range(6):
    if item % 2 == 1:
        print(item * item)
        
# 3
for item in range(9, 0, -3):
    print(item)
    
# 4
x = 5
i = 1
while i < 4:
    x -= 1
    i += 1
print(i, x)

# Q4
# 1
for x in range(100, 200, 2):
    print(x)
# 2
for x in range(1, 10):
    print(x - 1)
# 3
for x in range(4, 5):
    print(x + 3)
# 4
for x in range(-5, 6):
    print(x + 6)

# a
x = 0
while x < 9:
    print(x)
    x += 1

# b
for x in range(7, 8):
    print(x)

# c
for x in range(100, 200):
    if x % 2 == 0:
        print(x)

# d
x = 1
while x < 12:
    print(x)
    x += 1
    
# Q5
def calc_avg():
    sum = 0
    count = 0
    grade = int(input("Bla"))
    while grade > 0:
        sum += grade
        count += 1
        grade = int(input("Bla"))
        avg = sum / count
    print(avg)
calc_avg()

# Q6
def perfect_number():
    num = int(input("Please enter a number:"))
    sum = 0
    x = 1
    while x < num:
        if num % x == 0:
            sum = sum + x
        x = x + 1
    if sum == num:
        print("Perfect Number")
    else:
        print("Not Perfect Number")
perfect_number()


# Q6
def perfect_number():
    num = int(input("Please enter a number:"))
    sum = 1 - num
    x = 1
    # print("sum:", sum)
    while x < num:
        # print("num:", num, "\tsum:", sum, "\tx:", x, "\tnum // x:", num // x, "\tnum / x:", num / x)
        if num / x == num // x:
            sum = sum + num / x
        x = x + 1
    if sum == num:
        print("Perfect Number")
    else:
        print("Not Perfect Number")
perfect_number()
    
# Q7
def find_location():
    id_number = int(input("Please enter ID number:"))
    digit = int(input("Please enter a digit:"))
    found = False
    for index in range(0, 10):
        if id_number % 10 == digit:
            print(index + 1)
            found = True
        id_number = id_number // 10
    if found == False:
        print("-1")
find_location()

# Q8
import random

def shuffle(lst1):
    lst_size = len(lst1)
    shift_size = int(lst_size * 10)
    for i in range(shift_size):
        random_index = random.randrange(0, lst_size)
        item = lst1.pop(random_index)
        lst1.append(item)
    print(lst1)


lst1 = [120, 150, 200, 300, 190, 170, 250, 210, 230]
shuffle(lst1)


# 1
for x in range(360):
    t.left(1)
    t.forward(1)

# 2
for index in range(3):
    t.forward(100)
    t.left(360 / 3)
    
# 3
t.left(180)
t.forward(80)
t.left(90)
t.forward(70)
for index in range(4):
    t.forward(80)
    t.left(90)
    
# 4
for index in range(4):
    t.left(90)
    t.forward(90)
    t.right(90)
    t.forward(50)
    
# Q9
def create_skip2str():
    st = input("Please enter a string:")
    skip2str = ""
    for letter in range(0, len(st), 3):
        skip2str = skip2str + st[letter]
    print(skip2str)
create_skip2str()



# ###################### AMAT test KITA TET ################################### #

# Q1
# 1
arr = [32, 51, 13, 23, 30]
arr.sort()
tmp = arr[-1]
print(tmp)

# 2
arr = [32, 51, 13, 23, 30]
tmp = arr[0]
for item in arr:
    if item > tmp:
        tmp = item
print(tmp)

# 3
arr = [32, 51, 13, 23, 30]
tmp = max(arr)
print(tmp)

# 4
arr = [32, 51, 13, 23, 30]
arr.sort(reverse = True)
tmp = arr[0]
print(tmp)

# Q2
# 1
list1 = ['Israel', 'Japan', 'Italy', 'Jordan', 'Israel', 'Portugal']
list1.remove('Israel')
print(list1)
print(len(list1))

# 2
list1 = ['Israel', 'Japan', 'Italy', 'Jordan', 'Israel', 'Portugal']
for i in range(len(list1)):
    if 'Israel' in list1:
        list1.remove('Israel')
print(list1)
print(len(list1))

# 3
list1 = ['Israel', 'Japan', 'Italy', 'Jordan', 'Israel', 'Portugal']
count1 = list1.count('Israel')
for i in range(count1):
    list1.remove('Israel')
print(list1)
print(len(list1))

# 4
list1 = ['Israel', 'Japan', 'Italy', 'Jordan', 'Israel', 'Portugal']
count = list1.index('Israel')
list1 = list1[count + 1:]
print(list1)
print(len(list1))

# 5
list1 = ['Israel', 'Japan', 'Italy', 'Jordan', 'Israel', 'Portugal']
list2 = []
for state in list1:
    if not state == 'Israel':
        list2.append(state)
list1 = list2
print(list1)
print(len(list1))

# Q3
min = 10
num = int(input("4 digit natural number:"))
tmp = num % 10
for i in range(4):
    num = num // 10
    if min > tmp:
        min = tmp
    tmp = num % 10
print(min)

# Q4
# 1
def f1(lst):
    for x in lst:
        if x < 0:
            print(x)

lst = [-7, 2, 10, 5, -2, 8, -1, 0]
print("f1: ")
f1(lst)

# 2
def f2(lst):
    for x in lst[::-1]:
        if x < 0:
            print(x)

lst = [-7, 2, 10, 5, -2, 8, -1, 0]
print("f2: ")
f2(lst)

# 3
def f3(lst):
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] < 0:
            print(lst[i])

lst = [-7, 2, 10, 5, -2, 8, -1, 0]
print("f3: ")
f3(lst)

# 4
def f4(lst):
    for i in range(len(lst)):
        if lst[i] < 0:
            print(i)

lst = [-7, 2, 10, 5, -2, 8, -1, 0]
print("f4: ")
f4(lst)

# Q5
# 1
import queue
q1 = queue.Queue()
q2 = queue.Queue()
q1.put(10)
q1.put(20)
q1.put(30)
q1.put(40)
while not q1.empty():
    q2.put(q1.get())
while not q2.empty():
    q1.put(q2.get())
x = q1.get()
print(x)

# 2
import queue
q1 = queue.Queue()
list1 = []
q1.put(10)
q1.put(20)
q1.put(30)
q1.put(40)
while not q1.empty():
    list1.append(q1.get())
for item in list1:
    q1.put(item)
x = q1.get()
print(x)

# 3
import queue
q1 = queue.Queue()
q1.put(10)
q1.put(20)
q1.put(30)
q1.put(40)
l = []
s = 0;
while not q1.empty():
    x = q1.get()
    l.append(x)
    s = s + x
print(s)

# 4
import queue
q1 = queue.Queue()
list1 = []
q1.put(10)
q1.put(20)
q1.put(30)
q1.put(40)
temp = q1.get() + q1.get()
q1.put(temp)
temp = q1.get() + q1.get()
q1.put(temp)
print(q1.get())

# Q6
def change_password(password):
    temp = password[0].capitalize()
    temp = temp + password[1:]
    temp = temp.replace('a', '@')
    temp = temp.replace('i', '1')
    print(temp)
change_password('telaviv')
change_password('mazaltov')

# Q7 - problam with this question
# 1
def is_exist(lst, tav):
    for item in lst:
        if tav not in item:
            print('OUT')
            return
    print('IN')

is_exist(['ai', 'bi', 'i'], 'i')

def is_exist2(lst, tav):
    for item in lst:
        if tav not in item:
            print('IN')
            return
    print('OUT')

is_exist2(['ai', 'bi', 'i'], 'i')


# Q8
# 1
def select(lst1, party_time):
    lst1_size = len(lst1)
    return_lst = []
    sum_time = 0
    for item in lst1:
        if (sum_time + item) < (party_time * 60):
            return_lst.append(item)
            sum_time = sum_time + item
    print(return_lst)

lst1 = [120, 150, 200, 300, 190, 170, 250, 210, 230]
select(lst1, 10)
lst2 = [190, 150, 240, 220, 20, 270]
select(lst2, 14)


# ###################### AMAT test KITA HET - Checks ########################## #

# Ex 1 - AMAT test
t = turtle.Turtle('turtle')

def draw(size):
    for i in range(4):
        t.left(90)
        t.forward(size)

t.penup
t.goto(0, 0)
t.pendown
draw(50)
draw(100)
draw(150)

turtle.done()

# Ex 2 - AMAT test
t = turtle.Turtle('turtle')

t.penup()
t.goto(0, 100)
t.pendown()
t.goto(100, 100)
t.goto(0, 0)
t.goto(100, 0)

turtle.done()


# Ex 3 - AMAT test
t = turtle.Turtle('turtle')

t.shape("square")
size = 100
t.pendown()
for index in range(4):
    for item in range(4):
        t.forward(size)
        t.left(90)
    size = size - 20

turtle.done()

# EOF