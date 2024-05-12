import calculadora
import CalcularINSS
import RelogioDigital

def escolher_jogo():
    print("*********************************")
    print("******* ESCOLHA O PROJETO *******")
    print("*********************************")

    print("(1) Calculadora")
    print("(2) Calcular INSS")
    print("(3) Relogio Digital")

    projeto = int(input("Qual projeto? "))

    if (projeto == 1):
        print("Abrindo Calculadora...")
        calculadora.executar()
    elif (projeto == 2):
        print("Abrindo Calcular NSS...")
        CalcularINSS.executar()
    elif (projeto == 3):
        print("Abrindo Relogio digital...")
        RelogioDigital.executar()

if(__name__ == "__main__"):
    escolher_jogo()
