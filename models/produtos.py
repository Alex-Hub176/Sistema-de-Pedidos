class Produtos():
    def __init__(self, pedido_id: int, produto: str, preco: int, qtd: int):
        self.pedido_id = pedido_id
        self.produto = produto
        self.preco = preco
        self.qtd = qtd