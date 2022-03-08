###########################################################
# @author: barbarafonseca95@gmail.com                     #
# @description: Script que retorna o print de todos os    #
# números pares até o número escolhido                    # 
# @date: 23/02/2022                                       #
###########################################################

#Calcular o n elemento da sequência de fibonacci
a = 1
b = 1
k = 1
n = int(
	input('Valor: ')
)
while k <= n-2:
	a, b = b, a + b
	k = k + 1
print (b)
