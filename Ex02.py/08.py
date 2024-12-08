# Exercício 08

# Rendimento diário de uma pescaria:
    # Caso o peso excedente ultrapasse 50 kg deve pagar uma multa de R$ 4,00 por quilo excedente
# O programa deve ler a variavel e calcular o excesso

# Entrada
peso = float(input("Digite a quantidade de quilos que foi pescado: "))

# Processamento e saída
if peso >= 0:
    if peso <= 50:
        multa = 0
    else:
        multa = (peso - 50) * 4
    print("Pescando", peso, "kg", "terá uma multa equivalente a: R$", multa)

else:
    print("Digite um valor válido!")