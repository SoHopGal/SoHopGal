#################################################################################
# Calculator session.                                          Date: 25/06/2022 #
# This algorithm is open source.                                                #
# In this file there are example questions for using calculate function.        #
# Written by Gal Argov Sofer for 8th Grade (KITA HET) exam in Handasaim School. #
#################################################################################


# Solution for 4.5:
def calc(x, y):
    summ = x + y
    sub = x - y
    mul = x * y
    if y != 0:
        div = x / y
    return summ, sub, mul, div

def main():
    a, b, c, d = calc(5, 2)
    print(a, b, c, d)
    print(a - d)

main()


# Solution for 7.5:
def calc(x, y):
    summ = x + y
    sub = x - y
    mul = x * y
    if y != 0:
        div = x / y
    return summ, sub, mul, div

def main():
    a, b, c, d = calc(30, 6)
    print(a, b, c, d)
    print(c / b)

main()


# Other nice solutions for 7.5:
def calc(x, y):
    summ = x + y
    sub = x - y
    mul = x * y
    if y != 0:
        div = x / y
    return summ, sub, mul, div

def calc1(x, y):
    summ = x - y
    sub = x + y
    mul = x + y
    if y > 0:
        div = x - y
    return summ, sub, mul, div
    
def calc2(x, y):
    summ = x / y
    sub = x - y
    mul = x + y
    if y != 0:
        div = x * y
    return summ, sub, mul, div

def calc3(x, y):
    summ = x + y
    sub = x - y
    mul = x + y
    if y != 0:
        div = x + y
    return summ, sub, mul, div
    
def main():
    a, b, c, d = calc(5.5, 2)
    print(a, b, c, d)
    print(c - b)

    a, b, c, d = calc(5, 3)
    print(a, b, c, d)
    print(c / b)

    a, b, c, d = calc1(1.875, 1.875)
    print(a, b, c, d)
    print(c + b)

    a, b, c, d = calc2(2.75, 0.25)
    print(a, b, c, d)
    print(c * b)
    
    a, b, c, d = calc3(3.75, 3.75)
    print(a, b, c, d)
    print(c - b)

    a, b, c, d = calc(12, 1.5)
    print(a, b, c, d)
    print(c - b)

main()


# EOF