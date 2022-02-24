###########################################################
# @author: barbarafonseca95@gmail.com                     #
# @description: Script para verificar se o peso do peixe  #
# excede o estabelecido pela fiscalização e calcular      # 
# a quantidade de kg excedida e a multa                   #
# @date: 23/02/2022                                       #
###########################################################

# 1. Receber o peso
peso = int(input('Peso do Peixe: '))

# 2. Verificar se o peso excede o estabelecido, calcular o excedente e a multa
if peso>50:
    excedente = peso-50
    multa = excedente*4
else:
    excedente = 0
    multa = 0
# 3. Exibir os resultados
print(
    f'O excedente é de {excedente} Kg e a multa é de {multa} reais'
)