def fibonatchi (n):
    if n ==0  or n== 1:
        return 1
    else:
        return (fibonatchi(n-1)) + (fibonatchi(n-2))


print(fibonatchi(10))