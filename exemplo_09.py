'''Funções #9 - Funções parciais (functools).'''

# %%
from operator import add, mul
from functools import reduce, partial


def soma_2(x):
    return x + 2


print(soma_2(2))  # 4

# %%
soma_2 = lambda x: x + 2
print(soma_2(2))  # 4

# %%
soma_2 = add(2, 2)
print(soma_2)  # 4


# %%
def soma_2_1(x):
    return add(x, 2)


print(soma_2_1(2))  # 4

# %%
soma_2_1 = lambda x: add(x, 2)
print(soma_2_1(2))  # 4


# %%
def mul_2(x):
    return mul(x, 2)


print(mul_2(3))  # 6

# %%
mul_2_1 = lambda x: mul(x, 2)
print(mul_2_1(3))  # 6

# %%
part_add = partial(add, 2)
print(part_add(2))  # 4

# %%
part_mul = partial(mul, 2)
print(part_mul(3))  # 6

# %%
red_add_lamb = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
print(red_add_lamb)  # 15

# %%
red_mul_lamb = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])
print(red_mul_lamb)  # 120


# %%
red_add = reduce(lambda x, y: add(x, y), [1, 2, 3, 4, 5])
print(red_add)  # 15

# %%
red_mul = reduce(lambda x, y: mul(x, y), [1, 2, 3, 4, 5])
print(red_mul)  # 120


# %%
red_add = reduce(add, [1, 2, 3, 4, 5])
print(red_add)  # 15

red_add = reduce(add, [6, 7, 8])
print(red_add)  # 21

# %%
red_mul = reduce(mul, [1, 2, 3, 4, 5])
print(red_mul)  # 120

red_mul = reduce(mul, [6, 7, 8])
print(red_mul)  # 336

# %%
lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8]

part_red_mul = partial(reduce, mul)  # reutiliza a funcao varias vezes
print(part_red_mul(lista1))  # 120
print(part_red_mul(lista2))  # 336

# %%
lista3 = [1, 2, 3, 4, 5]
part_mul = partial(mul, 2)
print(part_mul(3))  # 6

part_mul_all = partial(map, part_mul)  # ← função parcial
resultado = part_mul_all(lista3)  # ← executa map(part_mul, lista1)
print(list(resultado))  # ← converte para lista [2, 4, 6, 8, 10]
