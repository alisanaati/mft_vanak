import random


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


lst = [random.randint(2, 10000) for i in range(1000)]

lst_prime = [i for i in lst if is_prime(i)]

print(lst_prime)
