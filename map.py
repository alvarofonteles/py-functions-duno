# %%
'''Sobre Map.
map(função, iterável)
    ↑        ↑
    │        └── Lista, tupla, etc
    └─────────── Função para aplicar em CADA elemento
'''

# %%
'''Comparação: Map vs List Comprehension'''
# Map()
resultado_map = list(map(lambda x: x * 2, [1, 2, 3]))
resultado_map
# [2, 4, 6]

# %%
# List Comprehension:
resultado_listcomp = [x * 2 for x in [1, 2, 3]]
resultado_listcomp
# [2, 4, 6]

# %%
palavras = ['amar', 'doar', 'servir', 'retribuir', 'crescer', 'viver']

# Converter para maiúsculas
maiusculas = list(map(str.upper, palavras))
maiusculas
# ['AMAR', 'DOAR', 'SERVIR', 'RETRIBUIR', 'CRESCER', 'VIVER']

# %%
# Calcular tamanhos
tamanhos = list(map(len, palavras))
tamanhos
# [4, 4, 6, 9, 7, 5]

# %%
# Somar elementos de duas listas
soma_listas = list(map(lambda x, y: x + y, [1, 2, 3], [4, 5, 6]))
soma_listas
# [5, 7, 9]

# %%
'''Dobrar números'''
numeros = [1, 2, 3, 4, 5]
dobro = list(map(lambda x: x * 2, numeros))
dobro
# [2, 4, 6, 8, 10]

# %%
'''Primeira letra maiúscula'''
nomes = ['eduardo', 'maria', 'joão']
capitalizado = list(map(str.capitalize, nomes))
capitalizado
# ['Eduardo', 'Maria', 'João']

# %%
'''MAP COM DICIONÁRIOS - Transformar valores'''
pessoas = {'eduardo': 25, 'maria': 17, 'joão': 30}

# Dobrar idades
idades_dobradas = dict(map(lambda item: (item[0], item[1] * 2), pessoas.items()))
idades_dobradas
# {'eduardo': 50, 'maria': 34, 'joão': 60}

# %%
'''MAP COM DICIONÁRIOS - Transformar chaves'''
# Capitalizar nomes
nomes_capitalizados = dict(
    map(lambda item: (item[0].capitalize(), item[1]), pessoas.items())
)
nomes_capitalizados
# {'Eduardo': 25, 'Maria': 17, 'João': 30}

# %%
'''MAP COM DICIONÁRIOS - Ambos (chave e valor)'''
# Nome em maiúsculo e idade + 10
transformados = dict(map(lambda item: (item[0].upper(), item[1] + 10), pessoas.items()))
transformados
# {'ALVARO': 35, 'MARIA': 27, 'JOÃO': 40}

# %%
'''LIST COMPREHENSION COM DICIONÁRIOS'''
# Equivalente aos exemplos acima

# Dobrar idades
idades_dobradas_lc = {k: v * 2 for k, v in pessoas.items()}
idades_dobradas_lc
# {'eduardo': 50, 'maria': 34, 'joão': 60}

# %%
# Capitalizar nomes
nomes_capitalizados_lc = {k.capitalize(): v for k, v in pessoas.items()}
nomes_capitalizados_lc
# {'Eduardo': 25, 'Maria': 17, 'João': 30}

# %%
# Transformar ambos
transformados_lc = {k.upper(): v + 10 for k, v in pessoas.items()}
transformados_lc
# {'ALVARO': 35, 'MARIA': 27, 'JOÃO': 40}

# %%
'''MAP EM LISTA DE DICIONÁRIOS'''
usuarios = [
    {'nome': 'eduardo', 'idade': 25},
    {'nome': 'maria', 'idade': 17},
    {'nome': 'joão', 'idade': 30},
]

# Capitalizar todos os nomes
nomes_caps = list(
    map(lambda user: {**user, 'nome': user['nome'].capitalize()}, usuarios)
)
nomes_caps
# [{'nome': 'Eduardo', 'idade': 25}, {'nome': 'Maria', 'idade': 17}, {'nome': 'João', 'idade': 30}]

# %%
# List Comprehension equivalente
nomes_caps_lc = [{**user, 'nome': user['nome'].capitalize()} for user in usuarios]
nomes_caps_lc
# [{'nome': 'Eduardo', 'idade': 25}, {'nome': 'Maria', 'idade': 17}, {'nome': 'João', 'idade': 30}]

# %%
'''MAP com múltiplos iteráveis em dicionários'''
chaves = ['nome', 'idade', 'cidade']
valores = ['Eduardo', 25, 'Fortaleza']

# Criar dicionário a partir de listas
dicionario = dict(map(lambda k, v: (k, v), chaves, valores))
dicionario
# {'nome': 'Eduardo', 'idade': 25, 'cidade': 'Fortaleza'}
