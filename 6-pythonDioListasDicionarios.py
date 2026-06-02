"""Listas, dicionários, tuplas e sets em Python (DIO).

Refatorado para ficar mais organizado e “apresentável” ao executar:
- Exemplos agrupados por tópico
- Saída com títulos/separadores
- `main()` como ponto de entrada
"""

from __future__ import annotations


def titulo(texto: str) -> None:
    print("\n" + "=" * 60)
    print(texto)
    print("=" * 60)


def separador() -> None:
    print("-" * 60)


def exemplo_listas_criacao_acesso() -> None:
    titulo("1) Listas: criação e acesso")

    # Listas:
    # - mutáveis (dá para alterar)
    # - ordenadas (mantêm a ordem de inserção)
    # - indexadas (acesso por índice)
    lista1 = [1, 2, 3, 4, 5]
    lista2 = ["maçã", "banana", "laranja"]
    lista3 = [1, "maçã", 3.14, True]

    print("lista1:", lista1)
    print("lista2:", lista2)
    print("lista3:", lista3)
    separador()

    print("lista1[0]  (primeiro):", lista1[0])
    print("lista2[1]  (segundo):", lista2[1])
    print("lista3[2]  (terceiro):", lista3[2])
    print("lista1[-1] (último):", lista1[-1])
    print("lista2[0:2] (slice):", lista2[0:2])
    print("lista3[:] (toda):", lista3[:])
    print("lista1[::2] (de 2 em 2):", lista1[::2])




def exemplo_listas_metodos() -> None:
    titulo("2) Listas: métodos comuns")

    # Métodos mais usados em listas
    frutas = ["maçã", "banana", "laranja"]
    print("Inicial:", frutas)

    # append adiciona no final
    frutas.append("uva")
    print("append('uva'):", frutas)

    # insert adiciona em uma posição específica (desloca o resto)
    frutas.insert(1, "abacaxi")
    print("insert(1, 'abacaxi'):", frutas)

    # remove remove pela 1ª ocorrência do valor (se não existir, gera erro)
    frutas.remove("banana")
    print("remove('banana'):", frutas)

    # pop remove por índice e retorna o valor removido (padrão: último)
    removido = frutas.pop()
    print("pop() ->", removido, "| lista:", frutas)

    removido = frutas.pop(0)
    print("pop(0) ->", removido, "| lista:", frutas)

    print("Iterando:")
    for fruta in frutas:
        print("-", fruta)

    # copy faz uma cópia "rasa" (shallow copy)
    frutas2 = frutas.copy()
    print("copy() -> frutas2:", frutas2)

    # sort ordena a lista "in-place" (altera a própria lista)
    frutas.sort()
    print("sort() ->", frutas)

    # reverse inverte a lista "in-place"
    frutas.reverse()
    print("reverse() ->", frutas)

    frutas.extend(["melancia", "abacate"])
    print("extend([...]) ->", frutas)

    frutas.clear()
    print("clear() ->", frutas)

def exemplo_matriz() -> None:
    titulo("3) Matriz (lista de listas)")

    # Matriz é uma lista onde cada item é outra lista (estrutura 2D)
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    print("Matriz:")
    for linha in matriz:
        print(linha)

    separador()
    print("matriz[0][1] (linha 0, coluna 1):", matriz[0][1])


def exemplo_list_comprehension() -> None:
    titulo("4) List comprehension")

    # Forma concisa de criar listas a partir de iteráveis
    quadrados = [x**2 for x in range(10)]
    print("Quadrados 0..9:", quadrados)


def exemplo_dicionarios() -> None:
    titulo("5) Dicionários: criação, acesso e métodos")

    # Dicionários:
    # - mapeiam chave -> valor
    # - são mutáveis
    pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
    print("pessoa:", pessoa)
    print("pessoa['nome']:", pessoa["nome"])

    # get evita KeyError (pode ter valor padrão)
    print("pessoa.get('idade'):", pessoa.get("idade"))
    print("pessoa.get('profissao', 'Desconhecida'):", pessoa.get("profissao", "Desconhecida"))

    separador()
    pessoa["profissao"] = "Engenheiro"
    print("Adicionar profissao:", pessoa)
    pessoa["idade"] = 31
    print("Atualizar idade:", pessoa)
    removido = pessoa.pop("cidade")
    print("pop('cidade') ->", removido, "| dict:", pessoa)

    separador()
    # items() retorna pares (chave, valor)
    print("items():")
    for chave, valor in pessoa.items():
        print(f"- {chave}: {valor}")

    # keys() e values() retornam visões (views); aqui transformamos em list só pra imprimir
    print("keys():", list(pessoa.keys()))
    print("values():", list(pessoa.values()))


