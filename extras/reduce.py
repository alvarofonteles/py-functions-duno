# %%
'''Sobre Reduce
reduce(função, iterável, valor_inicial)
     ↑         ↑           ↑
     │         │           └── Opcional: valor inicial
     │         └── Lista, tupla, etc
     └──────────── Função que acumula resultado
'''

# %%
from functools import reduce

'''Somar todos os números'''
numeros = [1, 2, 3, 4, 5]
soma_total = reduce(lambda acc, x: acc + x, numeros)
soma_total
# 15

# %%
'''Concatenar todas as palavras'''
palavras = ['amar', 'doar', 'servir', 'retribuir', 'crescer', 'viver']
frase = reduce(lambda acc, p: acc + ' ' + p, palavras)
frase
# 'amar doar servir retribuir crescer viver'

# %%
'''Encontrar o maior número'''
maior = reduce(lambda acc, x: x if x > acc else acc, numeros)
maior
# 5

# %%
'''Multiplicar todos os números'''
produto = reduce(lambda acc, x: acc * x, [1, 2, 3, 4])
produto
# 24

# %%
'''Com valor inicial'''
soma_com_inicial = reduce(lambda acc, x: acc + x, [1, 2, 3], 10)
soma_com_inicial
# 16 (10 + 1 + 2 + 3)

# %%
'''REDUCE COM DICIONÁRIOS - Somar todos os valores'''
pessoas = {'eduardo': 25, 'maria': 17, 'joão': 30, 'ana': 22}

# Somar todas as idades
soma_idades = reduce(lambda acc, item: acc + item[1], pessoas.items(), 0)
soma_idades
# 94 (25 + 17 + 30 + 22)

# %%
'''REDUCE COM DICIONÁRIOS - Concatenar todas as chaves'''
todas_chaves = reduce(lambda acc, item: acc + ', ' + item[0], pessoas.items(), 'Nomes:')
todas_chaves
# 'Nomes:, eduardo, maria, joão, ana'

# %%
'''REDUCE COM DICIONÁRIOS - Encontrar pessoa mais velha'''
mais_velha = reduce(
    lambda acc, item: item if item[1] > acc[1] else acc, pessoas.items()
)
mais_velha
# ('joão', 30)

# %%
'''REDUCE COM DICIONÁRIOS - Criar dicionário agrupado'''


# Agrupar por faixa etária: <18, 18-25, >25
def agrupar_idades(acc, item):
    nome, idade = item
    if idade < 18:
        acc['menores'].append(nome)
    elif idade <= 25:
        acc['jovens'].append(nome)
    else:
        acc['adultos'].append(nome)
    return acc


grupos = reduce(
    agrupar_idades, pessoas.items(), {'menores': [], 'jovens': [], 'adultos': []}
)
grupos
# {'menores': ['maria'], 'jovens': ['eduardo', 'ana'], 'adultos': ['joão']}

# %%
'''REDUCE COM LISTA DE DICIONÁRIOS'''
usuarios = [
    {'nome': 'Eduardo', 'idade': 25, 'salario': 3000},
    {'nome': 'Maria', 'idade': 17, 'salario': 1500},
    {'nome': 'João', 'idade': 30, 'salario': 4000},
    {'nome': 'Ana', 'idade': 22, 'salario': 2500},
]

# Somar todos os salários
total_salarios = reduce(lambda acc, user: acc + user['salario'], usuarios, 0)
total_salarios
# 11000

# %%
'''REDUCE COM LISTA DE DICIONÁRIOS - Múltiplas agregações'''


def agregar_dados(acc, user):
    acc['total_idade'] += user['idade']
    acc['total_salario'] += user['salario']
    acc['maior_salario'] = max(acc['maior_salario'], user['salario'])
    acc['pessoas'].append(user['nome'])
    return acc


estatisticas = reduce(
    agregar_dados,
    usuarios,
    {'total_idade': 0, 'total_salario': 0, 'maior_salario': 0, 'pessoas': []},
)
estatisticas
# {'total_idade': 94, 'total_salario': 11000, 'maior_salario': 4000, 'pessoas': ['Eduardo', 'Maria', 'João', 'Ana']}

# %%
'''REDUCE - Juntar múltiplos dicionários'''
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5, 'f': 6}

# Juntar todos os dicionários
dicts = [dict1, dict2, dict3]
juntar_todos = reduce(lambda acc, d: {**acc, **d}, dicts, {})
juntar_todos
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

# %%
'''REDUCE - Contar frequência de palavras'''
texto = ['python', 'é', 'legal', 'python', 'é', 'poderoso', 'python']
frequencia = reduce(
    lambda acc, palavra: {**acc, palavra: acc.get(palavra, 0) + 1}, texto, {}
)
frequencia
# {'python': 3, 'é': 2, 'legal': 1, 'poderoso': 1}
