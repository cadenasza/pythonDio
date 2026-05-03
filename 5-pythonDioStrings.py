"""Strings em Python (DIO).

Organizado por seções e com `main()` para a execução ficar mais limpa.
"""

from __future__ import annotations


def titulo(texto: str) -> None:
	print("\n" + "=" * 60)
	print(texto)
	print("=" * 60)


def exemplo_criacao() -> None:
	titulo("1) Criando strings")

	# Strings podem ser declaradas com aspas simples ou duplas
	string1 = "Olá, mundo!"  # aspas duplas
	string2 = "Olá, mundo!"  # aspas simples (mesmo resultado)

	# Strings multilinha usam aspas triplas
	string3 = """Olá,
mundo!"""  # multilinha

	print("string1:", string1)
	print("string2:", string2)
	print("string3:\n" + string3)


def exemplo_index_slice() -> None:
	titulo("2) Acessando caracteres (index e slice)")

	# Strings são sequências: dá pra acessar por índice e por "fatia" (slice)
	frase = "Python é incrível!"
	print("frase:", frase)
	print("frase[0]  (primeiro):", frase[0])  # índice 0
	print("frase[7]  (8º char):", frase[7])
	print("frase[-1] (último):", frase[-1])  # índice negativo conta a partir do fim

	# slice: [inicio:fim] (fim não entra) | [inicio:fim:passo]
	print("frase[0:6] (0..5):", frase[0:6])
	print("frase[:] (toda):", frase[:])
	print("frase[::2] (de 2 em 2):", frase[::2])
	print("frase[::-1] (reverso):", frase[::-1])
	print(f"Original vs reverso: {frase} | {frase[::-1]}")


def exemplo_concat_repeticao() -> None:
	titulo("3) Concatenação e repetição")

	# Concatenação com +
	nome = "João"
	sobrenome = "Silva"
	nome_completo = nome + " " + sobrenome
	print("nome_completo:", nome_completo)

	# Repetição com *
	repeticao = "Python " * 3
	print("repeticao:", repeticao)


def exemplo_fstring() -> None:
	titulo("4) f-strings")

	# f-string é a forma mais comum de interpolar variáveis em texto
	nome = "Maria"
	idade = 28
	mensagem = f"Meu nome é {nome} e eu tenho {idade} anos."
	print(mensagem)


def exemplo_metodos() -> None:
	titulo("5) Métodos úteis de string")

	# Strings são imutáveis: métodos retornam uma nova string (não alteram a original)
	texto = "   Olá, Mundo!   "
	# repr() mostra a representação "crua" (útil para enxergar espaços e \n)
	print("texto (repr):", repr(texto))
	print("strip:", repr(texto.strip()))
	print("upper:", texto.upper())
	print("lower:", texto.lower())
	print("replace:", texto.replace("Mundo", "Python"))
	print("split:", texto.split())
	print("len:", len(texto))
	print("count('o'):", texto.count("o"))
	print("title:", texto.title())
	print("center(30, '*'):", texto.center(30, "*"))


def exemplo_join_format_numerico() -> None:
	titulo("6) join e formatação numérica")

	texto_join = "Python"
	print("'-'.join('Python'):", "-".join(texto_join))

	pi = 3.14159
	print(f"O valor de PI é aproximadamente {pi:.2f}.")


def main() -> None:
	exemplo_criacao()
	exemplo_index_slice()
	exemplo_concat_repeticao()
	exemplo_fstring()
	exemplo_metodos()
	exemplo_join_format_numerico()


if __name__ == "__main__":
	main()