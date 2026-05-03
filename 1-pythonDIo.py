"""Resumo prático de Python (do básico ao mais avançado).

Execute este arquivo para ver exemplos na prática.
Os exemplos seguem o mesmo estilo do seu script: comentários + prints.
"""

from __future__ import annotations

# Observação:
# - `from __future__ import annotations` faz com que anotações de tipo sejam
#   tratadas como strings internamente (ajuda a evitar problemas de "forward refs"
#   e melhora performance/compatibilidade em alguns cenários).

import asyncio
import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


def titulo(texto: str) -> None:
	"""Imprime um título de seção no console.

	O objetivo é organizar a saída do script para ficar fácil de ler.
	"""
	print("\n" + "=" * 60)
	print(texto)
	print("=" * 60)


def exemplo_variaveis_tipos() -> None:
	"""Demonstra variáveis, tipos básicos e operações simples.

	Pontos importantes:
	- Python é dinamicamente tipado: o tipo está no valor, não na variável.
	- `type(x)` mostra o tipo do objeto.
	- `int('42')` converte string para inteiro (se for numérico).
	- f-string (f"...") é a forma moderna e mais comum de formatar texto.

	Resultado esperado (resumo):
	- Mostra nome/idade, seus tipos, soma, concatenação e troca de tipo.
	"""
	titulo("1) Variáveis, tipos e operações")

	# variaveis - nao precisam ser tipadas
	nome = "João"
	idade = 30
	# imprimindo variaveis
	print("Nome:", nome)
	print("Idade:", idade)
	# tipos de dados
	print("Tipo de nome:", type(nome))
	print("Tipo de idade:", type(idade))
	# operações com variaveis
	soma = idade + 5
	print("Idade + 5:", soma)
	# concatenando strings
	sobrenome = "Silva"
	nome_completo = nome + " " + sobrenome
	print("Nome completo:", nome_completo)
	# variaveis dinamicas
	variavel = "Texto"
	print("Valor da variavel:", variavel)
	variavel = 100
	print("Valor da variavel agora:", variavel)

	# valores booleanos
	ativo = True
	print("Ativo:", ativo, "| tipo:", type(ativo))

	# conversão (casting)
	texto_numero = "42"
	numero = int(texto_numero)
	print("Texto para int:", numero, "| tipo:", type(numero))

	# f-strings (muito usado no dia a dia)
	print(f"Olá, {nome}. Ano que vem você terá {idade + 1} anos.")


def exemplo_strings() -> None:
	"""Demonstra operações comuns com strings.

	Pontos importantes:
	- Strings são imutáveis: métodos retornam uma NOVA string.
	- `repr()` mostra a representação “crua” (útil para ver espaços e \n).
	- `strip()` remove espaços (e quebras) nas pontas.
	- `split()` quebra em lista de palavras.
	"""
	titulo("2) Strings (métodos comuns)")

	# `repr` ajuda a enxergar espaços no começo/fim
	frase = "  Python é incrível!  "
	print("Original:", repr(frase))
	print("strip:", repr(frase.strip()))
	print("upper:", frase.upper())
	print("lower:", frase.lower())
	print("replace:", frase.replace("incrível", "poderoso"))
	print("split:", frase.strip().split())


def exemplo_colecoes() -> None:
	"""Demonstra coleções mais usadas: list, tuple, dict e set.

	Pontos importantes:
	- `list` é mutável (pode adicionar/remover/alterar).
	- `tuple` é imutável (boa para "registro" fixo).
	- `dict` mapeia chave -> valor.
	- `set` não mantém duplicatas (ótimo para deduplicar e operações de conjunto).
	"""
	titulo("3) Coleções: list, tuple, dict, set")

	# list (mutável)
	numeros = [1, 2, 3]
	numeros.append(4)
	print("Lista:", numeros)
	print("Primeiro elemento:", numeros[0])

	# tuple (imutável)
	coordenada = (10, 20)
	print("Tupla:", coordenada)

	# dict (chave -> valor)
	pessoa = {"nome": "Ana", "idade": 25}
	pessoa["cidade"] = "São Paulo"
	print("Dicionário:", pessoa)
	print("pessoa['nome']:", pessoa["nome"])

	# set (conjunto, sem duplicatas)
	letras = {"a", "b", "a", "c"}
	print("Set (sem repetição):", letras)