def exemplo_dict_aninhado() -> None:
    titulo("6) Dicionário aninhado")

    # Um dicionário pode ter outros dicionários como valores
    alunos = {
        "aluno1": {"nome": "Maria", "idade": 22, "curso": "Engenharia"},
        "aluno2": {"nome": "Pedro", "idade": 24, "curso": "Medicina"},
        "aluno3": {"nome": "Ana", "idade": 21, "curso": "Direito"},
    }

    for aluno, info in alunos.items():
        print(aluno + ":")
        for chave, valor in info.items():
            print(f"  {chave}: {valor}")


def exemplo_dict_com_listas() -> None:
    titulo("7) Dicionário com listas")

    # Valores do dicionário também podem ser listas (ou qualquer outro tipo)
    cursos = {
        "Engenharia": ["Maria", "João", "Ana"],
        "Medicina": ["Pedro", "Lucas"],
        "Direito": ["Ana", "Carla"],
    }

    for curso, alunos in cursos.items():
        print(f"{curso}: {', '.join(alunos)}")


def exemplo_tuplas() -> None:
    titulo("8) Tuplas")

    # Tuplas:
    # - imutáveis (não dá para alterar)
    # - ordenadas e indexadas
    tupla1 = (1, 2, 3, 4, 5)
    tupla2 = ("maçã", "banana", "laranja")
    tupla3 = (1, "maçã", 3.14, True)

    print("tupla1:", tupla1)
    print("tupla2:", tupla2)
    print("tupla3:", tupla3)
    separador()

    print("tupla1[0]:", tupla1[0])
    print("tupla2[1]:", tupla2[1])
    print("tupla3[2]:", tupla3[2])
    separador()

    print("Iterando tupla1:")
    for elemento in tupla1:
        print("-", elemento)

    separador()
    print("tupla1.count(2):", tupla1.count(2))
    print("tupla1.index(3):", tupla1.index(3))


def exemplo_tuplas_aninhadas_e_dicts() -> None:
    titulo("9) Tuplas aninhadas e tupla de dicionários")

    tupla_aninhada = ((1, 2), (3, 4), (5, 6))
    for t in tupla_aninhada:
        print("Tupla:", t)
        for elemento in t:
            print("  elemento:", elemento)

    separador()

    tupla_dicionario = (
        {"nome": "Maria", "idade": 22},
        {"nome": "Pedro", "idade": 24},
        {"nome": "Ana", "idade": 21},
    )
    for pessoa in tupla_dicionario:
        print(f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']}")


def exemplo_sets() -> None:
    titulo("10) Sets")

    # Sets:
    # - não permitem duplicatas
    # - não são indexados (não dá pra acessar por posição)
    set0 = set()  # set vazio
    set1 = {1, 2, 3, 3, 4, 5}  # duplicatas são removidas
    set2 = {"maçã", "banana", "laranja"}
    set3 = {1, "maçã", 3.14, True}
    print("set1:", set1)
    print("set2:", set2)
    print("set3:", set3)

    separador()
    print("Iterando set1:")
    for elemento in set1:
        print("-", elemento)

    separador()
    set1.add(6)
    print("add(6) ->", set1)
    # remove gera erro se o elemento não existir; discard não gera
    set1.remove(3)
    print("remove(3) ->", set1)
    set1.discard(4)
    print("discard(4) ->", set1)


def exemplo_operacoes_set() -> None:
    titulo("11) Operações com sets")

    # Operações típicas de conjuntos: união, interseção, diferença
    set_a = {1, 2, 3, 4}
    set_b = {3, 4, 5, 6}
    print("A:", set_a)
    print("B:", set_b)
    separador()
    print("união (A | B):", set_a.union(set_b))
    print("interseção (A & B):", set_a.intersection(set_b))
    print("diferença (A - B):", set_a.difference(set_b))
    print("issubset (B ⊆ A):", set_b.issubset(set_a)) # elemnetos de B estão em A? False
    print("issuperset (A ⊇ B):", set_a.issuperset(set_b)) # elemnetos de A estão em B? False


def main() -> None:
    exemplo_listas_criacao_acesso()
    exemplo_listas_metodos()
    exemplo_matriz()
    exemplo_list_comprehension()
    exemplo_dicionarios()
    exemplo_dict_aninhado()
    exemplo_dict_com_listas()
    exemplo_tuplas()
    exemplo_tuplas_aninhadas_e_dicts()
    exemplo_sets()
    exemplo_operacoes_set()


if __name__ == "__main__":
    main()






