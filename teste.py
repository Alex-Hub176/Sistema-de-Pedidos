from repository import *

from models import *

#user1 = Usuario(None, "Luan", "luan@gmail.com", "123342333")
#repo_usu = UsuarioRepository()
#usuario_id = repo_usu.inserir(user1)

#pedido1 = Pedidos(usuario_id, 'pendente')
#repo_pedido = PedidoRepository()
#pedido_id = repo_pedido.inserir(pedido1)

#repo_produtos = ProdutoRepository()

pedido_item1 = PedidosItens(3, 2, 2, 69)
repo_pedido_itens = PedidoItensRepository()
repo_pedido_itens.inserir(pedido_item1)

print(repo_pedido_itens.consultar())
