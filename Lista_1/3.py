###########################################################
# @author: barbarafonseca95@gmail.com                     #
# @description: Script para calcular o salário bruto,     #
# os impostos(IR, INSS e Sindicato) e o salário líquido   # 
# @date: 23/02/2022                                       #
###########################################################

# 1. Receber o valor da hora e quantidade de horas trabalhadas
hora = int(
    input("Valor da hora(em reais): ")
)
horas_trabalhadas = int(
    input("Horas trabalhadas no mês: ")
)
# 2. Calcular o salário bruto
salário_bruto = hora*horas_trabalhadas

# 3. Calcular os impostos e o salário líquido
IR = salário_bruto*0.11
INSS = salário_bruto*0.08
Sindicato = salário_bruto*0.05
Salário_líquido = int(salário_bruto-IR-INSS-Sindicato)

# 4. Exibir os resultados
print(f"Salário bruto: {salário_bruto} reais")
print(f"IR(11%): {IR} reais")
print(f"INSS(8%): {INSS} reais")
print(f"Sindicato(5%): {Sindicato} reais")
print(f"Salário Líquido: {Salário_líquido} reais")
