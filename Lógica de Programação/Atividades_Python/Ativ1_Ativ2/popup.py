import tkinter as tk
from tkinter import simpledialog, messagebox

# Criar janela invisível principal
janela = tk.Tk()
janela.withdraw()  # Oculta a janela principal

# Pedir número ao usuário
numero = simpledialog.askinteger("Tabuada", "Digite um número:")

# Montar o texto da tabuada
mensagem = ""
for i in range(11):
    mensagem += f"{numero} x {i} = {numero * i}\n"

# Exibir em pop-up
messagebox.showinfo("Tabuada do " + str(numero), mensagem)
