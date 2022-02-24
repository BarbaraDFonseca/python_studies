############################################################
# @author: barbarafonseca95@gmail.com                       #
# @description: Script para determinar se o ano é bissexto  #
# @date: 23/02/2021                                         #
#############################################################

# 1. receber o ano
ano = str(input("[Split] Digite o ano: "))
# #2. dividir o ano por 4
bissexto = int(ano) / 4
# #3. fazer o split pelo .
bissexto = str(bissexto).split(".")
# #4. verificar se a posição 1 é diferente de zero e exibir o resultado
if bissexto[1] != '0':
 		print("O ano não é bissexto")
else:
    print("O ano é bissexto")