# Programa para calcular o IMC
# Missão: ajudar os usuarios a descobrirem se estão com peso ideal usando um programa

# Entrada de dados
nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso em Kg: "))
altura = float(input("Digite sua altura em metros: "))

# Processamento de dados
altura1 = altura ** 2 
imc = peso / altura1

# Saida dos dados
if imc <= 25:
    print("Seu peso está ideial")
else:
    print("Você está acima do peso: ")