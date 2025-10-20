'''Documentando funções com docstrings.'''


# %%
def soma(x: int, y: int) -> int:
    # Atalho: ctrl + shift + 2
    # PEP - 257
    # DOCSTRING ['''''']
    # TYPE HINTS [x: int]
    '''_summary_

    Args:
        x (int): _description_
        y (int): _description_

    Returns:
        int: _description_
    '''
    return x + y


# %%
def cadastro_usuario(nome: str, idade: int, gostos: list[str]) -> dict:
    '''
    Cria um dicionário com dados do usuário.

    Args:
        nome: Nome completo do usuário
        idade: Idade em anos
        gostos: Lista de hobbies/interesses

    Returns:
        Dict com chaves 'nome', 'idade' e 'gostos'

    Example:
        >>> cadastro_usuario('João', 25, ['ler', 'correr'])
        {'nome': 'João', 'idade': 25, 'gostos': ['ler', 'correr']}
    '''
    return {'nome': nome, 'idade': idade, 'gostos': gostos}


# %%
print(cadastro_usuario.__doc__)  # Mostra a documentação completa
# %%
print(cadastro_usuario.__annotations__)  # Mostra a anotação completa
# %%
cadastro_usuario('João', 25, ['ler', 'correr'])
