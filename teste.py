from repository.pedidos_repository import PedidoRepository
from models.pedidos import Pedidos

repo = PedidoRepository()
#pro1 = Pedidos(1, 'pendente')
print(repo.consultar(3))
