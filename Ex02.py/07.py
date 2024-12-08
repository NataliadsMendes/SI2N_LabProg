# Exercício 07

# Calcula o seu peso ideal conforme o seu genero

# Entrada
h = float(input("Digite a sua altura em metros: "))                   # O usuário digita a sua altura
g = input("Digite o seu gênero (M - mulheres ou H - homens): ")       # O usuário digita o seu gênero

# Processamento
if g == "M" or "m":
    peso = (62.1 * h) - 44.7  # Se a pessoa escolher m (mulher) será calculado essa fórmula
else:
    peso = (72.7 * h) - 58    # Caso não seja escolhido a opção anterior será usado essa fórmula

print(peso)