from database.conexao import conectar
from models.pedidos import Pedidos
from models.pedido_itens import PedidosItens
from repository.pedidos_itens_repository import PedidoItensRepository
from repository.produtos_repository import ProdutoRepository
from repository.pedidos_repository import PedidoRepository
from utils.validacoes import *

class PedidoService:
    CAMPOS_PERMITIDOS = ["usuario_id", "status"]

    def __init__(self):
        self.pedido_repository = PedidoRepository()
        self.itens_repository = PedidoItensRepository()
        self.produto_repository = ProdutoRepository()

    def criar_pedidos(self, usuario_id, itens):
        validar_id(usuario_id)

        if not isinstance(itens, list) or len(itens) == 0:
            raise ValueError("O pedido precisa ter pelo menos um item.")

        with conectar as conexao:
            cursor = conexao.cursor()
            novo_pedido = Pedidos(usuario_id, "pendente")

            pedido_id = self.pedido_repository.inserir(novo_pedido, cursor)

            for produto_id, quantidade in itens:
                validar_id(produto_id)
                validar_quantidade_item(quantidade)

                preco = self.produto_repository.consultar_preco(produto_id, cursor)

                if preco is None:
                    raise ValueError(f"Produto {produto_id} não encontrado.")

                item = PedidosItens(pedido_id, produto_id, quantidade, preco)
                self.itens_repository.inserir(item, cursor)
                
        return pedido_id


    def atualizar_status(self, id, novo_status):
        validar_id(id)
        validar_status(novo_status)

        self.pedido_repository.atualizar("status", id, novo_status)


    def deletar_pedido(self, id):
        validar_id(id)
        self.pedido_repository.deletar(id)


    def consultar_pedidos(self, id):
        validar_id(id)
        return self.pedido_repository.consultar(id)
