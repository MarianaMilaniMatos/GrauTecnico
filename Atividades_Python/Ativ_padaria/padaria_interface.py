import tkinter as tk
from tkinter import messagebox

# Preços dos pães
precos = {
    "Pão Francês": 1.04,
    "Pão Integral": 1.04,
    "Pão Doce Liso": 1.08,
    "Pão Doce Farofa": 1.11,
    "Pão de Forma": 0.95
}

# Quantidades e valores acumulados
quantidades = {
    "Pão Francês": 0,
    "Pão Integral": 0,
    "Pão Doce Liso": 0,
    "Pão Doce Farofa": 0,
    "Pão de Forma": 0
}

# Variável para armazenar o tipo de pão selecionado
tipo_selecionado = ""

# Função para adicionar pão
def adicionar_pao():
    global tipo_selecionado
    if tipo_selecionado:
        try:
            qtd = int(entrada_qtd.get())
            if qtd <= 0:
                raise ValueError
            quantidades[tipo_selecionado] += qtd
            atualizar_resumo()
            entrada_qtd.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Erro", "Digite uma quantidade válida (número positivo).")
    else:
        messagebox.showerror("Erro", "Selecione um tipo de pão primeiro.")

# Função para atualizar o resumo da compra
def atualizar_resumo():
    texto_resumo.delete("1.0", tk.END)
    total = 0
    total_itens = 0
    for tipo, qtd in quantidades.items():
        if qtd > 0:
            valor = qtd * precos[tipo]
            texto_resumo.insert(tk.END, f"{tipo}: {qtd} x R$ {precos[tipo]:.2f} = R$ {valor:.2f}\n")
            total += valor
            total_itens += qtd
    texto_resumo.insert(tk.END, f"\nTotal de itens: {total_itens}")
    texto_resumo.insert(tk.END, f"\nTotal da compra: R$ {total:.2f}")

# Função para selecionar o tipo de pão
def selecionar_tipo_pao(tipo):
    global tipo_selecionado
    tipo_selecionado = tipo
    label_tipo_selecionado.config(text=f"Tipo de pão selecionado: {tipo}")

# Função para finalizar a compra
def finalizar_compra():
    messagebox.showinfo("Compra Finalizada", "Obrigado pela compra!")
    janela.destroy()

# Janela principal
janela = tk.Tk()
janela.title("Sistema da Padaria")

# Label para exibir tipo de pão selecionado
label_tipo_selecionado = tk.Label(janela, text="Tipo de pão selecionado: Nenhum")
label_tipo_selecionado.grid(row=0, column=0, columnspan=2)

# Botões para cada tipo de pão
tipos_pao = list(precos.keys())
for i, tipo in enumerate(tipos_pao):
    tk.Button(janela, text=tipo, width=20, command=lambda t=tipo: selecionar_tipo_pao(t)).grid(row=i+1, column=0, columnspan=2, pady=2)

# Entrada de quantidade
tk.Label(janela, text="Quantidade:").grid(row=len(tipos_pao)+1, column=0)
entrada_qtd = tk.Entry(janela)
entrada_qtd.grid(row=len(tipos_pao)+1, column=1)

# Botão Adicionar
tk.Button(janela, text="Adicionar ao carrinho", width=20, command=adicionar_pao).grid(row=len(tipos_pao)+2, column=0, columnspan=2, pady=10)

# Área de resumo
tk.Label(janela, text="Resumo da compra:").grid(row=len(tipos_pao)+3, column=0, columnspan=2)
texto_resumo = tk.Text(janela, height=10, width=40)
texto_resumo.grid(row=len(tipos_pao)+4, column=0, columnspan=2)

# Botão de finalizar
tk.Button(janela, text="Finalizar Compra", bg="green", fg="white", command=finalizar_compra).grid(row=len(tipos_pao)+5, column=0, columnspan=2, pady=10)

# Inicia a interface
janela.mainloop()


