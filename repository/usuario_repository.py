from models.usuarios import Usuario
from database.conexao import conectar
from repository.repository_base import RepositoryBase

class UsuarioRepository(RepositoryBase):
    CAMPOS_PERMITIDOS = ["id" ,"nome", "email", "telefone"]
    
   
    def inserir(self, usuario: Usuario):
        with conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute("INSERT INTO usuarios (nome, email, telefone) VALUES (%s,%s,%s)", (usuario.nome, usuario.email, usuario.telefone))
            conexao.commit()

    def atualizar(self, id, campo, novo_valor):
        if campo not in UsuarioRepository.CAMPOS_PERMITIDOS:
            print("Campo inválido")
            return
        
        query = f"UPDATE usuarios SET {campo} = %s WHERE id = %s"
        with conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute(query, (novo_valor, id))
            conexao.commit()

    def deletar(self, id):
        with conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute("DELETE FROM usuarios WHERE id = %s", (id,))
            conexao.commit()

    def consultar(self, id):
        with conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE id = %s", (id,))
            user = cursor.fetchall()
            print(user)