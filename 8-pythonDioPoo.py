# POO - Programação Orientada a Objetos
# - Classes: moldes para criar objetos, definem atributos e métodos
# - Objetos: instâncias de classes, possuem estado (atributos) e comportamento (métodos)
# - Encapsulamento: esconder detalhes internos, expor apenas o necessário
# - Herança: criar classes que herdam atributos e métodos de outras classes
# - Polimorfismo: objetos de diferentes classes podem ser tratados de forma uniforme se tiverem métodos com a mesma assinatura

# Exemplo de classe simples
# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome  # Atributo de instância
#         self.idade = idade

#     def apresentar(self):
#         return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."
    
# # Criando objetos (instâncias da classe)
# pessoa1 = Pessoa("Maria", 28)
# pessoa2 = Pessoa("João", 35)
# print(pessoa1.apresentar())  # Chama o método apresentar do objeto pessoa1
# print(pessoa2.apresentar())  # Chama o método apresentar do objeto pessoa2

# class Carro:
#     def __init__(self, marca, ano, modelo):
#         self.marca = marca
#         self.ano = ano
#         self.modelo = modelo
        
#     def descricao(self):
#         return f"{self.marca} {self.modelo} ({self.ano})"

# carro1 = Carro("Toyota", 2025, "Corolla")
# print(carro1.descricao())  # Imprime a descrição do carro1


# # Encapulamento: usando métodos para acessar atributos privados
# # Atributos privados são indicados por convenção com __ (dunder), mas ainda podem ser acessados diretamente (não é uma proteção real, apenas uma convenção)
# class ContaBancaria:
#     def __init__(self, titular, saldo_inicial=0):
#         self.titular = titular
#         self.__saldo = saldo_inicial  # Atributo privado (convenção com __)

#     def depositar(self, valor):
#         if valor > 0:
#             self.__saldo += valor
#             return f"Depósito de R${valor:.2f} realizado. Saldo atual: R${self.__saldo:.2f}"
#         else:
#             return "Valor de depósito deve ser positivo."

#     def sacar(self, valor):
#         if valor > self.__saldo:
#             return "Saldo insuficiente para saque."
#         elif valor <= 0:
#             return "Valor de saque deve ser positivo."
#         else:
#             self.__saldo -= valor
#             return f"Saque de R${valor:.2f} realizado. Saldo atual: R${self.__saldo:.2f}"

#     def consultar_saldo(self):
#         return f"Saldo atual: R${self.__saldo:.2f}"
    
# conta = ContaBancaria("João", 1000)
# print(conta.consultar_saldo())  # Consulta o saldo inicial
# print(conta.depositar(500))  # Realiza um depósito
# print(conta.sacar(200))  # Realiza um saque


# # Herança: criando uma classe que herda de outra
# # Sintaxe: class que herdara(Classe que sera herdada):
# # super() é usado para chamar o construtor da classe base e acessar seus métodos 
# class Funcionario(Pessoa):
#     def __init__(self, nome, idade, cargo):
#         super().__init__(nome, idade)  # Chama o construtor da classe base (Pessoa)
#         self.cargo = cargo

#     def apresentar(self):
#         return f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e sou {self.cargo}."
    
# funcionario1 = Funcionario("Ana", 30, "Engenheira")
# print(funcionario1.apresentar())  # Chama o método apresentar do objeto funcionario1


#  -----------------------------------
# # Polimorfismo: objetos de diferentes classes podem ser tratados de forma uniforme se tiverem métodos com a mesma assinatura
# class Animal:
#     def falar(self):
#         pass  # Método abstrato (sem implementação)
# class Cachorro(Animal):
#     def falar(self):
#         return "Au au!"
# class Gato(Animal, Cachorro):  # Gato herda de Animal e Cachorro
#     def falar(self):
#         return "Miau!"
    
# animais = [Cachorro(), Gato()]
# for animal in animais:
#     print(animal.falar())  # Chama o método falar de cada animal, mesmo sendo de classes diferentes
    

