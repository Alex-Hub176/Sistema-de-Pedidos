from utils.database import conectar

def adicionar(id_pedido):
    nome_produto = str(input("Nome do produto: ")).strip()
    qtd = str(input("Quantidade de produtos: ")).strip()
    preco = float(input("Preço do produto: "))

    query = ('INSERT INTO itens_pedido(pedido_id,produto,quantidade,preco) VALUES (?,?,?,?)')
    with conectar() as con:
        cur = con.cursor()
        cur.execute(query,(id_pedido,nome_produto,qtd,preco,))

        con.commit()


