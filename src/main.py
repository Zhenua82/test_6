import modules.perimetr as perimetr
import modules.factoprial as factorial
import modules.test.test_all as te

print(f'Факториал 6 равен {factorial.func(6)}')

p1 = perimetr.perimetr([1,2,3])
print(p1)

p2 = perimetr.perimetr([1,2,3,4,5])
print(p2)

print(f'Факториал 5 равен {factorial.fact(5)}')

print(f'Факториал 12 равен {factorial.func(12)} = {factorial.fact(12)}')

print('Hello world!!!!!')