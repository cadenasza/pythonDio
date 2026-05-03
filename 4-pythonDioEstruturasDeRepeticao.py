"""Estruturas de repetição em Python (DIO).

Organizado em seções/funções para ficar mais apresentável ao executar.
"""

from __future__ import annotations


def titulo(texto: str) -> None:
    print("\n" + "=" * 60)
    print(texto)
    print("=" * 60)


def exemplo_while() -> None:
    titulo("1) while")

    # `while` repete enquanto a condição for True
    contador = 0
    while contador < 5:
        print(f"contador = {contador}")
        contador += 1  # incrementa para evitar loop infinito


def exemplo_for_range() -> None:
    titulo("2) for + range")

    # `for` percorre um iterável; `range(n)` gera 0..n-1
    for i in range(5):  # 0..4
        print(f"range(5) -> i = {i}")

    print("\nrange(2, 10, 2) -> pares de 2 a 8")
    # range(inicio, fim, passo) -> vai até (fim - 1)
    for j in range(2, 10, 2):
        print(f"j = {j}")


def exemplo_iterando_string() -> None:
    titulo("3) Iterando em string")

    # String é iterável: o `for` percorre cada caractere
    palavra = "Python"
    for letra in palavra:
        print(f"letra = {letra}")


def exemplo_enumerate() -> None:
    titulo("4) enumerate (índice + valor)")

    # `enumerate(lista)` retorna pares (indice, valor)
    frutas = ["maçã", "banana", "laranja"]
    for indice, fruta in enumerate(frutas):
        print(f"{indice} -> {fruta}")


def exemplo_iterando_lista() -> None:
    titulo("5) Iterando em lista")

    frutas = ["maçã", "banana", "laranja"]
    for fruta in frutas:
        print(f"fruta = {fruta}")


def exemplo_iterando_dict() -> None:
    titulo("6) Iterando em dicionário")

    pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
    # `items()` retorna (chave, valor)
    for chave, valor in pessoa.items():
        print(f"{chave}: {valor}")


def exemplo_break() -> None:
    titulo("7) break")

    # `break` interrompe o loop imediatamente
    contador = 0
    while True:
        print(f"contador = {contador}")
        contador += 1
        if contador >= 5:
            break  # sai do loop quando o contador atingir 5


def exemplo_continue() -> None:
    titulo("8) continue")

    # `continue` pula para a próxima iteração do loop
    for i in range(10):
        if i % 2 == 0:
            continue  # pula os pares
        print(f"ímpar = {i}")


def main() -> None:
    exemplo_while()
    exemplo_for_range()
    exemplo_iterando_string()
    exemplo_enumerate()
    exemplo_iterando_lista()
    exemplo_iterando_dict()
    exemplo_break()
    exemplo_continue()


if __name__ == "__main__":
    main()



