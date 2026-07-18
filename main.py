import utils
from datetime import datetime

print("Cadastrar usuario e pedido")
# Pegando o id gerado ao adicionar o novo usuario
id_usuario = utils.cadastros.cadastra_usuario()

# # # pegando o id do pedido criado do novo usuario
pedido_id = utils.pedido.criar_pedido(id_usuario)

# # # colocando o id do pedido criado para identificar de quem os itens adicionados
utils.adicionar_produto.adicionar(pedido_id)

# visualização das informações
mostrar = utils.listar_produtos.listar_pedido()
print(mostrar)
            
