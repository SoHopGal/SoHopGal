#################################################################################
# Turtle session.         		                               Date: 25/06/2022 #
# This algorithm is open source.                                                #
# In this file there are example questions for using turtle library function.   #
# Written by Gal Argov Sofer for 8th Grade (KITA HET) exam in Handasaim School. #
#################################################################################


import turtle

# Ex 1 - MAGEN DAVID - Star of David
t = turtle.Turtle()
polygon = 3
a = 180 - (180 * (polygon - 2)) / polygon
length = 100
start = 1
end = 4
rightAngle = 90
distance = 2 * 86

for sides in range(start, end):
    t.right(a)
    t.forward(length)

t.right(rightAngle)
t.penup()
t.forward(distance / polygon)
t.pendown()
t.right(rightAngle)

for sides in range(start, end):
    t.forward(length)
    t.right(a)

t.penup()

turtle.done()


# Ex 2 - MESHUSHE - Hexagon
t = turtle.Turtle('turtle')
n = 6
m = 3

t.width(5)
t.color('red')

for i in range(n):
    t.forward(100)
    t.left(180 - (180 * (n - 2)) /  n)

t.penup()

turtle.done()


# Ex 3 - MESHULASH - Triangular
t = turtle.Turtle('turtle')
n = 6
m = 3

t.width(5)
t.color('red')

for i in range(m):
    t.forward(100)
    t.left(180 - (180 * (m - 2)) /  m)

t.penup()

turtle.done()


# Ex 4 - Peace and Love Symbol
t = turtle.Turtle('turtle')

radius = 170
angle = 45

t.up()
t.width(10)
t.goto(0, -radius)
t.down()

t.circle(radius)
t.left(angle * 2)
t.forward(radius * 2)
t.up()
t.left(angle * 4)
t.forward(radius)
t.right(angle)
t.down()
t.forward(radius)
t.up()
t.backward(radius)
t.left(angle * 2)
t.down()
t.forward(radius)
t.up()

t.goto(0, 0)

turtle.done()


# Ex 5
t = turtle.Turtle()
t.setheading(180)
t.forward(100)


# EOF