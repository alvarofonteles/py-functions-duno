
'''Des|empacotamento de argumentos'''

# %%


def empacotamento(*args):  # Pode se mandar varios parametros, não nomeados
    print(f'empacotamento [args em tupla] {args}')
    print(f'type {type(args)}')
    return sum(args)


retorno = empacotamento(1, 2, 3, 4, 5)
print(f'soma {retorno}')
retorno2 = empacotamento(1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
print(f'soma2 {retorno2}')


def empacotamento(x, y, *args):  # Pode se mandar varios parametros, não nomeados
    print(f'x: {x} e y: {y} - com pack [args em tupla] {args}')
    print(f'type {type(args)}')
    return x, y, sum(args)


retorno = empacotamento(5, 6, 1, 2, 3, 4, 5)
print(f'soma {retorno}')
retorno2 = empacotamento(7, 8, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
print(f'soma2 {retorno2}')

# %%


def empacotamento2(*args, **kwargs):  # Pode se mandar varios parametros, não nomeados
    print(f'args {args} e kwargs {kwargs}')
    print(f'type {type(args)}, {type(kwargs)}')
    return args, kwargs


retorno3 = empacotamento2(1, 2, 3, 4, 5)
print(f'soma {retorno3}')
retorno4 = empacotamento2(1, 2, 3, 4, 5, a=5, b=6)
print(f'soma2 {retorno4}')

# %%


def desempacotamento(a, b, c, d, e):
    return a, b, c, d, e


lista = [1, 2, 3, 4, 5]
retorno5 = desempacotamento(*lista)
print(retorno5)

# %%


def desempacotamento_min(a, b, c, d, e):
    return min((a, b, c, d, e))


lista2 = [-1, 1, 2, 3, 4]
retorno6 = desempacotamento_min(*lista2)
print(retorno6)


# %%
def desempacotamento_min2(a, b, c, d, e, *args):
    return min((a, b, c, d, e, *args))


lista3 = [-1, 1, 2, 3, 4, 5, -10, 7, -11]
retorno7 = desempacotamento_min2(*lista3)
print(retorno7)

# %%


def desempacotamento_max(a=0, b=0, c=0, d=0, e=0, **kwargs):
    return max((a, b, c, d, e, *kwargs.values()))


dicionario = {'a': -1, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': -11}
retorno8 = desempacotamento_max(**dicionario)
print(retorno8)

# %%


def desempacotamento_max2(**kwargs):
    return max(*kwargs.values())


dicionario2 = {'a': -1, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': -11}
retorno9 = desempacotamento_max2(**dicionario2)
print(retorno9)

# %%
lista4 = [1, 2, 3]
dicionario3 = {'d': 4, 'e': 5}


def desempacotamento_mix(a, b, c, d=0, e=0):
    return a, b, c, d, e

retorno10 = desempacotamento_mix(*lista4, **dicionario3)
print(retorno10)