# Exercício 10

# Programa para uma loja de tintas
# O programa deverá pedir o taanho em metros da área a ser pintada
# Considere que a cobertura da tinta é de 1 litro para cada três metros quadrados
# A lata de tinta é vendida com 18 litros e que custram R$ 80,00

# Entrada
h = float(input("Digite a altura da área a ser pintada: "))
l = float(input("Digite a largura da área a ser pintada: "))

# Processamento e saída
if h <= 0 or l <= 0:         # Caso o usuário digita números negativos ou o zero, o programa pede para digitar novamente
    print("Digite um valor válido!")
else:
    # Fórmulas:
    area = h * l             # Fórmula para calcular a área

    litro = area / 3         # Calcula a quantidade necessária de litros de tinta
    if litro % 1 != 0:       # Se o número de litros não for inteiro, arredonda para cima
        litro = int(litro) + 1
    else:
        litro = int(litro)   # Se for inteiro, mantém o valor original

    lata = litro / 18        # Fórmula para calcular a quantidade de latas
    if lata % 1 != 0:        # Se o número de latas não for inteiro, arredonda para cima
        lata = int(lata) + 1
    else:
        lata = int(lata)     # Se for inteiro, mantém o valor original

    valor = lata * 80        # Fórmula para calcular o valor total

    print("Para pintar", area, "metros quadrados", "irá precisar de", litro, "litros")
    print("Ou seja, para", lata, "latas, irá gastar R$", valor)