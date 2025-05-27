# Programa que determina se um funcionário já pode se aposentar, Deve analisar idade, tempo de serviço e aplicar as regras da aposentadoria digital


# Entrada de dados
from datetime import date

nome = input("Digite seu nome: ")
ano_nascimento = int(input("Digite o ano que você nasceu: "))
entrada_empresa = int(input("Digite o ano que entrou na empresa: "))

# Processamento de dados e Saida
hoje = date.today()
idade = hoje.year - ano_nascimento
tempo_s = hoje.year - entrada_empresa

if idade >= 65 or tempo_s >= 30:
    print("Aprosentadoria disponivel, contate o RH")
elif idade >= 60 or tempo_s >= 25:
    print("Aprosentadoria disponivel, contate o RH")
else:
    print("Ainda falta um tempo, vai trabalhar vagabundo")
