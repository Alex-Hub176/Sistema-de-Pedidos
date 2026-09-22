class PedidosItens:
    def __init__(self, pedido_id, produto_id, qtd, preco_unitario):
        self.pedido_id = pedido_id
        self.produto_id = produto_id
        self.quantidade = qtd
        self.preco_unitario = preco_unitario
        