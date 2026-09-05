from abc import ABC
class Usuario(ABC):    
    def __init__(self, id=None, nome=str, email=str, telefone=int):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone

