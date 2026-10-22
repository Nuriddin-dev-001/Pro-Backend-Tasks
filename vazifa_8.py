 #List methodlari bilan ishlash

#1 append   'listga oxiriga bittadan element qo`shadi'
mashina = ['Bugatti', 'Ferrari', 'Lamborghini']
mashina.append('Pagani')
print(1,mashina)

#2 extend  'listga listni qo`shadi'
mashina = ['Bugatti', 'Ferrari', 'Lamborghini']
mashina2 = ['Ford', 'Mers', 'Volvo']
mashina.extend(mashina2)
print(2,mashina)

#3 insert  'listga elementni belgilangan index bo`yicha qo`shadi'
mashina = ['Bugatti', 'Ferrari', 'Lamborghini']
mashina.insert(1, "Pagani")
print(3,mashina)

#4 pop 'elementni alratib oladi '
mashina = ['Bugatti', 'Ferrari', 'Lamborghini', 'Pagani']
x=mashina.pop(1)
print(4,mashina)
print(x)

#5 remove 'belgilangan elementni olib tashlaydi'
mashina = ['Bugatti', 'Ferrari', 'Lamborghini']
mashina.remove("Ferrari")
print(5,mashina)

#6 clear 'tozalaydi'
mashina = ['Bugatti', 'Ferrari', 'Lamborghini']
mashina.clear()
print(6,mashina)

#7 copy 'nusxa oladi va u bilan islaganda asli o`zgarmaydi '
mashina = ['Bugatti', 'Ferrari', 'Lamborghini']
x = mashina.copy()
print(7,x)

#8 count 'sanaydi '
mashina = ['Bugatti', 'Ferrari', 'Pagani', 'Lamborghini']
x = mashina.count("Pagani")
print(8,x)

#9 index 'qaysi indexda turganini qaytaradi'
mashina = ['Bugatti', 'Ferrari', 'Pagani', 'Lamborghini']
x = mashina.index("Pagani")
print(9,x)

#10 reverse 'listni chappasiga o`giradi'
mashina = ['Bugatti', 'Ferrari', 'Pagani', 'Lamborghini']
mashina.reverse()
print(10,mashina)

#11 sort 'tartiblaydi'
mashina = ['Lamborghini', 'Ferrari', 'Bugatti', 'Pagani']
mashina.sort(reverse=False)
print(11,mashina)












