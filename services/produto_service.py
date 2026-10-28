from models.produtos import Produtos
from repository.produtos_repository import ProdutoRepository
from utils.validacoes import *

class ProdutoService:
    CAMPOS_PERMITIDOS = ["nome", "preco", "estoque"]

    def __init__(self):
        self.produto_repository = ProdutoRepository()

    def inserir_produto(self, nome_produto, preco, estoque):
        validar_nome(nome_produto)
        validar_preco(preco)
        validar_quantidade(estoque)

        novo_produto = Produtos(nome_produto, preco, estoque)
        self.produto_repository.inserir(novo_produto)

    def atualizar_produto(self, id, campo, novo_valor):
        if campo not in ProdutoService.CAMPOS_PERMITIDOS:
            raise AttributeError("Campo inválido")

        if campo == "nome":
            validar_nome(novo_valor)
        elif campo == "preco":
            validar_preco(novo_valor)
        elif campo == "estoque":
            validar_quantidade(novo_valor)
        validar_id(id)

        self.produto_repository.atualizar(campo, id, novo_valor)
        

    def deletar_produto(self, id):
        validar_id(id)
        self.produto_repository.deletar(id)

    def consultar_produto(self, id):
        validar_id(id)
        return self.produto_repository.consultar(id)
