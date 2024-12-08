# Exercício 11

# Programa para uma loja de tintas:
# O programa deve pedir o tamanho em metros da área a ser pintada
# Considere que a cobertura de tinta é de 1 litro para cada 6 metros quadrados e que tinta é vendida em
# latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros que custam R$ 25,00
# Informar ao usuário a quantidade de tinta a ser comprada e os respectivos preços em três situações

# Entrada
tam = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))

if tam < 0:                        # Condicional para verificar se a entrada é válido, por exemplo, é maior que zero
    print("Digite um valor válido!")
else:
    qtd = tam / 6                  # Fórmula para calcular a quantidade de tinta necessária
    if qtd % 1 != 0:
        qtd = int(qtd) + 1         # Caso o número seja exato arredonda para cima

# Situação 1: comprar apenas latas de 18 litros:
    tinta1 = qtd / 18
    if tinta1 % 1 != 0:
        tinta1 = int(tinta1) + 1
    valor1 = tinta1 * 18

    # Saída
    print("Ao comprar apenas latas de 18 litros:")
    print(f"Será necessário {tinta1} latas, terá um valor de R${valor1: .2f} para pintar {qtd} metros quadrados")

# Situação 2: comprar apenas galões de 3,6 litros:
    tinta2 = qtd / 3.6
    if tinta2 % 1 != 0:
        tinta2 = int(tinta2) + 1 
    valor2 = tinta2 * 25

    # Saída
    print()
    print("Ao comprar apenas galões de 3,6 litros: ")
    print(f'Será necessário {tinta2} latas, terá um valor de R${valor2: .2f} para pintar {qtd} metros quadrados')

# Situação 3: misturar latas e galões, e acrescentar 10% de folga
    tinta_latas = qtd // 18                       # Quantidade de latas de 18 litros necessárias
    tinta_restante = qtd % 18                     # O restante de tinta que não preenche uma lata inteira

    if tinta_restante > 0:                        # Se restar tinta após as latas, será necessário comprar galões
        tinta_galoes = tinta_restante / 3.6
        if tinta_galoes % 1 != 0:
            tinta_galoes = int(tinta_galoes) + 1  # Arredonda para cima, se necessário
    else:
        tinta_galoes = 0                          # Se não houver tinta restante, não é necessário comprar galões

    # Calculando os valores
    valor_latas = tinta_latas * 80                # Preço das latas
    valor_galoes = tinta_galoes * 25              # Preço dos galões
    total = valor_latas + valor_galoes            # Total

    # Saída
    print()
    print("Ao misturar latas e galões:")
    print(f"Será necessário comprar {tinta_latas} latas de 18 litros resultando em: R${valor_latas: .2f}")
    print(f"E precisar comprar {tinta_galoes} galões de 3,6 litros resultando em: R${valor_galoes: .2f}")
    print(f"Totalizando: R${total: .2f} para pintar {qtd} metros quadrados.")
