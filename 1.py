###########################################################
# @author: barbarafonseca95@gmail.com                     #
# @description: Script para determinar se os 3 números    #
# podem formar um triângulo e qual é o seu tipo           # 
# @date: 23/02/2022                                       #
###########################################################

# 1. Receber os números
lado_1 = int(
    input("Digite um número: ")
)

lado_2 = int(
    input("Digite um número: ")
)
lado_3 = int(
    input("Digite um número: ")
)

# 2. Verificar se é um triângulo, o seu tipo e exibir o resultado
if lado_1 + lado_2 > lado_3 and lado_1 + lado_3 > lado_2 and lado_2 + lado_3>lado_1:
    if lado_1 != lado_2 and lado_2 != lado_3 and lado_1 != lado_3:
        print('É um Triângulo Escaleno')
    elif lado_1 == lado_2 == lado_3:
        print('É um Triangulo Equilátero')
    elif lado_1 == lado_2 or lado_2 == lado_3 or lado_1 == lado_3:
        print('É um Triângulo Isósceles')
else: print('Não é um triângulo')