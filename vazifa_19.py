# 1_______________________________________________
def prime_generator():
    def is_prime(number):
        if number < 2:
            return False
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                return False
        return True

    number = 2
    while True:
        if is_prime(number):
            yield number
        number += 1

primes = prime_generator()
for _ in range(6):
    print(next(primes))

# 2_______________________________________________
import itertools

def password_generator(input_string):
    for pwd in itertools.permutations(input_string):
        yield ''.join(pwd)

input_string = "abs"
passwords = password_generator(input_string)
for _ in range(6):
    print(next(passwords))

# 3_______________________________________________
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fibonacci = fibonacci_generator()
for _ in range(10):
    print(next(fibonacci))


# 4_______________________________________________
import itertools

def group_generator(lst, n):
    for group in itertools.combinations(lst, n):
        yield group

my_list = [1, 2, 3, 4]
n = 2
groups = group_generator(my_list, n)
for group in groups:
    print(group)








