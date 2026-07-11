from utils.database import conectar


def listar_pedido():
    query = ('''
            SELECT usuarios.nome, pedidos.id, itens_pedido.produto, itens_pedido.quantidade, SUM(itens_pedido.quantidade * itens_pedido.preco) AS total
            
            FROM usuarios

            JOIN pedidos 
            ON usuarios.id = pedidos.usuario_id
            JOIN itens_pedido 
            ON pedidos.id = itens_pedido.pedido_id
               
            GROUP BY
            usuarios.nome, pedidos.id, itens_pedido.produto, itens_pedido.quantidade

               ''')
    
    with conectar() as con:
        cur = con.cursor()
        cur.execute(query)


    todos_dados = cur.fetchall()
    return todos_dados
    


def mostrar_nome(id):
    query = ('SELECT nome FROM usuarios WHERE id = (?)')
    
    with conectar() as con:
        cur = con.cursor()
        cur.execute(query,(id,))

        nomes = cur.fetchone()

        return nomes[0]

    