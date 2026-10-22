# 1. Stringni katta harfga o'tkazadi
def katta_harf(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@katta_harf
def words():
    return "python"

print(words())
# -----------------------------------------------------
# 2. Stringni reverse qiladi
def teskari_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result[::-1]
    return wrapper

@teskari_decorator
def teskari():
    return "salom"

print(teskari())
# -----------------------------------------------------
# 3. Funksiya ishlashi uchun ketgan vaqtni qaytaradi
import time

def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Dastur {end_time - start_time:.2f} sekundda ishladi.")
        return result
    return wrapper

@time_decorator
def time_funksiya():
    time.sleep(1)
    return "Bajarildi"

print(time_funksiya())
# -----------------------------------------------------
# 4. Funksiya necha marta chaqirilganini hisoblaydi
def call_counter(func):
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"{func.__name__} funksiyasi {count}-marta chaqirildi.")
        return func(*args, **kwargs)

    return wrapper

@call_counter
def greet(name):
    return f"Salom, {name}!"

print(greet("Ali"))                # greet funksiyasi 1-marta chaqirildi. || Salom, Ali!
print(greet("Bobur"))              # greet funksiyasi 2-marta chaqirildi. || Salom, Bobur!
print(greet("Sardor"))             # greet funksiyasi 3-marta chaqirildi. || Salom, Sardor!






































































