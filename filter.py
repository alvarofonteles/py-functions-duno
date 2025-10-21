# %%
'''Sobre Filter
filter(função, iterável)
     ↑         ↑
     │         └── Lista, tupla, etc
     └──────────── Função que retorna True/False para CADA elemento
'''

# %%
'''Comparação: Filter vs List Comprehension'''
# Filter():
resultado_filter = list(filter(lambda x: x > 5, [1, 8, 3, 10, 2]))
resultado_filter
# [8, 10]

# %%
# List Comprehension:
resultado_listcomp = [x for x in [1, 8, 3, 10, 2] if x > 5]
resultado_listcomp
# [8, 10]

# %%
'''Filtrar números pares'''
numeros = list(range(1, 11))
pares = list(filter(lambda x: x % 2 == 0, numeros))
pares
# [2, 4, 6, 8, 10]

# %%
'''Filtrar palavras que começam com vogal'''
palavras = ['amar', 'doar', 'servir', 'retribuir', 'crescer', 'viver']
vogais = list(filter(lambda p: p[0] in 'aeiou', palavras))
vogais
# ['amar']

# %%
'''Filtrar palavras longas'''


def eh_longo(palavra: str) -> bool:
    return len(palavra) > 5


longas = list(filter(eh_longo, palavras))
longas
# ['servir', 'retribuir', 'crescer']

# %%
'''FILTER COM DICIONÁRIOS - Chaves'''
pessoas = {'eduardo': 25, 'maria': 17, 'joão': 30, 'ana': 16}

# Filtrar chaves que começam com 'a'
chaves_com_a = dict(filter(lambda item: item[0].startswith('a'), pessoas.items()))
chaves_com_a
# {'eduardo': 25, 'ana': 16}

# %%
'''FILTER COM DICIONÁRIOS - Valores'''
# Filtrar maiores de idade
maiores_idade = dict(filter(lambda item: item[1] >= 18, pessoas.items()))
maiores_idade
# {'eduardo': 25, 'joão': 30}

# %%
'''FILTER COM DICIONÁRIOS - Condições complexas'''
# Filtrar pessoas entre 20 e 30 anos que o nome tem mais de 4 letras
filtro_complexo = dict(
    filter(lambda item: 20 <= item[1] <= 30 and len(item[0]) > 4, pessoas.items())
)
filtro_complexo
# {'eduardo': 25}

# %%
'''LIST COMPREHENSION COM DICIONÁRIOS'''
# Equivalente aos exemplos acima com list comprehension

# Chaves que começam com 'a'
chaves_a = {k: v for k, v in pessoas.items() if k.startswith('a')}
chaves_a
# {'eduardo': 25, 'ana': 16}

# %%
# Maiores de idade
maiores = {k: v for k, v in pessoas.items() if v >= 18}
maiores
# {'eduardo': 25, 'joão': 30}

# %%
# Condição complexa
complexo = {k: v for k, v in pessoas.items() if 20 <= v <= 30 and len(k) > 4}
complexo
# {'eduardo': 25}

# %%
'''FILTER EM LISTA DE DICIONÁRIOS'''
usuarios = [
    {'nome': 'Eduardo', 'idade': 25, 'cidade': 'Fortaleza'},
    {'nome': 'Maria', 'idade': 17, 'cidade': 'São Paulo'},
    {'nome': 'João', 'idade': 30, 'cidade': 'Rio de Janeiro'},
    {'nome': 'Ana', 'idade': 16, 'cidade': 'Fortaleza'},
]

# Filtrar maiores de idade de Fortaleza
fortaleza_maiores = list(
    filter(lambda user: user['idade'] >= 18 and user['cidade'] == 'Fortaleza', usuarios)
)
fortaleza_maiores
# [{'nome': 'Eduardo', 'idade': 25, 'cidade': 'Fortaleza'}]

# %%
# List Comprehension equivalente
fortaleza_maiores_lc = [
    user for user in usuarios if user['idade'] >= 18 and user['cidade'] == 'Fortaleza'
]
fortaleza_maiores_lc
# [{'nome': 'Eduardo', 'idade': 25, 'cidade': 'Fortaleza'}]
