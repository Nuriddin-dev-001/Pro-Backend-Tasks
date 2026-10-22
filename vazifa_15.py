# Hash table -> Dict

# CRUD = Create, Read, Update, Delete

d1 = {"ism":"Nuriddin", "yosh":22, "shahar":"Farg'ona"}
d2 = dict (ism = "Nuriddin", yosh = 22, shahar = "Farg'ona")
d3 = dict ([("ism", "Nuriddin"), ("yosh", 22), ("shahar", "Farg'ona")])

d1["malumoti"] = ["Oliy"]   # yangi element qo'shadi

print(d1)
print(d2)
print(d3)


duplicate_keys = {"key1": "value1","key1": "value2","key1": "value3"}
print(duplicate_keys)


# Update
harry_potter_dict = {
    "Harry Potter": "Griffindor",
    "Hermione Granger": "Griffindor",
    "Ron Weasley": "Griffindor",
}

add_characters = {
    "Albus Dumbledore": "Griffindor",
    "Severus Snape": "Slytherin",
}
add_characters1 = [
    ("Minerva McGonagall", "Griffindor"),
    ("Sirius Black", "Griffindor"),
]
harry_potter_dict.update(add_characters)  # add_characters1 ro'yxatini harry_potter_dict ga qo'shadi
harry_potter_dict.update(add_characters1)  # add_characters lug'atini harry_potter_dict ga qo'shadi
print(harry_potter_dict)

# Delete
del harry_potter_dict["Severus Snape"]  # Severus Snape ni delete funksiyasi orqali o'chiradi
harry_potter_dict.pop("Sirius Black")  # Sirius Black ni pop metodi orqali o'chiradi

found = harry_potter_dict.get("Albus Dumbledore", "Not found")  # Albus Dumbledore ni topadi agar topolmasa "Not found" qaytaradi
print(found)  # natija: Griffindor chiqadi

print(harry_potter_dict.setdefault("Remus Lupin", "Slytherin"))  # yangilangan lug'atni chiqaradi


# Items, keys, values
print(list(harry_potter_dict.items()))  # lug'atdagi barcha elementlarni chiqaradi
print(list(harry_potter_dict.keys()))  # lug'atdagi barcha kalitlarni chiqaradi
print(list(harry_potter_dict.values()))  # lug'atdagi barcha qiymatlarni chiqaradi

for key, value in harry_potter_dict.items():  # lug'atdagi barcha elementlarni chiqaradi
    print(f"{key}: {value}")

# Counter
from collections import Counter

counter = Counter(harry_potter_dict.values()) # bu harry potter dictidagi qiymatlarning chastotasini hisoblaydi
print(counter)

num = [1, 1, 2, 3, 3, 5, 5, 6, 6, 6
       ]
counter_num = Counter(num)
print(counter_num)

# ____________________________________________Vazifalar_____________________________________________________________
# 1. stringlar ro'yxatini oladigan va ularni uzunligi bo'yicha guruhlaydigan str_counter(strs) funksiya yozing,
# bunda kalitlar string uzunliklari va qiymatlar shu uzunlikdagi string keladi.
# M: str_counter(["shaftoli", "olma", "nok" ]) -> {8:"shaftoli", 4: "olma", 3: "nok"}

from collections import defaultdict

def str_counter(strs):
    result = defaultdict(list)
    for s in strs:
        result[len(s)].append(s)
    print(dict(result))
str_counter(["shaftoli","uzum","banan"])

# ___________________________________________________________________________________________________________________
# 2. Bir xil uzunlikdagi ikkita listni parametr sifatida oladigan, kalitlar birinchi ro'yxatning
# elementlari va qiymatlar ikkinchi ro'yxatning mos keladigan elementlari bo'lgan dict qaytaradigan merge_list(l1,l2) funksiya yarating.
# M: list_1 = ["a", "b", "c"]
#    list_2 = [1, 2, 3]
#    merge_list(list_1 ,list_2)  -> {"a":1, "b":2, "c":3}

def merge_list(l1, l2):
    return dict(zip(l1, l2))
print(merge_list(["a", "b", "c"],[1, 2, 3]))

# __________________________________________________________________________________________________________________
# 3. Foydalanuvchilarga kontaktlarni qo‘shish, yangilash, o‘chirish va qidirish
# imkonini beruvchi dict ga asoslangan telefon kontaktlar ro'yxati dasturini yarating
# M: contacts = {"Nodir":"+998918602711", "Laziz":"+998908002534"}

contacts = {"Nodir":"+998918602711", "Laziz":"+998908002534"}

while True:
     print("Kontaktlar ro'yxati: ", contacts)
     bolim = input("Bo'limni tanlang: \n1. Qo'shish \n2. Yangilash \n3. O'chirish \n4. Ko'rish \n5. Chiqish \n-> ")

     if bolim == "1":
         name = input("Kontakt nomini kiriting: ")
         number = input("Kontakt raqamini kiriting: ")

         newContact = [name, number]
         contacts[name] = number
     elif bolim == "2":
         update = input("Qaysi kontaktni yangilamoqchisiz: ")
         if update.capitalize() in contacts:
             updateNumber = input("Yangi raqamni kiriting: ")
             contacts[update.capitalize()] = updateNumber
         else:
             print("Bu kontakt mavjud emas")
     elif bolim == "3":
         delete = input("Qaysi kontaktni o'chirmoqchisiz: ")
         if delete.capitalize() in contacts:
             del contacts[delete.capitalize()]
         else:
             print("Bu kontakt mavjud emas")
     elif bolim == "4":
         print(contacts)
     elif bolim == "5":
         break
     else:
         print("Xato bo'lim")


# ________________________________________________________________________________________________________________
# 4. Raqamlar ro'yxatini oladigan va ro'yxatdagi har bir raqamning takrorlanish sonini o'z ichiga
# olgan dict qaytaradigan counter_dict(nums) nomli funksiya yozing.
# M: counter_dict([2,1,1,1) -> {2:1, 1:3} Chunki listda 1ta 2 va 3ta 1bor.

num = [1, 1, 2, 3, 3, 5, 5, 6, 6, 6
       ]
counter_num = Counter(num)
print(counter_num)


# ___________________________________________________________________________________________________________________
# 5. Ballar dict ni(kalit = talaba nomi, qiymat = ball) parametr sifatida oladigan va eng yaxshi ikkita
# o'quvchining ismlari ro'yxatini qaytaradigan max_ball_students(talabalar) funksiya yozing.
# max_ball_students({"Akmal":64, "Tohir":55, "Nodir":76, "Zafar":80 }) -> {"Zafar":80, "Nodir":76}

def max_ball_students(talabalar):
    yaxshi_ikkita = dict(Counter(talabalar).most_common(2))
    return yaxshi_ikkita
print(max_ball_students({"Akmal":64, "Tohir":55, "Nodir":76, "Zafar":80}))






















































