def exemplo_controle_fluxo() -> None:
	"""Demonstra controle de fluxo: if/elif/else, for e while.

	Pontos importantes:
	- `range(n)` gera 0..n-1.
	- `while` precisa de condição que eventualmente pare (senão vira loop infinito).
	"""
	titulo("4) Controle de fluxo: if/elif/else, for, while")

	idade = 17
	if idade >= 18:
		print("Maior de idade")
	elif idade >= 16:
		print("Pode votar (no Brasil)")
	else:
		print("Menor de idade")

	# for
	for i in range(3):
		print("for -> i:", i)

	# while
	contador = 0
	while contador < 3:
		print("while -> contador:", contador)
		contador += 1


def soma(a: int, b: int = 0) -> int:
	"""Soma dois inteiros.

	Pontos importantes:
	- `b=0` é um parâmetro com valor padrão (opcional na chamada).
	- A anotação `-> int` é *type hint* (não força tipo em runtime, mas ajuda IDE).
	"""
	return a + b


def exemplo_funcoes_args_kwargs() -> None:
	"""Demonstra funções, parâmetros padrão, *args e **kwargs.

	Pontos importantes:
	- `*args` captura argumentos posicionais extras em uma tupla.
	- `**kwargs` captura argumentos nomeados extras em um dicionário.
	- Muito usado para funções flexíveis e wrappers/decorators.
	"""
	titulo("5) Funções, *args e **kwargs")

	print("soma(10, 5):", soma(10, 5))
	print("soma(10):", soma(10))

	def somar_todos(*args: int) -> int:
		# *args vira uma tupla de argumentos
		# Resultado: soma todos os valores passados.
		total = 0
		for valor in args:
			total += valor
		return total

	print("somar_todos(1, 2, 3, 4):", somar_todos(1, 2, 3, 4))

	def exibir_dados(**kwargs: object) -> None:
		# **kwargs vira um dicionário
		# Resultado: imprime o dicionário recebido.
		print("kwargs:", kwargs)

	exibir_dados(nome="Carlos", idade=40, ativo=True)


def exemplo_comprehensions() -> None:
	"""Demonstra comprehensions e lambda.

	Pontos importantes:
	- Comprehensions criam listas/dicts de forma concisa.
	- `if` dentro da comprehension filtra elementos.
	- `lambda` é útil para funções curtas; para lógica maior, prefira `def`.
	"""
	titulo("6) Comprehensions (listas/dicts) e lambda")

	numeros = [1, 2, 3, 4, 5]
	quadrados = [n * n for n in numeros]
	pares = [n for n in numeros if n % 2 == 0]
	print("Quadrados:", quadrados)
	print("Pares:", pares)

	mapa = {n: n * n for n in numeros}
	print("Dict comprehension:", mapa)

	# lambda (função anônima pequena)
	dobrar = lambda x: x * 2
	print("lambda dobrar(10):", dobrar(10))


def exemplo_excecoes() -> None:
	"""Demonstra tratamento de erros com try/except/else/finally.

	Pontos importantes:
	- `except ValueError` captura erro específico (boa prática).
	- `else` roda só se NÃO houve exceção.
	- `finally` roda sempre (ideal para liberar recursos/limpeza).
	"""
	titulo("7) Exceções (try/except/else/finally)")

	texto = "abc"
	try:
		numero = int(texto)
	except ValueError as e:
		print("Erro ao converter para int:", e)
	else:
		print("Conversão ok:", numero)
	finally:
		print("finally: sempre executa")


