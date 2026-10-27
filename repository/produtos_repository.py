from repository.repository_base import RepositoryBase
from models.produtos import Produtos
from database.conexao import conectar

class ProdutoRepository(RepositoryBase):

    def inserir(self, produtos: Produtos):
        with conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute("INSERT INTO produtos (nome, preco, estoque) VALUES (%s,%s,%s)",  (produtos.nome_produto, produtos.preco, produtos.qtd))
            conexao.commit()

    def atualizar(self, campo, id, novo_valor):
        query = f"UPDATE produtos SET {campo} = %s WHERE id = %s"
        with conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute(query, (novo_valor, id))
            conexao.commit()

    def deletar(self, id):
        with conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute("DELETE FROM produtos WHERE id = %s", (id,))
            conexao.commit()

    def consultar(self, id):
        with conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM produtos WHERE id = %s", (id,))
            produto = cursor.fetchall()
            
        return produto

    def consultar_preco(self, id, cursor=None):
        query = "SELECT preco FROM produtos WHERE id = %s"

        if cursor is not None:
            cursor.execute(query, (id,))
            linha = cursor.fetchone()

        else:
            with conectar() as conexao:
                cursor_local = conexao.cursor()
                cursor_local.execute(query, (id,))
                linha = cursor_local.fetchone()

        if linha is None:
            return None

        return linha[0]