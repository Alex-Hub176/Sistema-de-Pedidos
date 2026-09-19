from models.pedidos import Pedidos
from repository.repository_base import RepositoryBase
from database.conexao import conectar

class PedidoRepository(RepositoryBase):

    def inserir(self, pedidos: Pedidos):
        with conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute("INSERT INTO pedidos (usuario_id, status) VALUES (%s, %s)", (pedidos.usuario_id, pedidos.status))
            conexao.commit()

    def atualizar(self, campo, id, valor):
        query = f"UPDATE SET pedidos {campo} = %s WHERE id = %s"
        with conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute(query,(valor, id))
            conexao.commit()


    def deletar(self, id):
        with conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute("DETELE FROM pedidos WHERE id = %s", (id,))
            conexao.commit()

    def consultar(self, id):
        with conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM pedidos WHERE id = %s", (id,))
            pedido = cursor.fetchall()
            return pedido