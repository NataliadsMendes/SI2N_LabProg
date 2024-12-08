# Exercício 05

# O programa que peça dois número inteiros e um número real. Calcule e mostre:
# - O produto do dobro do primero com metade do segundo
# - A soma do triplo do primeiro com o terceiro
# - O terceiro elevado ao cubo

# Entrada
in1 = int(input("Digite o primeiro número inteiro: "))
in2 = int(input("Digite o segundo número inteiro: "))
rea = float(input("Digite um número real: "))

# Processamento
op1 = (2 * in1) * (in2 / 2)    # Primeira operação
op2 = (3 * in1) + rea          # Segunda operação
op3 = rea ** 3                 # Terceira operação

# Saída
print("(2 *", in1, ") * (", in2, "/ 2) = ", op1)
print("(3 *", in1, "+", rea, ") =", op2)
print(rea, "**", 3, "=", op3)

