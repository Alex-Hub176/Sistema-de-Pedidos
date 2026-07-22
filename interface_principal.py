import tkinter as tk
from tkinter import ttk
from utils.atualizar_interface import atualizar_treeview

def iniciar_sistema():
    janela = tk.Tk()
    janela.title("Projeto Portfólio - Sistema de Pedidos")
    janela.geometry("800x400")

    colunas = ("clientes", "id_pedido", "produto", "quantidade", "total")

    tabela = ttk.Treeview(janela, columns=colunas, show="headings")

    tabela.heading("clientes", text="Nome do cliente")
    tabela.heading("id_pedido", text="N° do pedido")
    tabela.heading("produto", text="Produto")
    tabela.heading("quantidade", text="Qtd")
    tabela.heading("total", text="Total Acumulado (R$)")

    tabela.column("clientes", width=150, anchor="w")
    tabela.column("id_pedido", width=80, anchor="center")
    tabela.column("produto", width=150, anchor="w")
    tabela.column("quantidade", width=70, anchor="center")
    tabela.column("total", width=120, anchor="center")

    tabela.pack(fill="both", expand=True, padx=10, pady=10)
    atualizar_treeview(tabela)

    janela.mainloop()
