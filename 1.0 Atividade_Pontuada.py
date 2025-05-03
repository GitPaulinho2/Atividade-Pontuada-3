import os
os.system("clear")

matricula = input("Digite a sua matrícula: ")
senha = int(input("Digite sua senha: "))
salario = float(input("Digite o seu sálario: "))

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
def calcular_inss(salario):
    if salario <= 1518.08:
         return salario * 0.075
    elif salario <= 2793.88:
         return salario * 0.09
    elif salario <= 4190.83:
         return salario * 0.12
    elif salario <= 8157.41:
         return salario * 0.14	
    
def calcular_irrf(salario):
      if salario <= 2259.21:
        return salario * 0.075
      elif salario <= 2826.65:
        return salario * 0.09
      elif salario <= 4190.83:
        return salario * 0.12
      elif salario <= 8157.41:
        return salario * 0.14	

print(f"Matricula: {matricula}")
print(f"Senha: {senha}")
print(f"Sálario Líquido: {salario}")
print(f"Vale Refeição: {vale_refeicao}")
print(f"Dependentes: {dependentes}")
print(f"Vale Transporte: {vale_transporte}")
