# #Foydalanuvchi qiziqishi haqida.
# qiziqish = input("Nimaga qiziqasiz: ").lower()
# if qiziqish.find("kitob") >=0:
#     janr = input("Sizga qaysi janrdagi kitoblar yoqadi? ").lower()
#     if janr.find("diniv") >=0:
#         print("Sizga 'Hadis va hayot' kitoblar to'plamini sovg'a qilamiz!")
#     elif janr.find("detektiv") >=0:
#         print("Sizga 'Shaytanat' kitobini sovg'a qilamiz!")
#     else:
#         print("Sizga qiziq bo'lishi mumkin bo'lgan turli kitoblarimiz bor!")
# elif qiziqish.find("sport") >=0:
#     tur = input("Sizga qaysi sport turi yoqadi? ").lower()
#     if tur.find("futbol") >=0:
#         club = input("Qaysi klubga muhlislik qilasiz? ").lower()
#         if club.find("real") >=0 or club.find("barsa") >=0 or club.find("barselona") >=0:
#             print("Sizga El Clasico o'yiniga chipta sovg'a qilamiz!")
#         else:
#             print("Sizga sevimli jamoangizning maxsus sovg'asini beramiz!")
#     else:
#         print("Sizning sportga qiziqishingiz biz uchun qiziq, sovg'a tayyorlaymiz!")
# else:
#     print("Ajoyib! Sizning qiziqishingizni bilish biz uchun muhim!")

# #Vazifalar.
# # 1. masala
# pochtalar = ["user1@gmail.com", "user2yahoo.com", "user3@outlook.com"]
# for email in pochtalar:
#     if "@" in email and "." in email:
#         print(f"{email} - Emailingiz qabul qilindi:")
#     else:
#         print(f"{email} - Noto'g'ri email:")
#
# # 2. masala
# parollar = ["password123", "Qwerty!", "admin", "StrongPass1!"]
# for parol in parollar:
#     if len(parol) < 8:
#         print(f"{parol}: Juda qisqa")
#     elif not (r"[0-9]", parol) or not (r"[!@#$%^&*(),.?\":{}|<>]", parol):
#         print(f"{parol}: Kuchsiz parol")
#     else:
#         print(f"{parol}: Kuchli parol")
#
# # 3. masala
# haroratlar = [31, 22, 19, 25, 20, 33]
# ortacha_harorat = sum(haroratlar) / len(haroratlar)
# print(f"O'rtacha harorat: {ortacha_harorat:.2f}")
# for harorat in haroratlar:
#     if harorat < 22:
#         print(f"{harorat}°C - Salqin kun")
#     elif 22 <= harorat < 30:
#         print(f"{harorat}°C - Iliq kun")
#     else:
#         print(f"{harorat}°C - Issiq kun")
#
# # 4. masala
# mavjud_taomlar = ["Osh", "Shashlik", "Manti", "Lag'mon"]
# buyurtma = input("Nima buyurasiz: ")
# if buyurtma in mavjud_taomlar:
#     print("Buyurtmangiz qabul qilindi")
# else:
#     print("Kechirasiz, bunday taom yo'q")
#
# 5. masala
yoshlar = [16, 21, 17, 30, 25]
for yosh in yoshlar:
    if yosh < 18:
        print("Yosh chegarasiga yetmagan")
    else:
        print("Xush kelibsiz")

# 6. masala
xabarlar = ["Yangi xabar", "Batareya past", "Yangilanish mavjud"]
for xabar in xabarlar:
    if xabar == "Batareya past":
        print("Telefoningizni quvvatlang")

# 7. masala
fayllar = ["kitob.jpg", "kok jiguli.mp3", "tabiat.jpg", "malohat.mp3", "iphone16.jpg"]
musiqalar = []
rasmlar = []
for fayl in fayllar:
    if fayl.find(".jpg") != -1:
        rasmlar.append(fayl)
    elif fayl.find(".mp3") != -1:
        musiqalar.append(fayl)
print("Rasmlar:", rasmlar)
print("Musiqalar:", musiqalar)


