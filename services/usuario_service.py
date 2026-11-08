from models.usuarios import Usuario
from repository.usuario_repository import UsuarioRepository
from utils.validacoes import *


class UsuarioService:
    CAMPOS_PERMITIDOS = ["nome", "email", "telefone"]

    def __init__(self):
        self.usuario_repository = UsuarioRepository()

    def cadastrar_usuario(self, nome, email, telefone):
        validar_nome(nome)
        validar_email(email)
        validar_telefone(telefone)

        novo_usuario = Usuario(None, nome, email, telefone)
        usuario_id = self.usuario_repository.inserir(novo_usuario)
        return usuario_id


    def atualizar_usuario(self, id, campo, novo_valor):
        if campo not in UsuarioService.CAMPOS_PERMITIDOS:
            raise AttributeError("Campo inválido")

        if campo == "telefone":
            validar_telefone(novo_valor)
        elif campo == "nome":
            validar_nome(novo_valor)
        elif campo == "email":
            validar_email(novo_valor)
        validar_id(id)
        id_usuario = self.usuario_repository.atualizar(id, campo, novo_valor)
        if id_usuario == False:
            raise ValueError("Usuário não existe")
        return id_usuario


    def deletar_usuario(self, id):
        validar_id(id)
        usuarios_apagados = self.usuario_repository.deletar(id)
        if usuarios_apagados == 0:
            raise ValueError("Usuário não encontrado")
        return usuarios_apagados

    
    def consutar_usuario(self,id):
        validar_id(id)
        return self.usuario_repository.consultar(id)
