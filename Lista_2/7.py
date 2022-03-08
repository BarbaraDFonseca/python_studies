###############################################################
# @author: barbarafonseca95@gmail.com                         #
# @description: Script que verifica se senha e usuário são    #
# iguais, se sim indica o erro e solicita os dados novamente  # 
# @date: 03/03/2022                                           #
###############################################################

import getpass

while True:
	user = input("Usuário: ")
	password = getpass.getpass("Senha: ")
	if user != password:
		print("Cadastro Realizado")
		break
	print("Dados recusados, a senha não deve ser igual ao usuário")
