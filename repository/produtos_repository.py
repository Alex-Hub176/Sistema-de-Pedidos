from repository.repository_base import RepositoryBase
from models.produtos import Produtos
from database.conexao import conectar

class ProdutoRepository(RepositoryBase):

    def inserir(self, produtos: Produtos):
        with conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute("INSERT INTO produtos (nome, preco, quantidade) VALUES (%s,%s,%s)",  (produtos.nome_produto, produtos.preco, produtos.qtd))
            conexao.commit()

    def atualizar(self, id, campo, novo_valor):
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