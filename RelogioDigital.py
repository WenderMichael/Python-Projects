from tkinter import *
from time import strftime
import Menu

def executar():
# Função para atualizar o relógio
    def atualizar_relogio():
        horario_atual = strftime("%H:%M:%S %p")
        rotulo_relogio.config(text=horario_atual)
        rotulo_relogio.after(1000,atualizar_relogio)

    def voltar_menu():
        janela.destroy()
        Menu.escolher_jogo()

    # Criando da janela principal
    janela = Tk()
    janela.title("Relógio Digital Simples")

    # Criação do rótulo para exibir o relógio
    rotulo_relogio = Label(
        janela,
        font=("Arial", 40, "bold"),
        background="light green",
        foreground="white"
    )

    rotulo_relogio.grid(column=1, row=0)

    botao = Button(janela, text="Voltar ao menu", command=voltar_menu)
    botao.grid(column=1, row=2)

    # Inicia a atualização do relógio
    atualizar_relogio()

    # Inicia o loop principal da interface gráfica
    janela.mainloop()
if(__name__ == "__main__"):
    executar()