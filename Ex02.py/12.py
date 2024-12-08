# Exercício 12

# Programa que peça o tamanho de um arquivo para download (em MB) e velocidade de um link de internet (em Mbps),
# Calcular e informar o tempo aproximado de dowload do arquivo usando este link (em minutos)

# Entrada
tamanho_arquivo = float(input("Digite o tamanho do arquivo para download (em MB): "))
velocidade_link = float(input("Digite a velocidade do link de internet (em Mbps): "))

# Cálculo do tempo de download em segundos
tempo_segundos = (tamanho_arquivo * 8) / velocidade_link

# Convertendo o tempo de segundos para minutos
tempo_minutos = tempo_segundos / 60

# Saída
print(f"O tempo aproximado de download é de {tempo_minutos:.2f} minutos.")