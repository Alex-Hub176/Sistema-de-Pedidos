from utils.database import conectar
from utils.validacoes import ler_preco
from sqlite3 import IntegrityError, OperationalError, Error

def adicionar(id_pedido):
    nome_produto = str(input("Nome do produto: ")).strip()
    qtd = int(input("Quantidade de produtos: "))
    preco = ler_preco()

    query = ('INSERt INTO itens_pedido(pedido_id,produto,quantidade,preco) VALUES (?,?,?,?)')
    with conectar() as con:

        try: 

            cur = con.cursor()
            cur.execute(query,(id_pedido,nome_produto,qtd,preco,))
            con.commit() 

        except IntegrityError:
            print("Os dados informados violam uma regra do banco.")
        except OperationalError:
            print("Erro ao acessar o banco de dados.")
        except Error as erro:
            print(f"Erro SQLite {erro}")


