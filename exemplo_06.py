'''
Funções #6 - Funções como objetos de primeira classe.
(É uma função dentro de uma variável: list, dict, etc)
Programação funcional.
'''

# %%
from numbers import Number

# %%
'''Demonstra funções atribuídas a variáveis.'''
func = lambda: 'resultado'
func
# <function __main__.<lambda>()>
func()
# 'resultado'

# %%
'''Demonstra funções atribuídas a funções Anonimas, com dicionários.'''
calc = {
    'soma': lambda x, y: x + y,
    'sub': lambda x, y: x - y,
    'mult': lambda x, y: x * y,
    'div': lambda x, y: x / y,
}

calc['soma'](3, 7)
# 10

# %%
'''Demonstra funções atribuídas a funções anônimas, com dicionários.'''
calc_anonino: dict[str, callable] = {
    'soma': lambda x, y: x + y,
    'sub': lambda x, y: x - y,
    'mult': lambda x, y: x * y,
    'div': lambda x, y: x / y,
}

calc_anonino['soma'](3, 7)
# 10

# %%
'''Demonstra funções atribuídas a funções nomeadas, com dicionários.'''


def soma(x: Number, y: Number) -> Number:
    return x + y


def sub(x: Number, y: Number) -> Number:
    return x - y


def mult(x: Number, y: Number) -> Number:
    return x * y


def div(x: Number, y: Number) -> Number:
    return x / y


# callable minúsculo (built-in) + tipos built-in
calc_nomeado: dict[str, callable] = {
    'soma': soma,
    'sub': sub,
    'mult': mult,
    'div': div,
}

calc_nomeado['mult'](6, 8)
# 48

# %%
calc_nomeado
'''
{'soma': <function __main__.soma(x: numbers.Number, y: numbers.Number) -> numbers.Number>,
 'sub': <function __main__.sub(x: numbers.Number, y: numbers.Number) -> numbers.Number>,
 'mult': <function __main__.mult(x: numbers.Number, y: numbers.Number) -> numbers.Number>,
 'div': <function __main__.div(x: numbers.Number, y: numbers.Number) -> numbers.Number>}
 '''

# %%
calc_nomeado['soma']
'''<function __main__.soma(x: numbers.Number, y: numbers.Number) -> numbers.Number>'''

# %%
'''Demonstra funções atribuídas a funções anonimas, com listas.'''

soma2: list[callable] = [
    lambda x: x + 1,
    lambda x: x + 2,
    lambda x: x + 3,
]

soma2[0](3)
# 4

# %%
soma2[1](4)
# 6

# %%
soma2[1](7)
# 9

# %%
'''Demonstra funções atribuídas a funções nomeadas, com listas.'''


def soma3(x: Number) -> Number:
    return x + 1


def sub3(x: Number) -> Number:
    return x - 1


def mult3(x: Number) -> Number:
    return x * 1


def div3(x: Number) -> Number:
    return x / 1


soma3(4)
# 5
# %%
# dentro de uma lista temporária com 1 função
[soma3][0](4)
# 5

# %%
# dentro de uma tupla temporária com 1 função
(soma3,)[0](10)  # <-- me explica
# 11

# %%
# Lista permanente com várias funções
operacao: list[callable] = [
    soma3,
    sub3,
    mult3,
    div3,
]
operacao[0](2)
# 3

# %%
'''Extra 1.'''

# Aplicando todas as funções a um número
numero = 5
resultados = [func(numero) for func in soma2]
resultados
# [6, 7, 8]

# %%
'''Extra 2.'''

operacoes: list[callable] = [soma, sub, mult, div]

# Testando todas as operações
resultados = [op(10, 5) for op in operacoes]
# resultados: [15, 5, 50, 2.0]

# Acessando por índice
operacoes[0](10, 5)  # 15 (soma)
operacoes[1](10, 5)  # 5 (subtração)

# %%
'''
Exemplo de uso:
>>> resultados = [op(10, 5) for op in operacoes]
>>> print(resultados)
[15, 5, 50, 2.0]

Ou em células Jupyter:
[op(10, 5) for op in operacoes]  # Resultado: [15, 5, 50, 2.0]
'''