def exemplo_arquivos() -> None:
	"""Demonstra escrita/leitura de arquivo com `pathlib.Path`.

	Pontos importantes:
	- `Path` é a forma moderna de lidar com caminhos.
	- `write_text/read_text` facilitam operações simples.
	- `with ... open()` garante fechamento do arquivo.
	- Aqui o arquivo é criado e removido no final (exemplo auto-contido).
	"""
	titulo("8) Arquivos e Pathlib (com context manager)")

	# Context manager: 'with' garante fechamento do recurso
	caminho = Path("exemplo_pythondio.txt")
	conteudo = "Linha 1\nLinha 2\n"

	caminho.write_text(conteudo, encoding="utf-8")
	print("Arquivo criado:", caminho.resolve())

	with caminho.open("r", encoding="utf-8") as f:
		texto = f.read()
	print("Conteúdo lido:")
	print(texto)

	# limpeza (para não deixar arquivo sobrando)
	try:
		caminho.unlink()
		print("Arquivo removido:", caminho.name)
	except OSError as e:
		print("Não foi possível remover o arquivo:", e)


class ContaBancaria:
	"""Exemplo de Programação Orientada a Objetos (POO).

	O que demonstra:
	- `__init__` inicializa o objeto.
	- `@property` expõe `saldo` como atributo somente-leitura.
	- `depositar/sacar` encapsulam regras de negócio.
	- `_saldo` é "convencionalmente privado" (por convenção, não por bloqueio).
	"""
	titulo_classe = "9) POO: classes, métodos e propriedades"

	def __init__(self, titular: str, saldo: float = 0.0) -> None:
		"""Cria a conta com titular e saldo inicial."""
		self.titular = titular
		self._saldo = saldo

	@property
	def saldo(self) -> float:
		"""Retorna o saldo atual (somente leitura)."""
		return self._saldo

	def depositar(self, valor: float) -> None:
		"""Adiciona dinheiro ao saldo.

		Regra importante:
		- Não aceita valores <= 0 (levanta ValueError).
		"""
		if valor <= 0:
			raise ValueError("Depósito deve ser positivo")
		self._saldo += valor

	def sacar(self, valor: float) -> None:
		"""Remove dinheiro do saldo.

		Regras importantes:
		- Não aceita valores <= 0.
		- Não permite sacar mais do que o saldo (evita saldo negativo).
		"""
		if valor <= 0:
			raise ValueError("Saque deve ser positivo")
		if valor > self._saldo:
			raise ValueError("Saldo insuficiente")
		self._saldo -= valor

	def __repr__(self) -> str:
		"""Representação amigável do objeto (útil para debug/prints)."""
		return f"ContaBancaria(titular={self.titular!r}, saldo={self._saldo:.2f})"


def exemplo_poo() -> None:
	"""Demonstra uso prático da classe `ContaBancaria`.

	Resultado esperado:
	- imprime a conta inicial, depois após depositar e após sacar.
	"""
	titulo(ContaBancaria.titulo_classe)

	conta = ContaBancaria("João", 100.0)
	print("Conta inicial:", conta)
	conta.depositar(50.0)
	print("Após depositar 50:", conta, "| saldo:", conta.saldo)
	conta.sacar(30.0)
	print("Após sacar 30:", conta)


@dataclass(frozen=True)
class Produto:
	"""Exemplo de `dataclass`.

	Pontos importantes:
	- `@dataclass` gera automaticamente `__init__`, `__repr__`, etc.
	- `frozen=True` torna o objeto imutável (não deixa alterar atributos).
	"""
	nome: str
	preco: float


def exemplo_dataclass_typing() -> None:
	"""Demonstra `dataclass` e type hints (typing).

	Pontos importantes:
	- Type hints ajudam IDE/linters e documentação do código.
	- `Iterable[float]` aceita lista, tupla, generator, etc.
	"""
	titulo("10) Dataclasses e type hints (typing)")

	produto = Produto(nome="Camiseta", preco=59.9)
	print("Dataclass Produto:", produto)

	def total(precos: Iterable[float]) -> float:
		"""Soma uma coleção de preços e retorna o total."""
		soma_precos = 0.0
		for p in precos:
			soma_precos += p
		return soma_precos

	print("Total:", total([10.0, 20.5, 3.25]))


