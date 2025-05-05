import os
os.system("clear")

matricula = input("Digite a sua matrícula: ")
senha = int(input("Digite sua senha: "))
salario = float(input("Digite o seu sálario: "))
acrescimo_refeicao = 0

vale_refeicao = int(input("Digite o valor do vale refeição: "))
def vale_refeicao_recebido():
    acrescimo_refeicao = salario * 0.20
    return vale_refeicao

vale_transporte = input("Deseja receber vale transporte? Digite 'S' para sim 'N' para não:")
match vale_transporte:
        case "s":
         acrescimo_transporte = salario * 0.06
        case "n":
               print()     
dependentes = int(input("Informe a quantidade de dependentes: "))
def calcular_plano_saude(dependentes):
    return dependentes * 150.00
def calcular_inss(salario):
    match salario:
        case _ if salario <= 1518.00:
            return salario * 0.075
        case _ if salario <= 2793.88:
            return salario * 0.09 - 113.85
        case _ if salario <= 4190.83:
            return salario * 0.12 - 189.54
        case _ if salario <= 8157.41:
            return salario * 0.14 - 318.38
        case _:
            return 1142.04
    	
def calcular_irrf(salario, dependentes):
    base_calculo = salario - (189.59 * dependentes)
    match base_calculo:
        case _ if base_calculo <= 2259.20:
            return 0  
        case _ if base_calculo <= 2826.65:
            return base_calculo * 0.075 - 169.44
        case _ if base_calculo <= 3751.05:
            return base_calculo * 0.15 - 381.44
        case _ if base_calculo <= 4664.68:
            return base_calculo * 0.22 - 662.77
        case _:
            return base_calculo * 0.275 - 896.00
	
def calcular_salario_liquido(salario_base, dependentes, vale_transporte, vale_refeicao):
    calcular_inss = calcular_inss(salario_base)
    calcular_irrf = calcular_irrf(salario_base, dependentes)
    vale_transporte = vale_transporte(salario_base, vale_transporte)
    vale_refeicao_recebido = vale_refeicao_recebido(vale_refeicao)
    desconto_plano_saude = calcular_plano_saude(dependentes)

    salario = salario_liquido - (calcular_inss + calcular_irrf + vale_transporte + vale_refeicao_recebido + desconto_plano_saude)
    return salario_liquido

salario_liquido = calcular_salario_liquido(salario, dependentes, vale_transporte, vale_refeicao)

print(f"Matricula: {matricula}")
print(f"Senha: {senha}")
print(f"Sálario Líquido: {salario}")
print(f"Vale Refeição: {vale_refeicao}")
print(f"Dependentes: {dependentes}")
print(f"Vale Transporte: {vale_transporte}")
print(f"Sálario Total: {salario_liquido}")
