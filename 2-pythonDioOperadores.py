"""Operadores em Python (DIO).

Objetivo: deixar a execução mais organizada e legível.
- Agrupa os exemplos em seções.
- Evita código solto no topo do arquivo.
"""

from __future__ import annotations


def titulo(texto: str) -> None:
	print("\n" + "=" * 60)
	print(texto)
	print("=" * 60)


def exemplo_aritmeticos() -> None:
	titulo("1) Operadores aritméticos")

	# Operadores aritméticos básicos (números inteiros/float)
	soma = 10 + 5
	subtracao = 10 - 5
	divisao = 10 / 2
	multiplicacao = 10 * 2
	resto = 10 % 2  # resto da divisão
	exponenciacao = 10**2  # potenciação
	divisao_inteira = 10 // 3  # quociente sem o resto

	print(f"10 + 5  = {soma}")
	print(f"10 - 5  = {subtracao}")
	print(f"10 / 2  = {divisao}")
	print(f"10 * 2  = {multiplicacao}")
	print(f"10 % 2  = {resto}")
	print(f"10 ** 2 = {exponenciacao}")
	print(f"10 // 3 = {divisao_inteira}")

	# Precedência: parênteses primeiro, depois * / // %, depois + -
	print("\nOrdem de precedência (parênteses -> multiplicação -> soma/subtração):")
	print("10 - 5 * 2 + (10 + 3) =", 10 - 5 * 2 + (10 + 3))


def exemplo_comparacao() -> None:
	titulo("2) Operadores de comparação")

	# Comparações retornam booleano (True/False)
	print("10 >  5:", 10 > 5)
	print("10 <  5:", 10 < 5)
	print("10 == 10:", 10 == 10)
	print("10 != 5:", 10 != 5)
	print("10 >= 5:", 10 >= 5)
	print("10 <= 5:", 10 <= 5)


def exemplo_logicos() -> None:
	titulo("3) Operadores lógicos")

	# Lógicos combinam booleanos (e condições) e retornam booleano
	print("True  and False:", True and False)
	print("True  or  False:", True or False)
	print("not True:", not True)


def exemplo_atribuicao() -> None:
	titulo("4) Operadores de atribuição")

	# Atribuição composta: atualiza a variável usando o valor anterior
	x = 10
	print("x =", x)
	x += 5
	print("x += 5 ->", x)
	x *= 2
	print("x *= 2 ->", x)
	x -= 10
	print("x -= 10 ->", x)
	x /= 2
	print("x /= 2 ->", x)
	x %= 3
	print("x %= 3 ->", x)


def exemplo_identidade() -> None:
	titulo("5) Operadores de identidade (is / is not)")

	# `is` compara identidade (mesma referência/memória)
	# `==` compara igualdade (mesmo conteúdo/valor)
	a = [1, 2, 3]
	b = a
	c = [1, 2, 3]

	print("a is b:", a is b, "(mesmo objeto)")
	print("a is c:", a is c, "(objetos diferentes)")
	print("a == c:", a == c, "(conteúdo igual)")


def exemplo_associacao() -> None:
	titulo("6) Operadores de associação (in / not in)")

	# `in` verifica se um elemento está contido numa sequência/coleção
	print("'a' in 'banana':", "a" in "banana")
	print("'x' in 'banana':", "x" in "banana")
	print("1 in [1, 2, 3]:", 1 in [1, 2, 3])
	print("4 in [1, 2, 3]:", 4 in [1, 2, 3])
	print("'a' not in 'banana':", "a" not in "banana")
	print("'x' not in 'banana':", "x" not in "banana")


def main() -> None:
	exemplo_aritmeticos()
	exemplo_comparacao()
	exemplo_logicos()
	exemplo_atribuicao()
	exemplo_identidade()
	exemplo_associacao()


if __name__ == "__main__":
	main()
