# WHILE sikli mavzusi bo’yicha vazifalar.
# 1. Svetafor: Foydalanuvchidan inputda svetavor qaysi rangda deb so’rang. qizil,
# sariq yoki yashil deb yozmoagunicha, bu xato rang deb qayta so’rayvering. Agar shu
# ranglardan birini tanlasa “rahmat, to’g’ri keladi” degan print chiqazing.

ranglar = ["qizil","sariq","yashil"]
while True:

    rang = input("Svetafor qaysi rangda? ")
    if rang in ranglar:
        print(f"Rahmat, {rang} to’g’ri keladi ")
        break
    else:
        print("bu xato rang")

# 2. Tasodifiy Sonni Topish O'yini: Kompyuter 1 dan 10 gacha bo'lgan tasodifiy son
# o'ylaydi. Foydalanuvchidan ushbu sonni topishni so'rang. Foydalanuvchi to'g'ri sonni
# topguncha davom etadi. Har bir noto'g'ri urinishdan so'ng, "Noto'g'ri, qayta urinib
# ko'ring" deb chiqaring. To'g'ri topilganda, "Tabriklaymiz, siz topdingiz!" deb chiqaring.
# Ko'rsatma: random. dan foydalanib tasodifiy son yarating va while sikli yordamida
# foydalanuvchi kiritmalarini tekshiring.

import random

tasodifiy_son = random.randint(1,10)

while True:

    taxmin_son = int(input("1 dan 10 gacha sonlardan birini tanlang "))
    if taxmin_son == tasodifiy_son:
        print("Tabriklaymiz, siz topdingiz!")
        break
    else:
        print("Noto'g'ri, qayta urinib ko'ring")

# 3. Do'stlar Ro'yxatini Yaratish:
# ● Vazifa: Foydalanuvchidan do'stlarining ismlarini kiritishni so'rang.
# Foydalanuvchi "stop" deb yozmaguncha, yangi ismlar qo'shilaveradi. Oxirida
# barcha do'stlarining ismlari ro'yxatini chiqaring.
# ● Ko'rsatma: While sikli va list metodlaridan foydalanib, ro'yxatni shakllantiring.

dostlar = []

while True:

    ism = input("Do'stlaringizning ismini kiriting: ")

    if ism.lower() == "stop":
        break
    dostlar.append(ism)

print("Do'stlaringiz:")
for ism in dostlar:
    print(ism)

# 4. Valyuta Ayirboshlash Kalkulyatori: Foydalanuvchiga valyuta ayirboshlash
# imkoniyatini bering. U so'mni dollarga almashtirishi mumkin. Valyuta kurslarini
# oldindan belgilang (masalan, 1 USD = 12,600 so'm). Foydalanuvchi summani
# kiritadi, dastur esa hisob-kitobni chiqaradi. Foydalanuvchi "exit" deb yozmaguncha
# dastur davom etadi.exit deb yozsa dastur to’xtaydi

kurs = 12600

while True:

    summa = input("So'm miqdorini kiriting (stop deb yozsangiz dastur to'xtaydi): ")

    if summa.lower() == "stop":
        print("Dastur to'xtatildi.")
        break
    try:
        summa = float(summa)

        dollar = summa / kurs
        print(f"{summa} so'm = {dollar:.2f} dollar")
    except ValueError:
        print("Iltimos, to'g'ri raqam kiriting.")
