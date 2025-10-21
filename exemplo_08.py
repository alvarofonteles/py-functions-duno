'''Funções #8 - Módulo operator.'''

# %%
from operator import add, sub, mul, itemgetter, itruediv
from functools import reduce

# %%
add(2, 3)
# 5

# %%
add(6, 10)
# 16

# %%
sub(6, 2)
# 4

# %%
sub(12, 3)
# 9

# %%
mul(5, 5)
# 25

# %%
mul(7, 3)
# 21

# %%
itruediv(16, 2)
# 8.0

# %%
reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
# 15
# %%
reduce(lambda x, y: x - y, [1, 2, 3, 4, 5])
# -13
# %%
reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])
# 120
# %%
reduce(lambda x, y: x / y, [1, 2, 3, 4, 5])
# 0.008333...


# Usando Operator - Mais limpo e menos verboso
# %%
reduce(add, [1, 2, 3, 4, 5])
# 15
# %%
reduce(sub, [1, 2, 3, 4, 5])
# -13
# %%
reduce(mul, [1, 2, 3, 4, 5])
# 120
# %%
reduce(itruediv, [1, 2, 3, 4, 5])
# 0.008333...


# %%
palavras = ['amar', 'doar', 'servir', 'retribuir']

sorted(palavras, key=lambda str: str[1])
# ['servir', 'retribuir', 'amar', 'doar']

# %%
sorted(palavras, key=itemgetter(1))
# ['servir', 'retribuir', 'amar', 'doar']
