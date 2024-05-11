def executar():
      print("----------------------------------------------")

      print("Bem vindo a calculadora")

      print("----------------------------------------------")

      valor1_str = input("Digite seu primero valor: ")
      valor1 = float(valor1_str)
      valor2_str = input("Digite seu segundo valor: ")
      valor2 = float(valor2_str)

      print("----------------------------------------------")

      print("1. Adição (+)")
      print("2. Subtração (-)")
      print("3. Multiplicação (*)")
      print("4. Divisão (/)")

      print("----------------------------------------------")

      tipo_de_operacao_str = input("Digite o numero respectivo a sua operação: ")
      tipo_de_operacao = int(tipo_de_operacao_str)

      if(tipo_de_operacao == 1):
            valor_total = valor1 + valor2
      elif(tipo_de_operacao == 2):
            valor_total = valor1 - valor2
      elif(tipo_de_operacao == 3):
            valor_total = valor1 * valor2
      elif(tipo_de_operacao == 4):
            valor_total = valor1 / valor2
      else:
            print("Valor invalido.")

      print("----------------------------------------------")

      print("RESULTADO = ", valor_total)

      print("----------------------------------------------")

if(__name__ == "__main__"):
    executar()