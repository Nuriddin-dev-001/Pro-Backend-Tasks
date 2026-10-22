# 26-dars vazifasi Nuriddin Inomov
# Instance method vazifalari:
# 1.
# Atribut balansi bilan BankAccount clasini yarating. Depozit qilish,
# yechib olish va bank hisobidagi balansni mos ravishda tekshirish.
# Yechib olish va tekshirish usullarini qo'llang.

class BankAccount:
    def __init__(self, boshlangich_balans=0):
        self.balans = boshlangich_balans

    def deposit_qilish(self, summa):
        if summa > 0:
            self.balans += summa
            print(f"{summa} so'm depozit qilindi. Yangi balans: {self.balans} so'm")
        else:
            print("Depozit summasi musbat bo'lishi kerak.")

    def yechib_olish(self, summa):
        if summa <= 0:
            print("Yechib olish summasi musbat bo'lishi kerak.")
        elif summa > self.balans:
            print("Hisobda yetarli mablag' mavjud emas.")
        else:
            self.balans -= summa
            print(f"{summa} so'm yechib olindi. Yangi balans: {self.balans} so'm")

    def balansni_tekshirish(self):
        print(f"Hozirgi balans: {self.balans} so'm")
        return self.balans

hisob = BankAccount(100000)
hisob.deposit_qilish(50000)
hisob.yechib_olish(70000)
hisob.balansni_tekshirish()

# 2.
# Uzunlik va kenglik atributlari bilan Tortburchak clasini yarating.
# Maydon, perimetrni hisoblash uchun maydon, perimetr va kvadrat
# metr usullarini qo'llang va to'rtburchaklar mos ravishda
# kvadrat ekanligini tekshiring.

class Tortburchak:
    def __init__(self,uzunlik,kenglik):
        self.uzunlik = uzunlik
        self.kenglik = kenglik

    def maydon(self,):
        return self.uzunlik * self.kenglik

    def perimetr(self,):
        return 2 * (self.uzunlik + self.kenglik)

    def kvadratmi(self,):
        if self.uzunlik == self.kenglik:
            print("Kvadrat")
        else:
            print("Kvadrat emas")

shakl = Tortburchak(5,5)
print(f"Tortburchak yuzasi: {shakl.maydon()} ga teng")
print(f"Tortburchak perimetri: {shakl.perimetr()} ga teng")
shakl.kvadratmi()

# # 3.
# Atributlari nomi, yoshi va baholari bilan Talaba clasini yarating.
# Baho qoʻshish, oʻrtacha bahoni hisoblash va talaba xulosasini
# chop etish uchun mos ravishda qoʻshish_baho, oʻrtacha_hisoblash va
# chop_xulosa usullarini qoʻllang.

class Talaba:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.baholar = []
    def baho_qoshish(self,baho):
        self.baholar.append(baho)
    def ortachani_hisoblash(self):
        if self.baholar:
            return sum(self.baholar) / len(self.baholar)
        return 0
    def talaba_xulosasi(self):
        ortacha = self.ortachani_hisoblash()
        print(f"Ism: {self.name}")
        print(f"Yosh: {self.age}")
        print(f"O'rtacha baho: {ortacha:.2f}")

student1 = Talaba("Ali", 20)
student1.baho_qoshish(90)
student1.baho_qoshish(85)
student1.baho_qoshish(88)
student1.talaba_xulosasi()

# 4.
# Atribut radiusi bilan Doira clasini yarating. Doira maydonini,
# aylanasini va diametrini mos ravishda hisoblash uchun maydon,
# aylana va diametr usullarini qo'llang.

import math

class Doira:
    def __init__(self, radius):
        self.radius = radius

    def maydon(self):
        return math.pi * self.radius ** 2

    def aylana(self):
        return 2 * math.pi * self.radius

    def diametr(self):
        return 2 * self.radius

doira = Doira(5)

print("Radius:", doira.radius)
print("Maydon:", doira.maydon())
print("Aylana:", doira.aylana())
print("Diametr:", doira.diametr())

Radius: 5
Maydon: 78.53981633974483
Aylana: 31.41592653589793
Diametr: 10

