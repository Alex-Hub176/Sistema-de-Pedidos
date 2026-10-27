from models.pedidos import Pedidos
from repository.repository_base import RepositoryBase
from database.conexao import conectar

class PedidoRepository(RepositoryBase):

    def inserir(self, pedidos: Pedidos, cursor=None):
        script = "INSERT INTO pedidos (usuario_id, status) VALUES (%s, %s) RETURNING id"
        valores = (pedidos.usuario_id, pedidos.status)

        if cursor is not None:
            cursor.execute(script,valores)
            return cursor.fetchone[0]

        with conectar() as conexao:
            cursor_local = conexao.cursor()
            cursor_local.execute(script, valores)
            return cursor_local.fetchone()[0]


    def atualizar(self, campo, id, valor):
        query = f"UPDATE pedidos SET {campo} = %s WHERE id = %s"
        with conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute(query,(valor, id))


    def deletar(self, id):
        with conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute("DELETE FROM pedidos WHERE id = %s", (id,))

    def consultar(self, id):
        with conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM pedidos WHERE id = %s", (id,))
            return cursor.fetchall()