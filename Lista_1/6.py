###########################################################
# @author: barbarafonseca95@gmail.com                     #
# @description: Script para mostrar o maior valor         #
# entre 3 números                                         # 
# @date: 23/02/2022                                       #
###########################################################

# 1. #Receber os números
a = int(input('Digite um número: '))
b = int(input('Digite um número: '))
c = int(input('Digite um número: '))

# 2. Verificar qual é o maior
maior = a

if b>maior:
    maior = b
if c>maior:
    maior = c

# 3. Exibir o resultado
print(f'O maior número é: {maior}')
