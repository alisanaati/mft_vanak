def factorial(c):
    fact = 1
    for i in range(1, c + 1):
        fact = fact * i
    return fact


def combination(m, n):
    res = factorial(m) / (factorial(m - n) * factorial(n))
    return int(res)

def pascal(n):
    lst = []
    for i in range(0,n+1):
        res = combination(n , i)
        lst.append(res)
    return lst



print(pascal(10))

