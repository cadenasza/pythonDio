# nome = input("Digite seu nome: ")
# salario_fixo = float(input("Digite seu salario fixo: "))
# total_vendas = float(input("Digite o total de vendas em dinheiro: "))
# comissao = 0


# dia = int(input("Dia da venda: "))
# if dia > 0 and dia <= 3:
#     comissao = total_vendas * (20 / 100)
# elif dia > 3 and dia <= 5:
#     comissao = total_vendas * (15 / 100)
# else:
#     comissao = total_vendas * (10 / 100)

# salario_final = salario_fixo + comissao
# print(f"Olá {nome}, seu salário final é: R${salario_final:.2f}")

# nome = input("Digite seu nome: ")
# salario = float(input("Digite seu salario: "))

# if salario < 1903.99:
#     print(f"{nome}, você está isento de imposto de renda.")
# elif salario >= 1903.99 and salario <= 2826.65:
#     salario_liquido = salario - (salario * (7.5 / 100))
#     print(f"Ola {nome} , seu salario liquido e de: R${salario_liquido:.2f}")
# elif salario > 2826.65 and salario <= 3751.05:
#     salario_liquido = salario - (salario * (15 / 100))
#     print(f"Ola {nome} , seu salario liquido e de: R${salario_liquido:.2f}")
# elif salario > 3751.05 and salario <= 4664.68:
#     salario_liquido = salario - (salario * (22.5 / 100))
#     print(f"Ola {nome} , seu salario liquido e de: R${salario_liquido:.2f}")
# else:
#     salario_liquido = salario - (salario * (27.5 / 100))
#     print(f"Ola {nome} , seu salario liquido e de: R${salario_liquido:.2f}")

# nome = input("Digite seu nome: ")
# notas = []
# for i in range(5):
#     nota = float(input(f"Digite a nota: {i + 1}: "))
#     notas.append(nota)
    
# media = sum(notas) / len(notas)    
# print("-----------------------")
# print("Resultado final: ")

# print(f"Atleta: {nome}")
# for nota in notas:
#     print(f"Saltos - {nota:.2f}", end=' ')

# print(f"\nMédia dos saltos: {media:.2f} m")
# print("-----------------------")


# carros = []
# combustivel = []
# distancia = 1000
# litro_gasolina = 6.89

# for i in range(5):
#     carro = input("Digite o nome do carro: ")
#     consumo_por_litro = float(input("Digite o consumo por litro: "))
#     carros.append(carro)
#     combustivel.append(consumo_por_litro)
    
# maior_consumo = max(combustivel)
# indice_maior_consumo = combustivel.index(maior_consumo)
    
# print("-----------------------")
# print("Relatório Final: ")
# for k in range(5):
#     litros_necessarios = distancia / combustivel[k]
#     preco = litros_necessarios * litro_gasolina
#     print(f"Carro: {carros[k]} - Litros necessários: {litros_necessarios:.2f} - Preço total: R${preco:.2f}")
    
# print(f"Carro mais econômico: {carros[indice_maior_consumo]} - Consumo: {maior_consumo:.2f} km/l")



# numeros = []
# numeros.append(1)
# numeros.append(2)
# numeros.append(0)
# numeros.append(10)
# numeros.sort()
# print(numeros)
# numeros.sort(reverse=True)
# print(numeros)
# print(numeros[::-1])


numeros = [1, 2, 3, 4, 5, 6,7, 8, 9]
pares = [par for par in numeros if par % 2 == 0]
print(pares)