# abstração - ignorar o irrelevante e deixar apenas o principal, se concentrar apenas nas características essenciais de um objeto, sem se preocupar com detalhes de implementação
# metodo abstrato: método declarado em uma classe base que deve ser implementado por classes derivadas, serve como um contrato para garantir que as subclasses implementem certos métodos
# precisa do abc (Abstract Base Class) para criar métodos abstratos em Python, usando o módulo abc e decoradores @abstractmethod
# from abc import ABC, abstractmethod
# class Forma(ABC):
#     @abstractmethod
#     def area(self):
#         pass  # Método abstrato, sem implementação
# class Retangulo(Forma):
#     def __init__(self, largura, altura):
#         self.largura = largura
#         self.altura = altura
#     def area(self):
#         return self.largura * self.altura
# class Circulo(Forma):
#     def __init__(self, raio):
#         self.raio = raio
#     def area(self):
#         return 3.14 * (self.raio ** 2)

# retangulo = Retangulo(5, 3)
# circulo = Circulo(4)
# print(f"Área do retângulo: {retangulo.area()}")  # Chama o método area do retângulo
# print(f"Área do círculo: {circulo.area()}")  # Chama o método


# ENCAPSULAMENTO 
# convencao eh usar _ para indicar que um atributo ou método é protegido (não deve ser acessado diretamente fora da classe ou subclasses) e __ para indicar que é privado (não deve ser acessado diretamente de forma alguma, mesmo dentro de subclasses)
# existe a forma de usar __ para criar atributos privados, mas eles ainda podem ser acessados usando o nome mangling (nome da classe + nome do atributo), mas isso é desencorajado e deve ser evitado, pois quebra o encapsulamento e a intenção de privacidade do atributo
# exemplo de classe com encapsulamento usando atributos privados
class Conta:   
    def __init__(self,nro_agencia, saldo=0):
        self.__saldo = saldo  # Atributo privado
        self.nro_agencia = nro_agencia  # Atributo público
        
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            return f"Depósito de R${valor:.2f} realizado. Saldo atual: R${self.__saldo:.2f}"
        else:
            return "Valor de depósito deve ser positivo."
    
    def sacar(self, valor):
        if valor > self.__saldo:
            return f"Valor de {valor:.2f} excede o saldo disponível de R${self.__saldo:.2f}."
        else:
            self.__saldo -= valor
            return f"Saque de R${valor:.2f} realizado. Saldo atual: R${self.__saldo:.2f}"
        
    def __str__(self):
        return f"Conta Agência: {self.nro_agencia}, Saldo: R${self.__saldo:.2f}"

conta = Conta("0001", 100)
print(conta.depositar(50))  # Depósito de R$50.00 realizado. Saldo atual: R$150.00
print(conta.sacar(30))  # Saque de R$30.00 realizado. Saldo atual: R$120.00
print(conta.sacar(200))  # Valor de R$200.00 excede o saldo disponível de R$120.00.
print(conta)  # Conta Agência: 0001, Saldo: R$120.00

# Properties: permitem criar métodos que podem ser acessados como atributos, usando o decorador @property para criar um método getter e @nome_do_metodo.setter para criar um setter
# class Produto:
#     def __init__(self, nome, preco):
#         self.nome = nome
#         self.__preco = preco  # Atributo privado

#     @property # método para acessar o valor do atributo preço, usando o decorador @property
#     def preco(self):
#         return self.__preco
    
#     @preco.setter # método para definir o valor do atributo preço, usando o decorador @nome_do_metodo.setter
#     def preco(self, valor):
#         if valor < 0:
#             raise ValueError("O preço não pode ser negativo.")
#         self.__preco = valor
        
#     @preco.deleter # método para deletar o atributo preço, usando o decorador @nome_do_metodo.deleter
#     def preco(self):
#         del self.__preco
        
# produto = Produto("Notebook", 2500)
# print(produto.preco)  # Acessa o preço usando o getter
# produto.preco = 3000  # Atualiza o preço usando o setter
# print(produto.preco)  # Acessa o preço atualizado usando o getter


# Exemplo de classe com encapsulamento usando propriedades para calcular a idade a partir do ano de nascimento
import datetime
class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self.__nome = nome
        self.__ano_nascimento = ano_nascimento
        

    @property
    def idade(self):
        _ano_atual = datetime.datetime.now().year
        return _ano_atual - self.__ano_nascimento

pessoa = Pessoa("Carlos", 1990)
print(pessoa.__nome + " " + str(pessoa.idade))  # Acessa o nome e idade usando o getter





