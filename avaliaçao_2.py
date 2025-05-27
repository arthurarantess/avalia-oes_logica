# Programa Caça-Salário
# Entrada dos dados e processamento dos dados

maior_salario = 0
nome_maior = ""

for i in range(5):
    nome = input(f"Nome do {i+1}º funcionário: ")
    salario = float(input(f"Salário do {i+1}º funcionário (use ponto. ex: 1250.75): "))
    
    if salario > maior_salario:
        maior_salario = salario
        nome_maior = nome

# Formata o salário no padrão brasileiro
salario_formatado = f"{maior_salario:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

# Saida dos dados
print("\n--- Funcionário mais bem pago ---")
print(f"Nome: {nome_maior}")
print(f"Salário: R$ {salario_formatado}")