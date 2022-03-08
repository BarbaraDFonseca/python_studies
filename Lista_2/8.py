###########################################################
# @author: barbarafonseca95@gmail.com                     #
# @description: Script que retorna o print de todos os    #
# números pares até o número escolhido                    # 
# @date: 23/02/2022                                       #
###########################################################

#calcular em quanto tempo o país A ultrapassará a população do país B

A = 80000
B = 200000
anos = 0

while A < B:
	A = A + A * 0.03
	B = B + B * 0.015
	anos = anos + 1
else:
	print(f'O país A ultrapassará o B em {anos} anos')