def meu_decorator(func):
	"""Decorator simples.

	O que faz:
	- Recebe uma função (`func`) e devolve um wrapper.
	- O wrapper imprime mensagens antes/depois de chamar a função original.

	Ponto importante:
	- Decorators são muito usados para log, validação, cache, autenticação, etc.
	"""
	def wrapper(*args, **kwargs):
		# `*args/**kwargs` permitem repassar qualquer assinatura de função.
		print("Antes da função")
		resultado = func(*args, **kwargs)
		print("Depois da função")
		return resultado

	return wrapper


@meu_decorator
def dizer_oi(nome: str) -> None:
	"""Função decorada: ao chamar, passa pelo wrapper do decorator."""
	print("Oi,", nome)


def exemplo_decorators() -> None:
	"""Demonstra o efeito de um decorator na chamada de função."""
	titulo("11) Decorators")
	dizer_oi("Maria")


def contador_infinito():
	"""Generator infinito que produz 0, 1, 2, 3, ...

	Pontos importantes:
	- `yield` pausa e retoma a função.
	- É "infinito" de propósito, então o consumidor deve limitar quantos valores
	  vai puxar (como fazemos com `next()` 5 vezes).
	"""
	n = 0
	while True:
		yield n
		n += 1


def exemplo_generators() -> None:
	"""Demonstra consumo de generator com `next()`.

	Resultado esperado:
	- imprime os 5 primeiros números do contador.
	"""
	titulo("12) Iteradores e generators")

	gen = contador_infinito()
	print("Próximos 5 valores do generator:")
	for _ in range(5):
		print(next(gen))


async def tarefa_assincrona() -> str:
	"""Exemplo de função assíncrona.

	Pontos importantes:
	- `async def` define uma coroutine.
	- `await` libera o event loop enquanto aguarda I/O/tempo.
	- Ideal para tarefas I/O-bound (rede, disco, APIs), não para CPU pesada.
	"""
	await asyncio.sleep(0.1)
	return "resultado async"


def exemplo_asyncio() -> None:
	"""Demonstra como executar uma coroutine com `asyncio.run`.

	Ponto importante:
	- `asyncio.run(...)` cria e gerencia um event loop.
	- Em notebooks/ambientes que já têm loop rodando, `asyncio.run` pode falhar;
	  aí normalmente usa-se `await` diretamente (no contexto do notebook).
	"""
	titulo("13) Async/Await (asyncio)")
	resultado = asyncio.run(tarefa_assincrona())
	print("Async retornou:", resultado)


def exemplo_logging() -> None:
	"""Demonstra logging.

	Pontos importantes:
	- Em projetos reais, prefira `logging` ao invés de muitos `print()`.
	- `logging.exception(...)` deve ser chamado dentro de um `except`:
	  ele inclui automaticamente o traceback (pilha de erro) na saída.
	"""
	titulo("14) Logging (boas práticas ao invés de só print)")

	logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
	logging.info("Aplicação iniciou")
	logging.warning("Exemplo de aviso")
	try:
		1 / 0
	except ZeroDivisionError:
		logging.exception("Erro capturado")


def main() -> None:
	"""Orquestra a execução de todos os exemplos em sequência."""
	exemplo_variaveis_tipos()
	exemplo_strings()
	exemplo_colecoes()
	exemplo_controle_fluxo()
	exemplo_funcoes_args_kwargs()
	exemplo_comprehensions()
	exemplo_excecoes()
	exemplo_arquivos()
	exemplo_poo()
	exemplo_dataclass_typing()
	exemplo_decorators()
	exemplo_generators()
	exemplo_asyncio()
	exemplo_logging()


if __name__ == "__main__":
	main()


























