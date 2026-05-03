"""Estruturas condicionais em Python (DIO).

Organizado em funções e seções para a execução ficar mais clara.
"""

from __future__ import annotations


def titulo(texto: str) -> None:
    print("\n" + "=" * 60)
    print(texto)
    print("=" * 60)


def exemplo_if_elif_else() -> None:
    titulo("1) if / elif / else")

    # `if` executa um bloco se a condição for True
    # `elif` é um "senão se" (testa outra condição)
    # `else` é o caso padrão (quando nenhuma condição anterior é True)
    numero = 10
    if numero > 0:
        print(f"{numero} -> positivo")
    elif numero < 0:
        print(f"{numero} -> negativo")
    else:
        print(f"{numero} -> zero")


def exemplo_multiplas_condicoes() -> None:
    titulo("2) Múltiplas condições (operadores lógicos)")

    # Exemplo: faixas de idade (repare como as condições são avaliadas de cima para baixo)
    idade = 25
    if idade < 18:
        faixa = "menor de idade"
    elif idade < 65:
        faixa = "adulto"
    else:
        faixa = "idoso"
    print(f"Idade {idade} -> {faixa}")

    # Exemplo: comparação encadeada (forma bem comum em Python)
    # 25 < temperatura < 35 é equivalente a: (25 < temperatura) and (temperatura < 35)
    temperatura = 30
    if 25 < temperatura < 35:
        clima = "quente"
    elif 15 <= temperatura <= 25:
        clima = "ameno"
    else:
        clima = "frio"
    print(f"Temperatura {temperatura}°C -> clima {clima}")


def exemplo_classificacao_nota() -> None:
    titulo("3) Classificação por faixas (nota)")

    # Aqui classificamos uma nota por faixas (A, B, C, D, F)
    nota = 85
    if nota >= 90:
        conceito = "A"
    elif nota >= 80:
        conceito = "B"
    elif nota >= 70:
        conceito = "C"
    elif nota >= 60:
        conceito = "D"
    else:
        conceito = "F"
    print(f"Nota {nota} -> conceito {conceito}")


def exemplo_ternario() -> None:
    titulo("4) Operador ternário")

    # Expressão condicional em 1 linha: valor_se_true if condicao else valor_se_false
    idade = 20
    categoria = "Adulto" if idade >= 18 else "Menor de idade"
    print(f"Idade {idade} -> {categoria}")


def dia_da_semana(dia: int) -> str:
    """Retorna o nome do dia para um número (1..7) usando match/case."""
    # `match/case` é parecido com "switch" de outras linguagens.
    # Ele compara o valor e executa apenas o case correspondente.
    match dia:
        case 1:
            return "Domingo"
        case 2:
            return "Segunda-feira"
        case 3:
            return "Terça-feira"
        case 4:
            return "Quarta-feira"
        case 5:
            return "Quinta-feira"
        case 6:
            return "Sexta-feira"
        case 7:
            return "Sábado"
        case _:
            return "Dia inválido"


def exemplo_match_case() -> None:
    titulo("5) match / case")

    # Testando alguns valores, inclusive inválidos, para mostrar o case _ (padrão)
    for valor in (1, 4, 7, 0, 9):
        print(f"{valor} -> {dia_da_semana(valor)}")


def main() -> None:
    exemplo_if_elif_else()
    exemplo_multiplas_condicoes()
    exemplo_classificacao_nota()
    exemplo_ternario()
    exemplo_match_case()


if __name__ == "__main__":
    main()
