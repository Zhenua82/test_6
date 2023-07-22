
# def f(a):
#     a = a - 1
#     x = a
#     if a > 0:
#         x = a * (a + 1)
#         return f(a)
#     else:
#         print(x)
        
# f(3)

# def factorial(number):
#     result = 1
#     for i in range(2, (number + 1)):
#         result *= i
#     return result


# list_factorial = list()
# n = int(input('Введите любое натуральное число: ', ))
# source_factorial = factorial(n)
# for e in range (source_factorial, 0, -1):
#     list_factorial.append(factorial(e)) 
# print(list_factorial)


def fact(n):
    if n <= 1:
        return 1
    return n * fact(n-1)

print(fact(6))