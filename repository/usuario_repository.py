from models.usuarios import Usuario
from database.conexao import conectar

class UsuarioRepository(Usuario):
    CAMPOS_PERMITIDOS = ["id" ,"nome", "email", "telefone"]
    
   
    def inserir(self, usuario: Usuario):
        with conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute("INSERT INTO usuarios (nome, email, telefone) VALUES (?,?,?)", (self.nome, self.email, self.telefone))
            conexao.commit()

    def atualizar(self, id, campo, novo_valor):
        if campo not in self.CAMPOS_PERMITIDOS:
            print("Campo inválido")
            return
        
        query = f"UPDATE usuario SET {campo} = ? WHERE id = ?"
        with conectar as conexao:
            cursor = conexao.cursor()
            cursor.execute(query, (novo_valor, id))
            conexao.commit()

        def deletar(self, campo, id,):
            pass
