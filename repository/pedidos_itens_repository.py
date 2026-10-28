from models.pedido_itens import PedidosItens
from repository.repository_base import RepositoryBase
from database.conexao import conectar

class PedidoItensRepository(RepositoryBase):

    def inserir(self, pedido_itens: PedidosItens, cursor=None):
        query = "INSERT INTO pedido_itens (pedido_id, produto_id, quantidade, preco_unitario) VALUES (%s,%s,%s,%s)"
        valores = (pedido_itens.pedido_id, pedido_itens.produto_id, pedido_itens.quantidade, pedido_itens.preco_unitario)

        if cursor is not None:
            cursor.execute(query, valores)
            return
    
        with conectar() as conexao:
            cursor_local = conexao.cursor()
            cursor_local.execute(query, valores)


    def atualizar(self, campo, id, valor):
        query = f"UPDATE pedido_itens SET {campo} = %s WHERE id = %s"
        with conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute(query, (valor, id))


    def deletar(self, id):
        with conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute("DELETE FROM pedido_itens WHERE id = %s", (id,))


    def consultar(self, id):
        with conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM pedido_itens WHERE id = %s", (id,))
            return cursor.fetchall()
        