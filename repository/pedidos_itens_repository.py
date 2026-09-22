from models.pedido_itens import PedidosItens
from repository.repository_base import RepositoryBase
from database.conexao import conectar


class PedidoItensRepository(RepositoryBase):

    def inserir(self, pedido_itens: PedidosItens):
        with conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute(
                "INSERT INTO pedido_itens (pedido_id, produto_id, quantidade, preco_unitario) VALUES (%s,%s,%s,%s)", (pedido_itens.pedido_id, pedido_itens.produto_id, pedido_itens.quantidade, pedido_itens.preco_unitario)
            )
            conexao.commit()

    def atualizar(self, campo, id, valor):
        query = f"UPDATE pedido_itens SET {campo} = %s WHERE id = %s"
        with conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute(query, (valor, id))
            conexao.commit()

    def deletar(self, id):
        with conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute("DETELE FROM pedido_itens WHERE id = %s", (id,))
            conexao.commit()

    def consultar(self, id):
        with conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM pedido_itens WHERE id = %s", (id,))
        