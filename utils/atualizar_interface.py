from utils.listar_produtos import listar_pedido
from tkinter import ttk

def atualizar_treeview(treeview):
    for item in treeview.get_children():
        treeview.delete(item)

    pedidos = listar_pedido()

    if pedidos:
        for pedido in pedidos:
            treeview.insert("", "end", value=pedido)