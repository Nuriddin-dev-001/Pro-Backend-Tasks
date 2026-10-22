# List Comprehension
# 1_______________________________________________
from fileinput import lineno
from functools import reduce

l = [1,2,3,4,5,6,7,8,9]

toqlar = [i*2 for i in l if i%2 == 1]  #listdagi toqlarni 2 ga ko'paytiradi
print(toqlar)

kvadrat = [i**2 for i in l if i%2 ==0]  #listdagi juft sonlarni kvadratini chiqaradai
print(kvadrat)
# 2_______________________________________________
regions = [["Toshkent", "Buxoro"], ["Farg'ona", "Jizzax"], ["Jizzax", "Navoiy"], ["Andijon", "Farg'ona"],
           ["Samarqand", "Andijon"], ["Buxoro", "Samarqand"]]

from_city = [city[0] for city in regions] #har bir listning 0-elementini print qiladi
print(from_city)

# 3_______________________________________________
lst = [1, 2, 3, 'Alisa', 'Alisa']

indice = lst.index("Alisa")  #listdagi birinchi Alisaning indexsini qaytaradi
print(indice)

indices = [i for i in range(len(lst)) if lst[i]=="Alisa"]

print(indices) #listdagi barcha Alisalarning indexini qaytaradi

# 4_______________________________________________
people = [("John", 240_000), ("Alice", 120_000), ("Ann", 1_100_000), ("Zach", 44_000), ("Doe", 2_300_000)]

millioners = [name for name, money in people if money >= 1_000_000]
print(millioners)

cars = [("Bugatti Chiron", 5_000_000), ("BMW XM", 180_000), ("Maybach 680", 250_000), ("Pogani huayra", 4_000_000)]
auto = [name for name, salary in cars if salary >= 1_000_000]
print(auto)

# 5_______________________________________________
def millioneer(people):
    return [name for name, money in people.items() if money >= 1_000_000
            ]
people_data1 = {'Alice': 1_000_000, 'Bob': 998_170, 'Carol': 1_229_080, 'Frank': 881_230, 'Eve': 93_121}
people_data2 = {'Alice': 1_000_000, 'Bob': 998_170, 'Frank': 1_881_230, 'Eve': 93_121}

def test():
    assert millioneer(people_data1) == ['Alice', 'Carol']
    assert millioneer(people_data2) == ['Alice', 'Frank']

test()

l = []
for x in range(3):
    for y in range(3):
        l.append((x, y))
print(l)
print([(x, y) for x in range(3) for y in range(3)])

# 6_______________________________________________
text = '''Call me Ishmael. Some years ago - never mind how long precisely - having little
or no money in my purse, and nothing particular to interest me on shore, I thought I would
sail about a little and see the watery part of the world. It is a way I have of driving off
the spleen, and regulating the circulation. - Moby Dick '''
print([[i for i in line.split() if len(i)>8] for line in text.split("\n")])

# 7.Ziplash_______________________________________________
lst_1 = ['ism', 'familiya', 'yosh']
lst_2 = ['Akmal', 'Tohirov', 16]
zipped = zip(lst_1, lst_2)   #ziplaydi
# print(list(zipped))

# Unziplash
lst_1_new, lst_2_new = zip(*zipped)  #zipdan chiqaradi
print(list(lst_1_new))
print(list(lst_2_new))

# 8_______________________________________________
ustun_nomlari = ['name', 'salary', 'job']

qatorlar = [('Alice', 180_000, 'data scientist'),
            ('Bob', 99_000, 'project manager'),
            ('Frank', 87_000, 'backend developer')]
db = [dict(zip(ustun_nomlari, row))for row in qatorlar]
print(db)

# 9.Lambda_______________________________________________
f = lambda a: a * 2
                       # Ikkisi teng
# def f(a):
#     return a * 2
print(f(8))
# 10______________________________________________
# 1,
summa = lambda a, b, c: a + b + c
print(summa(1,2,3))

# 2,
print((lambda a, b, c : a + b+c)(1,2,3))

def summa(a,b,c):
    return a+b+c
print(summa(1,2,3))

# 11.Map______________________________________________
str_nums = ["4", "8", "6", "5", "3", "2", "8", "9", "2", "5"]  #Stringni integerga o'tkazadi
int_nums = map(int, str_nums)
print(list(int_nums))

# 12______________________________________________
print(list(map(lambda x, y: x - y, [2, 4, 6], [1, 3, 5])))

# 13______________________________________________
string_it = ["processing", "strings", "with", "map"]
print(list(map(str.upper, string_it)))
# 14.Reduce______________________________________________
n = 5
print(reduce(lambda x, y: x * y, range(1, n + 1)))