# # descontrutor: método especial chamado quando um objeto é destruído (garbage collected)
# class ExemploDestrutor:
#     def __init__(self, nome):
#         self.nome = nome
#         print(f"Objeto {self.nome} criado.")

#     def __del__(self):
#         print(f"Objeto {self.nome} destruído.")
# objeto = ExemploDestrutor("Teste")
# del objeto  # Força a destruição do objeto (chama o destrutor)


# # Desafio 1    
# class bicicleta:
#     def __init__(self, cor, modelo, ano, valor):
#         self.cor = cor
#         self.modelo = modelo
#         self.ano = ano
#         self.valor = valor
    
#     def buzinar(self):
#         return "BIIIIIIIIII"
    
#     def __str__(self):
#         return f"{self.__class__.__name__} : {",".join(f'{chave}={valor}' for chave, valor in self.__dict__.items())}"
    
# bicicleta1 = bicicleta("vermelha", "mountain bike", 2022, 1500.89)
# print(bicicleta1)  # Imprime a descrição da bicicleta1
# print(bicicleta1.buzinar())  # Chama o método buzinar da bicicleta1

# # teste caneca
# class Caneca:
#     def __init__(self, cor, conteudo, cafe=False):
#         self.cor = cor
#         self.conteudo = conteudo
#         self.cafe = cafe

#     def __str__(self):
#         return f"A cor da sua caneca eh {self.cor} com {self.conteudo} dentro dela"
    
#     def ColocarCafe(self):
#         if self.cafe:
#             return "A caneca já tem café, estado atual: com cafe"
#         else:
#             self.cafe = True
#             return "Colocando cafe na caneca, estado atual: " + ("com cafe" if self.cafe else "sem cafe")

# caneca = Caneca("preta", "coca-cola", True)       
# print(caneca)
# print(caneca.ColocarCafe())



# desafios dio
# class Calculadora:
#   def __init__(self):
#     self.num1 = 0
#     self.num2 = 0

#   def soma(self, num1, num2):
#     return num1 + num2

# num1 = int(input())
# num2 = int(input())

# # Criando uma instância da calculadora
# calc = Calculadora()

# resultado = calc.soma(num1, num2)
# print(resultado)

# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade

# #TODO: Crie um método para retornar as informações formatas com Nome e Idade:    
#     def __str__(self):
#       return f"Nome: {self.nome}, idade: {self.idade}"

# # Entrada do usuário
# nome = input()
# idade = int(input())

# # TODO: Crie uma instância da pessoa:
# pessoa = Pessoa(nome, idade)

# #TODO: Chame o método para retornar as informações formatadas e imprima o resultado:
# print(pessoa)

# class conversor:
#   def __init__(self, celsius):
#     self.celsius = celsius

#   def celsius_para_fahrenheit(self):
#     return (1.8 * self.celsius) + 32

# # Entrada do usuário
# celsius = float(input())

# # TODO: Crie uma instância do conversor:
# c = conversor(celsius)

# fahrenheit = c.celsius_para_fahrenheit()1
# print(fahrenheit)


# desafio livro
# class Livro:
#     def __init__(self, titulo, paginas):
#       self.titulo = titulo
#       self.paginas = paginas
#       self.pagina_atual = 1

#     def __str__(self):
#       return f"Livro: {self.titulo}, Páginas: {self.paginas} no total, voce esta na pagina: {self.pagina_atual}"
      
#     def avancar_paginas(self, qtd_pagina = 1):
#       contador = 0
#       for pg in range(0, qtd_pagina, 1):
#         if not self.fim_livro():
#           self.pagina_atual += 1
#           contador += 1
#         else:
#           print("Você já chegou ao final do livro.")
#           break
        
#       print(f"Avançou {contador} páginas, voce esta na pagina: {self.pagina_atual}")

        
#     def fim_livro(self) -> bool:
#       return True if self.pagina_atual >= self.paginas else False
    
# titulo = input("Digite o título do livro: ")
# paginas = int(input("Digite o número total de páginas do livro: "))
# livro = Livro(titulo, paginas)
# print(livro)
# qtd_paginas_avancar = int(input("Digite a quantidade de páginas que deseja avançar: "))
# livro.avancar_paginas(qtd_paginas_avancar)
