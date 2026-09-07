from abc import ABC, abstractmethod

class RepositoryBase(ABC):
    @abstractmethod
    def inserir(self):
        pass

    @abstractmethod
    def atualizar(self, campo, id, valor):
        pass

    @abstractmethod
    def deletar(self, id):
        pass

    @abstractmethod
    def consultar(self, id):
        pass