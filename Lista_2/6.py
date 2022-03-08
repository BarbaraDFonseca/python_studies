#########################################################################
# @author: barbarafonseca95@gmail.com                                   #
# @description: Script que recebe um valor inteiro como nota, verifica  #
# se está entre 0 e 10, caso não esteja é solicitada uma nova nota até  # 
# atender o critério e entregar o resultado da nota                     #
# @date: 03/03/2022                                                     #
#########################################################################

while True:
	nota = float(
		input("Nota: ")
	)
	if nota <= 10 and nota >=0:
		print(f"Sua nota é: {nota}")
		break
	print("Escolha uma nota entre 0 e 10")


