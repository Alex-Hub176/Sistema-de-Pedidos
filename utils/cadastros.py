from utils.database import conectar
from utils.validacoes import ler_email
from sqlite3 import OperationalError, IntegrityError, Error

def cadastra_usuario():
    nome = str(input("Nome: ")).strip()
    email = ler_email()
    query = ('INSERT INTO usuarios(nome,email) VALUES (?,?)')
    
    with conectar() as conexao:
        try:
            cursor = conexao.cursor()   
            cursor.execute(query,(nome,email,))
            id_usuario = cursor.lastrowid
            conexao.commit()
            return id_usuario
        
        except IntegrityError:
            print("Os dados informados violam uma regra do banco.")
        except OperationalError:
            print("Erro ao acessar o banco de dados.")
        except Error as erro:
            print(f"Erro SQLite {erro}")

        



    



