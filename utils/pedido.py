from utils.database import conectar
from utils.listar_produtos import mostrar_nome
from datetime import datetime
from sqlite3 import IntegrityError, OperationalError, Error

def criar_pedido(id_usuario):
    escolha = str(input(f"Adicionar pedido para {mostrar_nome(id_usuario)}? (s/n): ")).strip().lower()[0]

    if escolha == 's':
        data_atual = datetime.now()

        query = ('INSERT INTO pedidos(usuario_id, data_pedido) VALUES (?,?)')
        with conectar() as con:
            try:
                cur = con.cursor()
                cur.execute(query,(id_usuario,data_atual,))
                pedido_id = cur.lastrowid
                con.commit()
                return pedido_id

            except IntegrityError:
                print("Os dados informados violam uma regra do bando.")
            except OperationalError:
                print("Erro ao acessar o banco de dados.")
            except Error as erro:
                print(f"Erro SQLite {erro}")

            

