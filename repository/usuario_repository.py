from models.usuarios import Usuario
from database.conexao import conectar
from repository.repository_base import RepositoryBase

class UsuarioRepository(RepositoryBase):

    def inserir(self, usuario: Usuario, cursor=None):
        script = "INSERT INTO usuarios (nome, email, telefone) VALUES (%s,%s,%s) RETURNING id"
        valores = (usuario.nome, usuario.email, usuario.telefone)

        if cursor is not None:
            cursor.execute(script, valores)
            return cursor.fetchone()[0]

        with conectar() as conexao:
            cursor_local = conexao.cursor()
            cursor_local.execute(script, valores)
            return cursor_local.fetchone()[0]

            
    def atualizar(self, id, campo, novo_valor):
        query = f"UPDATE usuarios SET {campo} = %s WHERE id = %s RETURNING id"
        with conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute(query, (novo_valor, id))
            return cursor.fetchone() is not None
        

    def deletar(self, id):
        with conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute("DELETE FROM usuarios WHERE id = %s", (id,))
            return cursor.rowcount
            

    def consultar(self, id):
        with conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE id = %s", (id,))
        return cursor.fetchall()
        