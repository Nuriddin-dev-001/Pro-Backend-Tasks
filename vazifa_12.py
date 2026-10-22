                            # 12-dars Funksiya mavzusi.
# 1.
print(1)
n = input("Ismingizni kiriting ")
f = input("Familiyangizni kiriting ")
a = input("Yoshingizni kiriting ")
def user_data(n, f, a):
    print(f""""
    ____________________________
    |                          |
    |      Ism = {n}      |
    |      familiya = {f}   |
    |      Yosh = {a}           |
    |__________________________|
""")
user_data(n, f, a)

# 2.
print(2)
def find_max(a, b, c):
    max_val = max(a, b, c)
    max_vals = []

    if a == max_val:
            max_vals.append("A")
    if b == max_val:
            max_vals.append("B")
    if c == max_val:
            max_vals.append("C")

    max_vals_str = " va ".join(max_vals)
    print(f"Eng katta son {max_val}, bu {max_vals_str} ga tegishli.")

a = int(input("Birinchi sonni kiriting: "))
b = int(input("Ikkinchi sonni kiriting: "))
c = int(input("Uchinchi sonni kiriting: "))

find_max(a, b, c)

# 3.
print(3)
def find_letter_count(word, letter):
    count = word.lower().count(letter.lower())
    print(f"Matnda {letter} {count} martta qatnashgan.")

word = input("Matn kiriting! ")
letter = input("Ixtiyoriy harf kiriting men uni matnda necha marta qatnashganini topaman! ")

find_letter_count(word, letter)

# 4.
print(4)
def list_sum(myList):
    total = sum(myList)
    print(f"Listdagi elementlar yig'indisi {total} ga teng.")

myList = [2,5,11,32,9]

list_sum(myList)

# 5.
print(5)
def daraja(a, b):
    natija = a ** b
    print(f"{a} ning {b}-darajasi {natija}ga teng")

daraja(5,15)

# 6.
print(6)
def daraja4(a,b,c,d):
    natija1 = a**b
    natija2 = a**c
    natija3 = a**d
    print(f"{a} ning {b}-darajasi {natija1}ga, {c}-darajasi {natija2}, {d}-darajasi {natija3} ga teng")

daraja4(5,4,7,8)

# 7.
print(7)
def digit_count_and_sum(word):
    soni = 0
    yigindisi = 0
    for i in word:
        if i.isdigit():
            soni += 1
            yigindisi += int(i)
    print(f"{word} ichidagi raqamlar soni {soni} ta !" )
    print(f"{word} ichidagi raqamlar yig'indisi {yigindisi}ga teng !")

digit_count_and_sum("ab1c23d4")

# 8.
print(8)
def add_right(a, b):
    print(f"{a}{b}")

add_right(20,26)

# 9.
print(9)
def add_left(a, b):
    print(f"{b}{a}")

add_left(20, 26)

# 10.
print(10)
a = [4, 5, 6, 7, 8, 9]

def work_with_list(a):
    min_a = min(a)
    for i in range(len(a)):
        a[i] = a[i] * min_a
    print(a)

work_with_list(a)

# 11.
print(11)
def big_sales(sales):
    return max(sales, key=sales.get)

sales = {
    'yanvar': 12000,
    'mart': 6000,
    'aprel': 15000,
    'sentyabr': 9000,
    'dekabr': 10000
}
print(big_sales(sales))

# 12.
print(12)
def min_max(numbers, max_num, min_num):
    maxi = max(numbers)
    mini = min(numbers)
    if maxi == max_num:
        print(f"Ha, {maxi} katta!")
    if mini == min_num:
        print(f'Ha, {mini} kichik!')
    else:
        print(f'Xato! eng kattasi {maxi}, eng kichigi {mini}')

min_max([1,2,3,4,5],2,3)

# 13.
print(13)
def expensiveProducts(products):
    product = products[0]
    for i in products:
        if i['price'] > product["price"]:
            product = i
    print(f"Eng qimmat telefon nomi: <<{product['name']}>>, narxi: {product['price']}$")

products=[
  {
    "name": "Vertu Metavertu Max",
    "price": 50000
  },
  {
    "name": "Iphone 17 pro max",
    "price": 1500
  },
  {
    "name": "Samsung S26 Ultra ",
    "price": 1200
  },
  {
    "name": "Vertu iVERTU",
    "price": 1500
  },]
expensiveProducts(products)