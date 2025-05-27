# Bot para uma lanchonete
# Entrada dos dados
pedido = 0 
qnt = 0 
valor = 0 

mensagem = """
ㅤ・・・ ＬＡＮＣＨＯＮＥＴＥ ＤＯ ＢＡＩＲＲＯ ・・・

    Olá, sejá bem-vindo a lanchoete
・・・ 1 X-tudo R$:12,00 ・・・
・・・ 2 Batatas-frita R$6,00 ・・・
・・・ 3 Coca cola R$:6,00 ・・・
・・・ 4 Cachorro quente R$10,00 ・・・

"""
print (mensagem)

#qnt = quantidade
pedido = int(input("Digite o numero do seu pedido: "))
qnt =int(input("Digite a quantidade de unidade: "))

# Processamento dos dados e saida dos dados
if pedido == 1:
    valor = qnt * 12.00
    pedido = ("X-tudo")
    print(f"O valor do eu pedido ficou {qnt} unidades de {pedido} foi R${valor:.2f}")
elif pedido == 2:
    valor = qnt * 6.00
    pedido = ("Batata Frita")
    print(f"O valor do eu pedido ficou {qnt} unidades de {pedido} foi R${valor:.2f}")
if pedido == 3:
    valor = qnt * 6.00
    pedido = ("Coca-Cola")
    print(f"O valor do eu pedido ficou {qnt} unidades de {pedido} foi R${valor:.2f}")
if pedido == 4:
    valor = qnt * 10.00
    pedido = ("Cachorro-Quente")
    print(f"O valor do eu pedido ficou {qnt} unidades de {pedido} foi R${valor:.2f}")

