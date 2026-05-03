# funcoes - 
def saudacao(nome):
    return f"Olá, {nome}!"

print(saudacao("Maria"))  # Chama a função e imprime o resultado

# Exemplo de função com parâmetros e retorno
def calcular_area_circulo(raio):
    import math
    return math.pi * raio**2

# Exemplo de função sem parâmetros
def exemplo_sem_parametros():
    print("Esta função não recebe parâmetros e não retorna nada.")
    
# Exemplo de função com parâmetros opcionais
def saudacao_personalizada(nome, saudacao="Olá"):
    return f"{saudacao}, {nome}!"

# Exemplo de função com parâmetros variáveis - permite passar um número variável de argumentos  (*args) - vem em tupla
def soma(*numeros):
    return sum(numeros)

print(soma(1, 2, 3, 4))  # Soma de vários números

# (**kwargs) - permite passar um número variável de argumentos nomeados (chave-valor) - vem em dicionário
def imprimir_info(**info):
    for chave, valor in info.items():
        print(f"{chave}: {valor}")
        
imprimir_info(nome="João", idade=30, cidade="São Paulo")  # Imprime as informações passadas como argumentos nomeados


# Exemplo de função com parâmetros nomeados - permite passar argumentos pelo nome
def criar_usuario(nome, idade, email):
    return {
        "nome": nome,
        "idade": idade,
        "email": email
    }

usuario = criar_usuario(nome="João", idade=30, email="joao@example.com")
print(usuario)


# Exemplo de função recursiva - funcao que chama a si mesma
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)
    
print(fatorial(5))  # Imprime o fatorial de 5 (120)


# Exemplo de função lambda (função anônima)
quadrado = lambda x: x ** 2

# Exemplo de função com docstring (documentação)
def multiplicar(a, b):
    """Retorna o produto de a e b."""
    return a * b


# Exemplo de função com tipo de retorno anotado - indica o tipo esperado do retorno
def dividir(a: float, b: float) -> float:
    """Retorna a divisão de a por b. Lança ValueError se b for zero."""
    if b == 0:
        raise ValueError("Divisor não pode ser zero.")
    return a / b

print(dividir(10, 2))  # Imprime a divisão de 10 por 2 (5.0)


# Exemplo de funcao com parametros por posição (/) - indica que os argumentos devem ser passados por posição, não por nome
def funcao_posicional(a, b, /, c):
    return a + b + c
print(funcao_posicional(1, 2, c=3))  # Chama a função com argumentos por posição e nomeado

# Exemplo de função com parâmetros por palavra-chave (*) - indica que os argumentos devem ser passados por nome, não por posição
def funcao_palavra_chave(*, a, b, c):
    return a + b + c
print(funcao_palavra_chave(a=1, b=2, c=3))  # Chama a função com argumentos nomeados

#existe a possibilidade de combinar os tipos de parâmetros (posição, palavra-chave, variáveis) em uma única função, seguindo a ordem: parâmetros posicionais, parâmetros por posição (/), parâmetros por palavra-chave (*), parâmetros variáveis (*args e **kwargs).


# Objetos de primeira classe: funções podem ser atribuídas a variáveis, passadas como argumentos para outras funções e retornadas por outras funções
def saudacao(nome):
    return f"Olá, {nome}!"
minha_saudacao = saudacao  # Atribui a função a uma variável
print(minha_saudacao("Maria"))  # Chama a função através da nova variável

# exemplo pratico
def soma(a, b):
    return a + b

def operacao(a, b, funcao):
    resultado = funcao(a, b)  # Chama a função passada como argumento
    return resultado

print(operacao(10, 5, soma))  # Passa a função soma como argumento para operacao (15)
