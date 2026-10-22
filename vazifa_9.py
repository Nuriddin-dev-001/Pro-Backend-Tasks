# # 1.Ob-havo tavsifi:
# user=int(input("Havo haroratini kiriting; "))
# if user <= 0:
#     print("Sovuq")
# elif (user > 0 and user < 20):
#     print("Salqin")
# elif user >= 20 and user <= 30:
#     print("Iliq")
# else:
#     print("Issiq")
#
# # 2.Internet do`kon chegirmasi:
# summa = int(input("Xarid summasini kiriting: "))
# if summa <= 50000:
#     chegirma = 0
# elif 50000 < summa <= 100000:
#     chegirma = 0.05
# else:
#     chegirma = 0.10
# yakuniy_narx = summa - summa * chegirma
# print(f"Chegirma: {chegirma * 100}%")
# print(f"Yakuniy narx: {yakuniy_narx} so'm")
#
# # 3. Tizmga kirish:
# login="admin"
# parol="12345"
# user_login=input("Login: ")
# user_parol=input("Parol: ")
# if user_login==login and user_parol==parol:
#     print("Xush kelibsiz admin!")
# else:
#     print("login yoki parol xato!")
#
# # 4. Film yosh cheklovi:
# user=int(input("Yoshingiz; "))
# if user<13:
#     print("Sizga ushbu film tavsiya qilinmaydi!")
# elif user>=13 and user<18:
#     print("Filmni ota onangiz bilan ko`shingiz mumkin!")
# else:
#     print("Filmni tomosha qilishingiz mumkin!")
#
# # 5. Restoran menyusi:
# tanlov = input("Tanlang (1, 2, yoki 3): ")
# if tanlov == "1":
#         print("Taom: Osh")
#         print("Narxi: 40,000 so'm")
#         print("Tayyorlanish vaqti: 10 daqiqa")
# elif tanlov == "2":
#         print("Taom: Mastava")
#         print("Narxi: 25,000 so'm")
#         print("Tayyorlanish vaqti: 10 daqiqa")
# elif tanlov == "3":
#         print("Taom: Shashlik")
#         print("Narxi: 20,000 so'm")
#         print("Tayyorlanish vaqti: 10 - 15 daqiqa")
# else:
#         print("Noto'g'ri tanlov! Iltimos, 1, 2 yoki 3 ni tanlang.")
#
# #6. Foydalanuvchidan email manzilini olish:
# email = input("Iltimos, email manzilingizni kiriting: ")
# if email.find("@") == -1 or email.find(".") == -1:
#     print("Noto'g'ri email manzili")
# else:
#     print("Email qabul qilindi")

# 7. Talaba baholash tizimi:
ball=int(input("Balni kiriting: "))
if ball > 85 and ball <= 100:
    print("5 baho!")
elif ball >= 70 and ball < 85:
    print("4 baho!")
elif ball >= 55 and ball < 70:
    print("3 baho!")
else:
    print("2 baho")

# 8. Bankomatdan pul yechish:
balans=int(input("Karta balansini kiriting: "))
summa=int(input("Yechiladigan summani kiriting: "))
if balans < summa:
    print("Hisobda yetarli mablag` mavjud emas!")
elif summa < 5000:
    print("Minimal yechish summasi 5 000 so`m!")
else:
    print(f"Pul muvaffaqiyatli yechildi: balans-{balans-summa}")

# 9. Ish Jadvalini Tekshirish:
kun = input("Bugun qaysi kun?  ")
if kun in ["Shanba", "Yakshanba"]:
    print("Bugun dam olish kuni")
else:
    print("Bugun ish kuni")

# 10. Mobil Tarif Tanlash:
tarif=int(input("Oyiga necha GB internet trafikdan foydalanasiz? "))
if tarif <= 10:
    print("Sizga 'Mini' tarifi mos keladi.")
elif  10 < tarif <= 20:
    print("Sizga 'Standart' tarifi mos keladi.")
else:
    print("Sizga 'Unlimited' tarifi mos keladi.")
