# Exercício 03

# Calculaoora simples:
# O usuário insere dois números e, em seguida, ele escolhe a operação matemática
# O programa deve realizar a operação escolhida e exibir o resultado

# Entrada
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
op = input("Digite a operação matemática (+ -> adição, - -> subtração, / -> divisão, * -> multiplicação): ")

# Processamento
if op == "+":                 # Se o usuário escolher o sinal "+" o programa irá resolver como adição
    res = num1 + num2
elif op == "-":               # Se o usuário escolher o sinal "-" o programa irá resolver como subtração
    res = num1 - num2
elif op == "*":               # Se o usuário escolher o sinal "*" o programa irá resolver como multiplicação
    res = num1 * num2
else:                         # O "else" mostra que caso as outras opções não tenham sido escolhidas, o programa vai executar essa
    res = num1 / num2         # Se o usuário escolher o sinal "/" o programa irá resolver como divisão


# Saída
print(" O resultado de:", num1, op, num2, "=", res)