#Crie um script python que leia o dia, o mês e o ano do nascimento de uma pessoa e mostre uma mensagem com a data formatada

name = input("Antes de iniciarmos, por favor me informe seu nome: ")

print (f"\nÉ um prazer poder falar com você {name} !")
dia = input("\nPor favor me informe o dia que você nasceu: ")
mes = input("\nCerto, agora me informe o mês em que você nasceu: ")
ano = input("\nOk, me informe o ano que você nasceu: ")

print(f'''\nMuito obrigado {name} pelas informações !
\ncom estes dados vamos concluir que você nasceu no dia {dia} de {mes} de {ano}''')