# 5.
# Sarlavha, muallif va joriy_sahifa atributlari bilan sinf kitobini
# yarating. Kitobni ma`lum bir sahifada ochish, sahifani aylantirish
# va kitobni mos ravishda 1-sahifadan qayta ishga tushirish uchun ochish,
# sahifani ochish va qayta ishga tushirish usullarini qo`llang.

class Kitob:
    def __init__(self, sarlavha, muallif):
        self.sarlavha = sarlavha
        self.muallif = muallif
        self.joriy_sahifa = 1

    def sahifa_ochish(self, sahifa):
        if sahifa >= 1:
            self.joriy_sahifa = sahifa
            print(f"{self.sarlavha} kitobi {self.joriy_sahifa}-sahifada ochildi.")
        else:
            print("Sahifa raqami 1 yoki undan katta bo'lishi kerak.")

    def sahifa_aylantirish(self):
        self.joriy_sahifa += 1
        print(f"{self.joriy_sahifa}-sahifaga o‘tildi.")

    def qayta_boshlash(self):
        self.joriy_sahifa = 1
        print(f"{self.sarlavha} kitobi boshidan o‘qilmoqda (1-sahifa).")

kitob1 = Kitob("Alkimyogar", "Paulo Koel'o")
kitob1.sahifa_ochish(25)
kitob1.sahifa_aylantirish()
kitob1.qayta_boshlash()

# Class Method vazifalari:
# 6.
# Dog nomli klass yarating, unda total_dogs nomli klass darajasidagi
# atribut bo‘lsin va get_total_dogs nomli metod bo‘lib, u yaratilgan
# itlar sonini qaytarsin.

class Dog:
    total_dogs = 0
    def __init__(self):
        Dog.total_dogs += 1
    def get_total_dogs(self):
        return Dog.total_dogs
dog1 = Dog()
dog2 = Dog()
dog3 = Dog()
print(dog1.get_total_dogs())
print(dog2.get_total_dogs())
print(dog3.get_total_dogs())

# 7.
# Computer nomli klass yarating, unda total_computers va computers_list
# nomli klass darajasidagi atributlar bo‘lsin. add_computer nomli
# metodni amalga oshiring, u kompyuter obyektini ro‘yxatga qo‘shadi va
# total_computers hisoblagichini yangilaydi.

class Computer:
    total_computers = 0
    computers_list = []

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def add_computer(self):
        Computer.computers_list.append(self)
        Computer.total_computers += 1

    def __str__(self):
        return f"{self.brand} {self.model}"

obj1 = Computer("Dell", "XPS 13")
obj2 = Computer("Apple", "MacBook 14 Pro")
obj3 = Computer("HP", "Spectre x360")
obj1.add_computer()
obj2.add_computer()
obj3.add_computer()
print("Jami kompyuterlar soni:", Computer.total_computers)
print("Ro'yxatdagi kompyuterlar:")
for comp in Computer.computers_list:
    print("-", comp)

# 8.
# Xodimlar nomli klass yarating, unda klass darajasidagi
# jami xodimlar soni va xodimlar ro‘yxati atributlari
# bo‘lsin. hire_employee nomli metodni amalga oshiring, u xodimning
# nusxasini ro‘yxatga qo‘shadi va total_employees sonini yangilaydi.

class Xodimlar:
    jami_xodimlar = 0
    xodimlar_royxati = []

    def __init__(self,name,lavozimi):
        self.name = name
        self.lavozimi = lavozimi

    def hire_employee(self):
        Xodimlar.xodimlar_royxati.append(self)
        Xodimlar.jami_xodimlar += 1

    def __str__(self):
        return f"{self.name} - {self.lavozimi}"

emp1 = Xodimlar("Ali", "Dasturchi")
emp1.hire_employee()
emp2 = Xodimlar("Laylo", "Dizayner")
emp2.hire_employee()
print(f"Jami xodimlar soni: {Xodimlar.jami_xodimlar}")
print("Xodimlar ro'yxati:")
for emp in Xodimlar.xodimlar_royxati:
    print(emp)

# 9.
# Television nomli klass yarating, unda o'rtacha_ekran_o'lchami
# nomli class darajasidagi atribut (klass-level atribut) bo‘lsin va
# update_o'rtacha_ekran_o'lchami nomli metod bo‘lib, har safar
# yangi televizor nusxasi (obyekti) yaratilganda o‘rtacha
# ekran o‘lchamini yangilab borsin.

