###########################################################
# @author: barbarafonseca95@gmail.com                     #
# @description: Script para calcular a quantidade de      #
# latas de tinta para pintar um cômodo e seu preço        # 
# @date: 23/02/2022                                       #
###########################################################

# 1. Importar módulo da biblioteca
from math import ceil

# 2. Receber a área do cômodo
área = int(input("área do cômodo: "))

# 3. Calcular a quantidade de litros necessária
litros = área/3

# 4. Calcular a quantidade de latas necessária
qtd_latas = ceil(litros/18)

# 5. Calcular o preço final
preço = qtd_latas*80

# 6. Exibir o resultado
print(f'Você precisará de {qtd_latas} latas de tinta')
print(f'Preço: {preço} reais')