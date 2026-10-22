# 25-dars vazifasi Nuriddin Inomov
# 1__________________________________________________________________
# "Texnika" parent klass.Konstruktorida esa(brand, model, type)
# parametrlar bor. info() - (brand, model, type) ni print qilib beradi.
#
#"Notebooks" child klassi bor.Unda konstruktirida qo'shimcha
# (video_card, ram, display). more_info() - (brand, model, type,
# video_card, ram, display) ni print qilib beradi.
#
# "Televisions" child klassi bor.Unda konstruktirida(size, display)
# parametrlari bor. more_info() - (brand, model, type, size, display)
# ni print qilib beradi.
#
# "Smartphones" child klassi bor. Unda konstruktirida(size, sim_count)
# parametrlari bor. more_info() - (brand, model, type, size, sim_count)
# ni print qilib beradi.
#

class Texnika:
    def __init__(self, brand, model, type):
        self.brand = brand
        self.model = model
        self.type = type

    def info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Type: {self.type}")

class Notebooks(Texnika):
    def __init__(self, brand, model, type, video_card, ram, display):
        super().__init__(brand, model, type)
        self.video_card = video_card
        self.ram = ram
        self.display = display

    def more_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Type: {self.type}, "
              f"Video Card: {self.video_card}, RAM: {self.ram}, Display: {self.display}")

class Televisions(Texnika):
    def __init__(self, brand, model, type, size, display):
        super().__init__(brand, model, type)
        self.size = size
        self.display = display

    def more_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Type: {self.type}, "
              f"Size: {self.size}, Display: {self.display}")

class Smartphones(Texnika):
    def __init__(self, brand, model, type, size, sim_count):
        super().__init__(brand, model, type)
        self.size = size
        self.sim_count = sim_count

    def more_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Type: {self.type}, "
              f"Size: {self.size}, SIM Count: {self.sim_count}")


notebook = Notebooks("Dell", "XPS 13", "Notebook", "Intel Iris Xe", "16GB", "13.3 inch")
notebook.info()
notebook.more_info()

tv = Televisions("Samsung", "QLED Q60", "Television", "55 inch", "QLED")
tv.info()
tv.more_info()

phone = Smartphones("Apple", "iPhone 14", "Smartphone", "6.1 inch", 2)
phone.info()
phone.more_info()
# 2_______________________________________________________________
# "Transport" parent klass.Konstruktorida esa(brand, model, type)
# parametrlari bor. info() - (brand, model, type) ni print qilib beradi.
#
# "ElentroCars" - child klassi bor.Unda konstruktirida qo'shimcha
# (battery_life, chargin_time). more_info() - (brand, model, type,
# battery_life, chargin_time) ni print qilib beradi.
#
# "SportCars" - child klassi bor.Unda konstruktirida qo'shimcha
# (motor, color). more_info() - (brand, model, type, motor, color) ni
# print qilib beradi.
#
# "Truck" - child klassi bor.Unda konstruktirida qo'shimcha
# (motor, height, long, wieght). more_info() - (brand, model, type,
# height, long, wieght) ni print qilib beradi.

class Transport:
    def __init__(self,brand,model,type):
        self.brand = brand
        self.model = model
        self.type = type
    def info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Kuzov: {self.type}")

class ElectroCars(Transport):
    def __init__(self,brand,model,type,battery_life, chargin_time):
        super().__init__(brand, model, type,)
        self.baterry_life = battery_life
        self.chargin_time = chargin_time

    def more_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Kuzov: {self.type},"
              f" Batareya hajmi: {self.baterry_life}, Quvvatlash vaqti: {self.chargin_time}")

class SportCars(Transport):
    def __init__(self,brand,model,type,motor,color):
        super().__init__(brand,model,type)
        self.motor = motor
        self.color = color

    def more_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Kuzov: {self.type},"
              f" Motor: {self.motor}, Rangi: {self.color}")

class Truck(Transport):
    def __init__(self,brand, model, type,motor, height, long, wieght):
        super().__init__(brand, model, type)
        self.motor = motor
        self.height = height
        self.long = long
        self.wieght = wieght

    def more_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Kuzov: {self.type},"
              f" Balandlik: {self.height}, Uzunligi: {self.long}, Vazn: {self.wieght}")

Electromobil = ElectroCars("BYD","Song plus","Krossover","100 kw","3 soat")
Electromobil.info()
Electromobil.more_info()

Sportcar = SportCars("Bugatti","Chiron","Sport","V16 Twinturbo 1200 HP","Qora")
Sportcar.info()
Sportcar.more_info()

Truck = Truck("Mersedes Benz","M 324","Yuk tashuvchi","2000 HP","3050 mm","12 000 mm","15 000 kg",)
Truck.info()
Truck.more_info()
# 3.1_____________________________________________________________
#"University" - parent klass. Konstruktorida esa (university)
# parametrlari bor. info() - (university) ni print qilib beradi.
#
#"Staff" - child klass. Unda konstruktirida qo'shimcha (first_name,
# last_name, age) parametrlari bor. staff_info() - (university,
# first_name, last_name, age) ni print qilib beradi.
#
#"Student" - child klass. U "Staff" dan vorislik oladi. Unda
# konstruktirida qo'shimcha (group) parametrlari bor. more_info() -
# (university, first_name, last_name, age, group) ni print qilib beradi.
#
#"Teacher" - child klass. U "Staff" dan vorislik oladi. Unda
# konstruktirida qo'shimcha (position, subject) parametrlari bor.
#more_info() - (university, first_name, last_name, position, subject) ni print qilib beradi.
#
#"OtherStaff" - child klass. U "Staff" dan vorislik oladi. Unda
# konstruktirida qo'shimcha (position) parametrlari bor.
#more_info() - (university, first_name, last_name, position,) ni print qilib beradi.

