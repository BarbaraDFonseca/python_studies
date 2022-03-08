###########################################################
# @author: barbarafonseca95@gmail.com                     #
# @description: Script que retorna o print de todos os    #
# números pares até o número escolhido                    # 
# @date: 23/02/2022                                       #
###########################################################

#Máximo divisor comum de 2 valores

a = int(
	input('Valor de a: ')
)

b = int(
	input('Valor de b: ')
)

while a%b != 0:
	a, b = b, a%b
print (f'mdc = {b}')