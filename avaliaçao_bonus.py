# Programa de Agendamento de Hóspedes

# Entrada de dados

mensagem = """

 ✧✧✧✧ ＨＯＴＥＬ ＮＡＣＩＯＮＡＬ ✧✧✧✧

 Olá, Seja bem-vindo ao Hotel Nacional
Atualmente temos apenas acomodações Standard ou Luxo

Standard com 25% de desconto por apenas R$150 adulto e R$75 crianças
Já a luxo... Aqui você encontra tudo o que procurava
O melhor, com um preço imperdível!
De R$400 por R$200 adulto, e crianças de R$200 por R$100

"""

print(mensagem)

nome = input("Digite o nome completo: ")
email = input("Digite o e-mail: ")
tipo_acomodacao = input("Digite o tipo de acomodação: ").lower()
adultos = int(input("Digite a quantidade de adultos: "))
criancas = int(input("Digite a quantidade de crianças: "))

# Processamento dos dados 
total_pessoas = adultos + criancas
if total_pessoas > 4:
    print("Erro: O número total de pessoas não pode ser maior que 4.")
    exit()

dias = int(input("Digite a quantidade de dias de hospedagem: "))
if dias > 30:
    print("Erro: O número máximo de dias é 30.")
    exit()

if tipo_acomodacao == "standard":
    preco_adulto = 150
    preco_crianca = 75
elif tipo_acomodacao == "luxo":
    preco_adulto = 200
    preco_crianca = 100
else:
    print("Erro: Tipo de acomodação inválido.")
    exit()

valor_bruto = (adultos * preco_adulto + criancas * preco_crianca) * dias

if dias <= 5:
    taxa = 0.05
elif dias <= 10:
    taxa = 0.08
else:
    taxa = 0.10

valor_total = valor_bruto + (valor_bruto * taxa)

# Saída dos dados
print("\n--- RESUMO DA RESERVA ---")
print(f"Nome: {nome}")
print(f"E-mail: {email}")
print(f"Acomodação: {tipo_acomodacao.capitalize()}")
print(f"Adultos: {adultos}")
print(f"Crianças: {criancas}")
print(f"Dias: {dias}")
print(f"Valor da hospedagem: R${valor_total:.2f}")