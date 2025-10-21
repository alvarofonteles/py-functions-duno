'''Funções #7 - Funções de ordem superior HOFs. (Linguagens Funcionais)'''

# %%
from functools import reduce
from itertools import groupby, takewhile


# %%
def soma_3(val: int):
    return val + 3


soma_3(2)
# 5

# %%
soma_3(soma_3(4))
# 10

# %%
soma_2 = lambda val: val + 2
soma_2(2)
# 2

# %%
soma_2(soma_2(2))
# 5
# chamou duas vezes 2+1=3 e 2+3 =5


# Twice
def reaplica(func: callable, val: any) -> any:
    '''Função que reaplica a função ao resultado da chamada.'''
    return func(
        func(val),
    )


reaplica(soma_2, 1)
# 5
# chamou duas vezes 2+1=3 e 2+3 =5


# %%
def seleciona(op: str) -> callable:
    '''Seleciona uma função, usando seu nome.'''
    ops = {
        'soma': lambda x, y: x + y,
        'sub': lambda x, y: x - y,
    }
    return ops[op]


seleciona('soma')(2, 3)
# 5

# %%
seleciona('sub')(5, 2)
# 3

# %%
palavras = [
    'amar',
    'doar',
    'servir',
    'retribuir',
    'crescer',
    'viver',
]

sorted(palavras)
# ['servir', 'retribuir', 'viver', 'amar', 'doar', 'crescer']

# %%
sorted(
    palavras,
    key=lambda string: string[1],
)
# ['servir', 'retribuir', 'viver', 'amar', 'doar', 'crescer']

# %%
list(
    map(
        lambda val: val * 2,
        palavras,
    ),
)
'''
['amaramar',
 'doardoar',
 'servirservir',
 'retribuirretribuir',
 'crescercrescer',
 'viverviver']
'''

# %%
list(
    map(
        lambda val: val * 2,
        [1, 2, 3, 5],
    ),
)
# [2, 4, 6, 10]

# %%

list(groupby(palavras))
'''
[('amar', <itertools._grouper at 0x2303119b010>),
 ('doar', <itertools._grouper at 0x2303119ad40>),
 ('servir', <itertools._grouper at 0x2303119ad10>),
 ('retribuir', <itertools._grouper at 0x23031199b70>),
 ('crescer', <itertools._grouper at 0x2303119b4f0>),
 ('viver', <itertools._grouper at 0x2303119b880>)]
'''

# %%
print(f'{len(palavras)} palavras')
list(groupby(palavras, key=lambda string: string[-2:]))
''''
[('ar', <itertools._grouper at 0x23031199390>),
 ('ir', <itertools._grouper at 0x23031199cc0>),
 ('er', <itertools._grouper at 0x230311980a0>)]
'''

# %%
list(filter(lambda string: string[-2:] == 'ir', palavras))
# ['servir', 'retribuir']

# %%
'''agrupa tudo e soma
reduce de soma similar o sum()
'''

reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
# 15

# %%
list(takewhile(lambda x: x <= 10, [2, 5, 9, 7, 10, 12, 15, 18]))
# [2, 5, 9, 7, 10]
