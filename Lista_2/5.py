###########################################################
# @author: barbarafonseca95@gmail.com                     #
# @description: Script que retorna a média dos valores    #
# inseridos até o valor de pausa ser inserido, o zero     # 
# @date: 03/03/2022                                       #
###########################################################

#média de valores inseridos até a pausa, o zero
soma = 0
count = 0
while True:
	x = int(
		input('n (zero sai): ')
	)
	if x == 0:
		break
	soma = soma+x
	count = count+1

avg = soma/count

print(avg)

