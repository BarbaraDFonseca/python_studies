###########################################################
# @author: barbarafonseca95@gmail.com                     #
# @description: Script que calcula o fatorial de x^n      # 
# @date: 03/03/2022                                       #
###########################################################

n = 1
fat = 1
x = int(
		input(f'n: ')
	)
while n<=x:
	fat = fat * n
	n = n + 1

print(f'fat({n}): {fat:.1f}')