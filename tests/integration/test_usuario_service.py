from database.conexao import conectar
from services.usuario_service import UsuarioService

def test_criar_usuario_no_banco():
    service = UsuarioService()
    id_novo = service.cadastrar_usuario("Teste", "teste@exemplo.com", "(11) 99999-9999")

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT nome, email, telefone FROM usuarios WHERE id = %s", (id_novo,))
    linha = cursor.fetchone()
    cursor.close()
    conexao.close()

    assert linha == ("Teste", "teste@exemplo.com", "(11) 99999-9999")


def test_atualizar_usuario_no_banco():
    service = UsuarioService()
    id_novo = service.cadastrar_usuario("Teste", "teste@exemplo.com", "(11) 99999-9999")

    service.atualizar_usuario(id_novo, "nome", "Teste Novo")
    service.atualizar_usuario(id_novo, "email", "testenovo@exemplo.com")
    service.atualizar_usuario(id_novo, "telefone", "(11) 88888-8888")

    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT id, nome, email, telefone FROM usuarios WHERE id = %s", (id_novo,))
    linha = cur.fetchone()
    cur.close()
    con.close()

    assert linha == (id_novo, "Teste Novo", "testenovo@exemplo.com", "(11) 88888-8888")


def test_deletar_usuario_no_banco():
    service = UsuarioService()
    id_novo = service.cadastrar_usuario("Teste", "teste@exemplo.com", "(11) 99999-9999")

    service.deletar_usuario(id_novo)
    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT id FROM usuarios WHERE id = %s", (id_novo,))
    linha = cur.fetchone()
    cur.close()
    con.close()

    assert linha == None


def test_consultar_usuario_no_banco():
    service = UsuarioService()
    id_novo = service.cadastrar_usuario("Teste", "teste@exemplo.com", "(11) 99999-9999")

    linha = service.consutar_usuario(id_novo)[0]

    assert linha == (id_novo, "Teste", "teste@exemplo.com", "(11) 99999-9999")