# Exerício 09

# Programa que pergunta o quanto ganha ganha por hora e o número de horas trabalhadas no mês
# Calcular e mostrar o salário bruto, salário líquido, e os descontos no referido mês, sabendo-se que são descontados:
    # 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato

# Entrada
hora = float(input("Digite a quantidade de horas trabalhadas: "))
val = float(input("Digite o valor da hora trabalhada: "))

# Processamento e saída
if hora < 0 or val < 0:    # Se o usuário digitar números menores que zero o programa pedirá para digitar de novo
    print("Digite um valor válido!")
else:
    # Fórmulas
    sb = hora * val        # Salário bruto
    ir = sb * 11 / 100     # Imposto de Renda
    inss = sb * 8 / 100    # INSS
    si = sb * 5 / 100      # Sindicato
    de = ir + inss + si    # Descontos
    sl = sb - de           # Salário líquido
    # Sáida com o resultado
    print("Salário bruto: R$", sb)
    print("Imposto de Renda: R$", ir)
    print("INSS: R$:", inss)
    print("Sindicato: R$", si)
    print("Descontos: R$", de)
    print("Salário Líquido: R$", sl)