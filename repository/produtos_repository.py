from repository.repository_base import RepositoryBase
from models.produtos import Produtos
from database.conexao import conectar

class ProdutoRepository(RepositoryBase):

    def inserir(self, produtos: Produtos, cursor=None):
        script = "INSERT INTO produtos (nome, preco, estoque) VALUES (%s,%s,%s)"
        valores = (produtos.nome_produto, produtos.preco, produtos.qtd)

        if cursor is not None:
            cursor.execute(script, valores)

        with conectar() as conexao:
            cursor_local = conexao.cursor()
            cursor_local.execute(script, valores)


    def atualizar(self, campo, id, novo_valor):
        query = f"UPDATE produtos SET {campo} = %s WHERE id = %s RETURNING id, nome, estoque"
        with conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute(query, (novo_valor, id))
            return cursor.fetchone() is not None

    def deletar(self, id):
        with conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute("DELETE FROM produtos WHERE id = %s", (id,))
            return cursor.rowcount

    def consultar(self, id):
        with conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM produtos WHERE id = %s", (id,))
            return cursor.fetchall()

        
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