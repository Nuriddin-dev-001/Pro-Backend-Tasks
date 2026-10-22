# string methods
# Ma`lum obyekt, klassga tegishli funksiya metod deyiladi
#
# #1 capitalize
# x = "salom"
# x2 = x.capitalize()
# print(x2)
#
# #2 casefold
# x = "Salom"
# x2= x.casefold()
# print(x2)
#
# #3 center.1
# x="ananas"
# x2=x.center(10)
# print(x2)
#
# #4 center.2
# x="ananas"
# x2=x.center(20,"*")
# print(x2)
#
# #5 count
# x="I love apples, apple are my favorite fruit"
# x2=x.count("apple")
# print(x2)
# #
# #6 encode
# x="My name is Ståle"
# x2=x.encode()
# print(x2)
#
# #7 endswith
# x="Hello, welcome to my world."
# x2=x.endswith("world.")
# print(x2)
#
# #8 expandtabs
# x="H\te\tl\tl\to"
# x2=x.expandtabs(0)
# print(x2)
#
# #9 find
# x="Hello, welcome to my world."
# x2=x.find("to")
# print(x2)
#
# #10 index
# x="Hello, welcome to my world."
# x2=x.index("Hello") #finddan farqi shu holatda error qaytaradi
# print(x2)
#
# #11 isalnum
# x="Company12" #raqam bo`lmasa false qaytaradi
# x2=x.isalnum()
# print(x2)
#
#12 isalpha
# x="Company" #raqam ishtirok etsa false qaytaradi
# x2=x.isalpha()
# print(x2)
#
# #13 isascii
# x="Company123"
# x2=x.isascii()
# print(x2)
#
# #14 isdecimal
# x="1234"
# x2=x.isdecimal()
# print(x)
#
# #15 isdigit
# x="50800"
# x2=x.isdigit() #raqam bo`lsa true qaytaradi
# print(x2)
#
# #16 istitle
# x="Hello, And Welcome To My World!"
# x2=x.istitle()
# print(x2)

#17 isidentifier
# x="Demo"
# x2=x.isidentifier()
# print(x2)
#
# #18 islower
# x="hello world!"
# x2=x.islower()
# print(x2)
#
# #19 isupper
# x="THIS IS NOW!"
# x2=x.isupper()
# print(x2)
#
# #20 join
# myTuple = ("John", "Peter", "Vicky")
# x="  ".join(myTuple)
# print(x)
#
# #21 lower
# x="Hello my FRIENDS"
# x2=x.lower()
# print(x2)
#
# #22 lstrip
# x="     banana     "
# x2=x.lstrip()
# print(x2)
#
# #23 rstrip
# x="     banana     "
# x2=x.rstrip()
# print(x2)
# #
# #24 split
x = "welcome jungle"
x2=x.split()
print(x2)

#25 maketrans
x="Hello Sam!"
x2=x.maketrans("S", "P")
print(x.translate(x2))

#26 replace
x="I like bananas"
x2=x.replace("bananas", "apples")
print(x2)

#27 rfind
x="Mi casa, su cas."
x2=x.rfind("casa")
print(x2)

#28 translate
x= {83:  80}
x2="Hello Sam!"
print(x2.translate(x))

#29 splitlines
x="Thank you for the music\nWelcome to the jungle"
x2=x.splitlines()
print(x2)

#30 upper
x="Hello my friends"
x2=x.upper()
print(x2)
