# Exercício 01

# Média de notas, solicita ao usuário para inserir cinco notas e calcular a sua média

# Entrada
not1 = float(input("Digite a nota da primeira disciplina: ")) # O usuário insere a primeira nota
not2 = float(input("Digite a nota da segunda disciplina: "))  # O usuário insere a segunda nota
not3 = float(input("Digite a nota do terceira displina: "))   # O usuário insere a terceira nota
not4 = float(input("Digite a nota da quarta disciplina: "))   # O usuário insere a quarta nota
not5 = float(input("Digite a nota da quinta disciplina: "))   # O usuário insere a quinta nota

# Processamento
media = (not1+not2+not3+not4+not5) / 5                        # Calcula a média

# Saída
print("A média das notas inseridas é:", media)                # Mostre o resultado