# %%

''' 
Obs.: Devido ao autopep8 a funcao lambda anonima [lambda param and lambda param1, param2] 
      se converteu em [def anomima(param) and def anomima2(param1, param2)] respectivamente
'''

anonima = lambda param: param + 2
anonima_plus =  lambda param1, param2: param1 + param2


param1 = anonima(3)
print(param1)

param2 = anonima_plus(7, 9)
print(param2)

# %%
def anomima(param): return param + 1  # um parametro na funcao anonima


soma = anomima(3)
print(soma)


def anomima2(param1, param2): return param1 + param2


soma2 = anomima2(7, 9)
print(soma2)


def soma_posicional(x, y):  # aceita qualquer posicao desde que seja posicionado
    return x + y


soma3 = soma_posicional(y=9, x=7)
print(soma3)


def soma_nomeados(x=5, y=4):  # como default, na falta de parametro assume se o valor nomeado
    return x + y


soma4 = soma_nomeados()
print(soma4)

soma4_1 = soma_nomeados(3, 9)
soma4_2 = soma_nomeados(y=9, x=3)
soma4_3 = soma_nomeados(9)
soma4_4 = soma_nomeados(x=3)
soma4_5 = soma_nomeados(y=9)

print(soma4_1)
print(soma4_2)
print(soma4_3)
print(soma4_4)
print(soma4_5)


# %%
def soma_explic_nomeados(*, x=5, y=4):
    print(f'x:{x}, y:{y}')
    return x + y


# soma5_1 = soma_explic_nomeados(1, x=3, y=8)  # nao aceita posicional
# print(soma5_1)
soma5_2 = soma_explic_nomeados(x=3, y=8)
print(soma5_2)
soma5_3 = soma_explic_nomeados(y=8)
print(soma5_3)
soma5_4 = soma_explic_nomeados(x=3)
print(soma5_4)

# %%


def soma_explic_nomeados2(x=5, *,  y=4):
    print(f'x:{x}, y:{y}')
    return x + y


# aceita posicional final, pois ja tem a frent args
soma6_1 = soma_explic_nomeados2(1, y=8)
print(soma6_1)
soma6_2 = soma_explic_nomeados2(8)
print(soma6_2)
# nao aceita nominal, pelo menos um ultimo y=8
# soma6_2_1 = soma_explic_nomeados2(3, 8)
# print(soma6_2_1)
soma6_3 = soma_explic_nomeados2(x=3, y=8)
print(soma6_3)
soma6_4 = soma_explic_nomeados2(y=8)
print(soma6_4)
soma6_5 = soma_explic_nomeados2(x=3)
print(soma6_5)


# posso deixar default [x=3, y=8] se quiser
def soma_explic_posicional(x, y, /):
    print(f'x:{x}, y:{y}')
    return x + y


soma7_1 = soma_explic_posicional(3, 8)
print(soma7_1)
# soma7_2 = soma_explic_posicional() # precisaria de default
# print(soma7_2)
# soma7_3 = soma_explic_posicional(x=3, y=1)  # somente posicional
# print(soma7_3)


''' [*] nomeados e [/] posicional '''


def soma_tudo_mix(x, y, /, z, *, w):
    print(f'x:{x}, y:{y}, x:{z}, y:{w}')
    return sum((x, y, z, w))


soma8_1 = soma_tudo_mix(3, 8, 6, w=5)  # [z] aceita posicional
print(soma8_1)
soma8_2 = soma_tudo_mix(3, 8, z=6, w=5)  # [z] aceita como nomeado
print(soma8_2)