class University:
    def __init__(self, university):
        self.university = university

    def info(self):
        print(f"Universitet: {self.university}")

class Staff(University):
    def __init__(self, university, first_name, last_name, age):
        super().__init__(university)
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def staff_info(self):
        print(f"Universitet: {self.university}")
        print(f"Ismi: {self.first_name} {self.last_name}")
        print(f"Yoshi: {self.age}")

class Student(Staff):
    def __init__(self, university, first_name, last_name, age, group):
        super().__init__(university, first_name, last_name, age)
        self.group = group

    def more_info(self):
        print(f"Universitet: {self.university}")
        print(f"Ismi: {self.first_name} {self.last_name}")
        print(f"Yoshi: {self.age}")
        print(f"Guruh: {self.group}")

class Teacher(Staff):
    def __init__(self, university, first_name, last_name, age, position, subject):
        super().__init__(university, first_name, last_name, age)
        self.position = position
        self.subject = subject

    def more_info(self):
        print(f"Universitet: {self.university}")
        print(f"Ismi: {self.first_name} {self.last_name}")
        print(f"Yoshi: {self.age}")
        print(f"Lavozimi: {self.position}")
        print(f"Mavzu: {self.subject}")

class OtherStaff(Staff):
    def __init__(self, university, first_name, last_name, age, position):
        super().__init__(university, first_name, last_name, age)
        self.position = position

    def more_info(self):
        print(f"Universitet: {self.university}")
        print(f"Ismi: {self.first_name} {self.last_name}")
        print(f"Yoshi: {self.age}")
        print(f"Lavozimi: {self.position}")

Talaba = Student("TATUFF", "Nuriddin", "Inomov", 21, "541-23")
Oqituvchi = Teacher("TATUFF", "Ahror", "Qayumov", 45, "Professor", "Dasturlash")
Ishchi_xodim = OtherStaff("TATUFF", "Gulbahor", "Ismoilova", 35, "Kutubxonachi")

print("\n--- Talaba haqida ma'lumot ---")
Talaba.more_info()

print("\n--- O'qituvchi haqida ma'lumot ---")
Oqituvchi.more_info()

print("\n--- Xodim haqida ma'lumot ---")
Ishchi_xodim.more_info()

# 3.2______________________________________________________________
# "Object" - child klass.U "University" dan vorislik oladi.Unda
# konstruktirida qo'shimcha (name) parametrlari bor. object_info() -
# (university, name) ni print qilib beradi.
#
# "Computer" - child klass.U "Object" dan vorislik oladi.Unda
# konstruktirida qo 'shimcha (soni, tizimi, holati) parametrlari bor.
# object_more_info() - (university, name, soni, tizimi, holati) ni print qilib beradi.
#
# "Mebel" - child klass.U "Object" dan vorislik oladi.Unda
# konstruktirida qo'shimcha (soni, turi, holati) parametrlari bor.
# object_more_info() - (university, name, soni, turi, holati) ni print qilib beradi. Namuna obyektlar bilan sinov

class University:
    def __init__(self, university):
        self.university = university

    def info(self):
        print(f"Universitet: {self.university}")

class Object(University):
    def __init__(self, university, name):
        super().__init__(university)
        self.name = name

    def object_info(self):
        print(f"Universitet: {self.university}")
        print(f"Jihoz nomi: {self.name}")

class Computer(Object):
    def __init__(self, university, name, soni, tizimi, holati):
        super().__init__(university, name)
        self.soni = soni
        self.tizimi = tizimi
        self.holati = holati

    def object_more_info(self):
        print(f"Universitet: {self.university}")
        print(f"Jihoz nomi: {self.name}")
        print(f"Soni: {self.soni}")
        print(f"Tizimi: {self.tizimi}")
        print(f"Holati: {self.holati}")

class Mebel(Object):
    def __init__(self, university, name, soni, turi, holati):
        super().__init__(university, name)
        self.soni = soni
        self.turi = turi
        self.holati = holati

    def object_more_info(self):
        print(f"Universitet: {self.university}")
        print(f"Jihoz nomi: {self.name}")
        print(f"Soni: {self.soni}")
        print(f"Turi: {self.turi}")
        print(f"Holati: {self.holati}")

Kompyuter = Computer("TATUFF", "Kompyuter", 25, "Windows 11", "Yangi")
Mebel = Mebel("TATUFF", "Stol", 40, "Yozuv stoli", "Yaxshi")

print("\n--- Kompyuter haqida ma'lumot ---")
Kompyuter.object_more_info()

print("\n--- Mebellar haqida ma'lumot---")
Mebel.object_more_info()
