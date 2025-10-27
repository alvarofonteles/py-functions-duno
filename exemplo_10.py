'''
Minissérie Pythonica: Funções #10 - Funções aninhadas.

Funções dentro de Funções.
'''

# %%
from difflib import ndiff


# verboso
def arquivo_diferente(arq1: str, arq2: str):
    with open(arq1, encoding='utf-8') as arq_1, open(arq2, encoding='utf-8') as arq_2:
        contexto1 = arq_1.read().splitlines()  # ← keepends=False é padrão
        contexto2 = arq_2.read().splitlines()

    diferenca = ndiff(contexto1, contexto2)
    return '\n'.join(diferenca)


diff = arquivo_diferente('texto1.txt', 'texto2.txt')
print(diff)


# %%
# limpo e reaproveitamento de código (Funções aninhadas)
def arquivo_diferente2(arq1: str, arq2: str):
    def ler_arquivo(arq: str):
        with open(arq, encoding='utf-8') as aq:
            contexto = aq.read().splitlines()  # ← keepends=False é padrão
        return contexto

    contexto1 = ler_arquivo(arq1)
    contexto2 = ler_arquivo(arq2)

    diferenca = ndiff(contexto1, contexto2)
    return '\n'.join(diferenca)


diff = arquivo_diferente2('texto1.txt', 'texto2.txt')
print(diff)

# %%
'''
- Oi        # texto1.txt tinha 'Oi'
+ Olá       # texto2.txt mudou para 'Olá'
  meu       # Igual nos dois
  nome      # Igual nos dois  
- é         # texto1.txt tinha 'é'
- Alvaro    # texto1.txt tinha 'Alvaro'  
+ nao é     # texto2.txt mudou para 'nao é'
+ Eduardo   # texto2.txt adicionou 'Eduardo'
'''


# %%
# Calculadora com validação interna
def calculadora(operacao, a, b):
    def validar_numeros():
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError('Apenas números são permitidos!')

    def somar():
        return a + b

    def multiplicar():
        return a * b

    def dividir():
        if b == 0:
            raise ValueError('Divisão por zero!')
        return a / b

    # Execução
    validar_numeros()

    if operacao == 'somar':
        return somar()
    elif operacao == 'multiplicar':
        return multiplicar()
    elif operacao == 'dividir':
        return dividir()
    else:
        raise ValueError('Operação inválida!')


# Uso
print(calculadora('somar', 5, 3))  # 8
print(calculadora('dividir', 10, 2))  # 5.0


# %%
# Gerador de saudação personalizada
def criar_saudacao2(nome):
    def formatar_mensagem(mensagem):
        return f' {mensagem}, {nome}!'

    def manha():
        return formatar_mensagem('Bom dia')

    def tarde():
        return formatar_mensagem('Boa tarde')

    return {'manha': manha, 'tarde': tarde}


saudacao = criar_saudacao2('Álvaro')
print(saudacao['manha']())  # Bom dia, Álvaro!
print(saudacao['tarde']())  # Boa tarde, Álvaro!

# %%
'''Closure vs Classe.'''


# COM CLOSURE (seu exemplo)
def criar_saudacao3(nome):  # ← "Fábrica de funções"
    def manha():
        return f"Bom dia, {nome}!"  # ← Lembra do 'nome'!

    return {'manha': manha}


saudacoes = criar_saudacao3("Álvaro")  # ← Configura UMA vez
print(saudacoes['manha']())  # "Bom dia, Álvaro!" ← Usa MÚLTIPLAS vezes


# %%
# COM CLASSE (equivalente)
class Saudacao:
    def __init__(self, nome):  # ← Configura UMA vez
        self.nome = nome

    def manha(self):  # ← Usa MÚLTIPLAS vezes
        return f"Bom dia, {self.nome}!"


saudacoes = Saudacao("Álvaro")  # ← Instância
print(saudacoes.manha())  # "Bom dia, Álvaro!"


# %%
# Closure perfeito
def criar_contador():
    count = 0

    def incrementar():
        nonlocal count
        count += 1
        return count

    return incrementar  # ← Retorna UMA função


contador = criar_contador()
print(contador())  #  1
print(contador())  #  2


# %%
# Factory de funções (Closure)
def criar_logger(prefixo):  # ← Recebe parâmetro
    def log(mensagem):
        print(f"[{prefixo}] {mensagem}")

    return log  # ← Retorna função PERSONALIZADA


# Cria MÚLTIPLAS funções diferentes
logger_erro = criar_logger("ERRO")  # ← Função customizada
logger_info = criar_logger("INFO")  # ← Outra função customizada

logger_erro('Linha 235, esperava um [int]')
logger_info('Passei por aqui!')

# %%
'''
Ambos são Closures (funções que "lembram" do escopo externo)

Factory = Closure que personaliza funções via parâmetros

Factory é um tipo de Closure que cria funções customizadas!
'''
