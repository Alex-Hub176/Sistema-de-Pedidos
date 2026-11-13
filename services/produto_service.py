from models.produtos import Produtos
from repository.produtos_repository import ProdutoRepository
from utils.validacoes import *
from database.conexao import conectar
from utils.erros import tratar_erros_db

class ProdutoService:
    CAMPOS_PERMITIDOS = ["nome", "preco", "estoque"]

    def __init__(self):
        self.produto_repository = ProdutoRepository()
    @tratar_erros_db
    def inserir_produto(self, nome_produto, preco, estoque):
        validar_nome(nome_produto)
        validar_preco(preco)
        validar_quantidade(estoque)

        with conectar() as conexao:
            cursor = conexao.cursor()
            novo_produto = Produtos(nome_produto, preco, estoque)
        self.produto_repository.inserir(novo_produto, cursor)


    @tratar_erros_db
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

        produto_atualizado = self.produto_repository.atualizar(campo, id, novo_valor)

        if produto_atualizado == False:
            raise ValueError("Produto não existe")
        return produto_atualizado

        
    @tratar_erros_db
    def deletar_produto(self, id):
        validar_id(id)
        produto_apagado = self.produto_repository.deletar(id)
        if produto_apagado == 0:
            raise ValueError("Produto não encotrado")
        return produto_apagado


    @tratar_erros_db
    def consultar_produto(self, id):
        validar_id(id)
        return self.produto_repository.consultar(id)
