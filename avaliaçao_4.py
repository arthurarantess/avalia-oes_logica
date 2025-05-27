# Missão, criar um programa que ajude os caixas a calcular o valor final das compras

# Entrada de dados
nome_p = input("Digite o produto que você deseja: ")
quantidade_c = int(input("Digite a quantidade de compra desejada: "))
preço_u = float(input("Digite o preço unitário: "))

# Processameno de dados

total_d = quantidade_c * preço_u

if quantidade_c <= 5:
    preço_f = total_d - (total_d * 0.02)
elif quantidade_c >= 10:
    preço_f = total_d - (total_d * 0.03)
else:
    preço_f = total_d - (total_d * 0.05)

# Saida de dados
print(f"Sua compra do {nome_p}, com {quantidade_c} ficou um total de: {preço_f:.2f} desconto já aplicado.")