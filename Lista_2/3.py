###########################################################
# @author: barbarafonseca95@gmail.com                     #
# @description: Script que gera a média dos números       #
# inseridos, contando que sejam 10 valores                # 
# @date: 03/03/2022                                       #
###########################################################

n = 1
sum = 0

while n<=10:
	x = int(
		input(f'{n} número: ')
	)

	sum = sum + x
	n = n + 1
avg = sum/x	
print(f'Média: {avg:.1f}')

