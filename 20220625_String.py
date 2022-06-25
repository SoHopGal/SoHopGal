#################################################################################
# String session.                                             Date: 25/06/2022  #
# This algorithm is open source.                                                #
# In this file there are example questions for using string data type.	        #
# Written by Gal Argov Sofer for 8th Grade (KITA HET) exam in Handasaim School. #
#################################################################################


# Ex 1
def getMiddleThreeChars(str1):
    print("Original String is", str1)
    mi = int(len(str1) / 2)
    res = str1[mi - 1:mi + 2]

    print(mi, "Middle three chars are:", res)


getMiddleThreeChars("HANDASA")
getMiddleThreeChars("HANDASAIM")


# Ex 2
def solve(s, t):
    res = ""
    i = 0
    m = min(len(s), len(t))
    print("res:", res, "\t\ti:", i, "\t", "m:", m, "\t", "len(res):", len(res))

    while i < m:
        res += s[i] + t[i]
        i += 1
        print("res:", res, "\ti:", i, "\t\t", "len(res):", len(res))
    return res + s[i:] + t[i:]

s = "abc"
t = "xyz"

print("The function returns:", solve(s, t))


# Ex 3
str1 = "I loooooove Handasaim"
print(str1[:2:] + str1[2:4:] + str1[7:9:] + " " + str1[10::])
print(str1[:4:] + str1[9:12:] + str1[12::])
str1 = "I loooove Handesaim"
print(str1[:2:] + str1[2:4:] + str1[7:9:] + " " + str1[10::])


# Ex 4
string = "Yes We Can!!!"
print(string[4])
print(len(string))
print(string[-3])
print(string[::2])
print(string[4:-3])
print(string[:])


# Ex 5
secret = ""
if (len("comp") == len("uter")):
    secret = "computer"
else:
    secret = "secret"
if (len("science") % 2 == 0):
    secret = secret + "secret"
else:
    secret = secret + "science"
if ("a" in "scratch"):
    secret = secret + "1"
else:
    secret = secret + "2"
print(secret)


# Ex 6
word1 = "lo"
word2 = "han"
word3 = "v"
word1 = word1 + word3[0]
print(word1)
if (len(word1) % 3 == 0):
    word1 = word1 + "e"
else:
    word1 = word1 + "a"
if (len(word2) < 4):
    word2 = word2 + "dasa"
else:
    word2 = word2 + "ing"
print(word1, word2)


# EOF