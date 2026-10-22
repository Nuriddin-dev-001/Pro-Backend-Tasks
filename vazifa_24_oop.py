# 24-Dars_OOP_uy_vazifasi

print('1.')
class Oson1:
    a = 4

    def print_a(cls):
        print(cls.a)

Oson1.print_a(Oson1)

print('2.')
class Oson2:
    a = 0
    b = 0
    @classmethod
    def summa(cls):
        print(cls.a + cls.b)
Oson2.a = 10
Oson2.b = 15
Oson2.summa()

print('3.')
class Oson3:
    a = 0
    @classmethod
    def plus_minus(cls):
        if cls.a < 0:
            print("manfiy")
        elif cls.a > 0:
            print("musbat")
        else:
            print("nolga teng")
Oson3.a = -6
Oson3.plus_minus()

print('4.')
class Oson4:
    a = 0
    @classmethod
    def toq_juft(cls):
        if cls.a % 2 == 0:
            print("juft")
        else:
            print("toq")
Oson4.a = 5
Oson4.toq_juft()

print('5.')
class Oson5:
    a = 0
    b = 0
    @classmethod
    def daraja(cls):
        print(cls.a ** cls.b)
Oson5.a = 5
Oson5.b = 3
Oson5.daraja()

print('6.')
class MyClass6:
    words = []
    @classmethod
    def add_word(cls,word):
        cls.words.append(word)
    @classmethod
    def remove(cls,word):
        if word in cls.words:
            cls.words.remove(word)
        else:
            print(f"{word} ro'yxatda yo'q")
obj = MyClass6
obj.add_word("Salom")
obj.add_word("dunyo")
print(obj.words)

obj.remove("dunyo")
print(obj.words)

print('7.')
class MyClass7:
    myDict = {}
    @classmethod
    def add_elem(cls, key, val):
        if key not in cls.myDict:
            cls.myDict[key] = val
    @classmethod
    def update_elem(cls, key, val):
        if key in cls.myDict:
            cls.myDict[key] = val

MyClass7.add_elem("a", 1)
print(MyClass7.myDict)

MyClass7.add_elem("a", 100)
print(MyClass7.myDict)
class Oson2:
    a = 0
    b = 0
    @classmethod
    def summa(cls):
        print(cls.a + cls.b)
Oson2.a = 10
Oson2.b = 15
Oson2.summa()
MyClass7.update_elem("a", 200)
print(MyClass7.myDict)

MyClass7.update_elem("b", 300)
print(MyClass7.myDict)

print('8.')
class MyClass8:
    numbers = [1, 2, 3, 4]
    @classmethod
    def compare_lists(cls, new_list):
        sum_numbers = sum(cls.numbers)
        sum_new_list = sum(new_list)

        if sum_numbers > sum_new_list:
            print(f"Katta list: {cls.numbers}")
        elif sum_numbers < sum_new_list:
            print(f"Katta list: {new_list}")
        else:
            print("Ikkala list ham teng!")
MyClass8.compare_lists([1, 2, 3, 4])
MyClass8.compare_lists([10, 20, 30, 40])

print('9.')
class MyClass:
    list1 =[13,15,21,54,32]
    list2 =[64,23,29,13,35]
    @classmethod
    def list1_max(cls):
        return max(cls.list1)
    @classmethod
    def list2_max(cls):
        return max(cls.list2)
    @classmethod
    def sum_of_two_max(cls):
        result = cls.list1_max() + cls.list2_max()
        print(f"maximumlar yig'indisi {result}")
MyClass.list1_max()
MyClass.list2_max()
MyClass.sum_of_two_max()

print('10.')
class MyClass:
    numbers = []
    @classmethod
    def divide(cls,d):
        return [num for num in cls.numbers if num % d == 0]
MyClass.numbers = [1,2,3,4,5,6,7,8,9,10]
print(MyClass.divide(2))
