# Programa de automatização para calcular o salario dos colaboradores com base no salário familia. 

# Entrada dos dados
nome = (input("Digite seu nome: "))
salario = float(input("Digite seu sálario bruto: "))
filhos = int(input("Digite quantos filhos voce tem! "))
salario_familia = {300.00 * filhos}

# Processamento de dados 

# Formata o salário no padrão brasileiro
salario_formatado = f"{salario:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


if filhos > 0:
    salario_liquido = salario + filhos * 300
    print(f"Seu salario é: {salario_liquido}")
else:
    print(f"Voce nao possui filho, {salario}")
