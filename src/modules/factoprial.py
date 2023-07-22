
def fact(n):
    if n <= 1:
        return 1
    return n * fact(n-1)

def func(n):
    result = 1
    for i in range(2, (n + 1)):
        result *= i
    return result