class Television:
    total_screen_size = 0
    total_televisions = 0
    average_screen_size = 0

    def __init__(self, screen_size):
        self.screen_size = screen_size
        Television.total_screen_size += screen_size
        Television.total_televisions += 1
        self.update_average_screen_size()

    def update_average_screen_size(self):
        Television.average_screen_size = Television.total_screen_size / Television.total_televisions

tv1 = Television(42)
print(f"O'rtacha ekran o'lchami: {Television.average_screen_size}")
tv2 = Television(55)
print(f"O'rtacha ekran o'lchami: {Television.average_screen_size}")
tv3 = Television(32)
print(f"O'rtacha ekran o'lchami: {Television.average_screen_size}")

# 10.
# Course nomli class yarating. Unda class darajasidagi total_courses
# (umumiy kurslar soni) va courses_list (kurslar ro‘yxati) nomli
# atributlar bo‘lsin. add_course nomli metodni amalga oshiring, u
# yangi kurs obyektini ro‘yxatga qo‘shadi va kurslar sonini yangilaydi.

class Course:
    total_courses = 0
    courses_list = []

    def __init__(self, name):
        self.name = name
        self.add_course()

    def add_course(self):
        Course.courses_list.append(self)
        Course.total_courses += 1

course1 = Course("Matematika")
course2 = Course("Fizika")
course3 = Course("Ingliz tili")

print(f"Umumiy kurslar soni: {Course.total_courses}")  # 3 ta kurs
print("Kurslar ro'yxati:")
for course in Course.courses_list:
    print(f"- {course.name},")

# Static Method vazifalari:
# 11.
# Math nomli class yarating. Unda multiply (ko‘paytirish) nomli
# statik metod bo‘lsin. Bu metod ikki sonni qabul qilib,
# ularning ko‘paytmasini qaytarsin.

class Math:
    @staticmethod
    def multiply(a, b):
        return a * b
kopaytma = Math.multiply(6, 7)
print(f"Ko‘paytma: {kopaytma}")

# 12.
# Temperature nomli class yarating. Unda celsius_to_fahrenheit nomli
# statik metod bo‘lsin. Bu metod berilgan haroratni Selsiydan
# Farengeytga o‘zgartirib qaytarsin.

class Temperature:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

harorat_c = 25
harorat_f = Temperature.celsius_to_fahrenheit(harorat_c)
print(f"{harorat_c}°C = {harorat_f}°F")

# 13.
# Distance nomli class yarating. Unda miles_to_kilometers nomli
# statik metod bo‘lsin. Bu metod berilgan masofani mil (miles) dan
# kilometr (kilometers) ga aylantirib qaytarsin.

class Distance:
    @staticmethod
    def miles_to_kilometers(miles):
        return miles * 1.60934

masofa_mil = 1
masofa_km = Distance.miles_to_kilometers(masofa_mil)
print(f"{masofa_mil} mil = {masofa_km} kilometr")

# 14.
# Utility nomli class yarating. Unda is_even nomli statik metod bo‘lsin.
# Bu metod berilgan sonning juft yoki toq ekanligini tekshiradi
# va natijani qaytaradi.

class Utility:
    @staticmethod
    def is_even(number):
        return number % 2 == 0

son = 8
if Utility.is_even(son):
    print(f"{son} — juft son.")
else:
    print(f"{son} — toq son.")

# 15.
# Time nomli class yarating. Unda seconds_to_minutes nomli statik metod
# bo‘lsin. Bu metod berilgan vaqtni sekundlarda qabul qilib,
# uni daqiqa va sekundga ajratib, (daqiqa, sekund) ko‘rinishida
# juftlik (tuple) sifatida qaytarsin.

class Time:
    @staticmethod
    def seconds_to_minutes(seconds):
        minutes = seconds // 60
        remaining_seconds = seconds % 60
        return (minutes, remaining_seconds)

sekund = 125
daqiqa_va_sekund = Time.seconds_to_minutes(sekund)
print(f"{sekund} sekund = {daqiqa_va_sekund[0]} daqiqa va {daqiqa_va_sekund[1]} sekund")



