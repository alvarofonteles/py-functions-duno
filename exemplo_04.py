'''Anotações de tipos de argumentos
Pesquisar
 - PEP-484
 - mypy
 - monkeytype
'''

# %%
from numbers import Number
from typing import Union, List, Any, Dict, Sequence, Text

# %%


def soma(x: int, y: int) -> int:
    return x + y


soma('a', 'b')  # 'ab',


# %% Podem ser somadas listas, strings, numeros
hasattr('', '__add__')

# %%
hasattr(2, '__add__')
# %%
hasattr([], '__add__')  # True


# %%
def soma(x: [int, float, complex], y: [int, float, complex]) -> [int, float, complex]:
    return x + y


soma('a', 'b')


# %%
def soma(x: Number, y: Number) -> Number:
    return x + y


soma(1, 1)

# %%
isinstance(1.0, Number)
# %%
isinstance(1.0 + 1j, Number)  # True
# %%
issubclass(int, Number)  # True
# %%
issubclass(float, Number)  # True
# %%
issubclass(complex, Number)  # True
# %%


def soma(
    x: Union[Number, str, list], y: Union[Number, str, list]
) -> Union[Number, str, list]:
    return x + y


soma(1, 1)
# %%

somavel = Union[Number, str, list]


def soma(x: somavel, y: somavel) -> somavel:
    return x + y


soma('a', 'b')


# %%
def identidade(val: Any) -> Any:
    return val


identidade(2)


# %%
def meu_sum(l):
    return sum(l)


meu_sum([1, 2, 3])
# %%
meu_sum((1, 2, 3))
# %%
meu_sum({1, 2, 3})
# %%
meu_sum(range(1, 2, 3))


# %%
def meu_sum(l: List[Number]) -> Number:
    return sum(l)


meu_sum([1, 2, 3])


# %%
def cadastro_usuario(
    nome: str,
    idade: int,
    gostos: List[str],
) -> dict:
    return {
        'nome': nome,
        'idade': idade,
        'gostos': gostos,
    }


cadastro_usuario('Álvaro', 42, ['Estudar', 'Ajudar'])


# %%
''' Agora tudo bem definido '''


def cadastro_usuario2(
    nome: str,
    idade: int,
    gostos: List[str],
) -> Dict[str, Union[str, int, List[str]]]:
    return {
        'nome': nome,
        'idade': idade,
        'gostos': gostos,
    }


cadastro_usuario2('Álvaro', 42, ['Estudar', 'Ajudar'])


# %%
type('2.5')
# %%
type(b'2.5')  # bytes


# %%¨
def meu_min(seq: Sequence[Number]) -> Number:
    """Encontra o menor valor em uma sequência de números."""
    return min(seq)


# ✅ Testes
meu_min([1, 2, 3])  # Lista
# %%
meu_min((1.5, 2.5, 3.5))  # Tupla
# %%
meu_min({5, 3, 8})  # Set


# %%
def converte_texto_para_float(valor: Text) -> float:
    """Converte texto para valor em reais (float)."""
    # Remove R$, espaços e converte vírgula para ponto
    valor_limpo = valor.replace('R$', '').replace(' ', '').replace(',', '.')
    return float(valor_limpo)


# ✅ Testes
converte_texto_para_float("R$ 2,50")  # 2.5
# %%
converte_texto_para_float("10,99")  # 10.99
# %%
converte_texto_para_float("  5.75  ")  # 5.75
