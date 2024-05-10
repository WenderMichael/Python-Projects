def executar():
    print("----------------------------------------------")
    print("Bem vindo ao Calcular INSS!")
    print("----------------------------------------------")

    salario = float(input("Digite o valor do salário: "))

    if salario <= 1302.00:
        inss = salario * 0.075
    elif salario <= 2571.29:
        inss = salario * 0.09
    elif salario <= 3856.94:
        inss = salario * 0.12
    elif salario <= 7507.49:
        inss = salario * 0.14
    else:
        inss = 1051.04

    liquido = salario - inss

    print("Salário: {:.2f} INSS: {:.2f} Salário Líquido: {:.2f}".format(salario, inss, liquido))
if(__name__ == "__main__"):
    executar()