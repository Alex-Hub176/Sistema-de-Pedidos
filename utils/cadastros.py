from utils.database import conectar


def cadastra_usuario():
    nome = str(input("Nome: ")).strip()
    email = str(input("Email: ")).strip()
    query = ('INSERT INTO usuarios(nome,email) VALUES (?,?)')
    
    with conectar() as conexao:
        cursor = conexao.cursor()
        cursor.execute(query,(nome,email,))
        id_usuario = cursor.lastrowid
        
        conexao.commit()
        
    return id_usuario



    



