import pytest
from utils.validacoes import *

@pytest.mark.parametrize("funcao, entrada, resul_esperado", [
    (validar_preco, 0, 0),
    (validar_preco, 25.50, 25.50),
    (validar_quantidade, 0, 0),
    (validar_quantidade, 1, 1),
    (validar_quantidade_item, 1, 1),
    (validar_email, "teste@exemplo.com", "teste@exemplo.com"),
    (validar_nome, "A" * 25, "A" * 25),
    (validar_id, 1, 1),
    (validar_status, "pendente", "pendente"),
    (validar_telefone, "(11) 99999-9999", "(11) 99999-9999"),
    (validar_telefone, 11999999999, "11999999999")
])
def test_deve_validar_valor_correto(funcao, entrada, resul_esperado):
    resultado = funcao(entrada)
    assert resultado == resul_esperado
    assert type(resultado) is type(resul_esperado)


@pytest.mark.parametrize("funcao, entrada, erro", [
    (validar_preco, "10", TypeError),
    (validar_preco, -1 , ValueError),
    (validar_quantidade, "10", TypeError),
    (validar_quantidade, -1, ValueError),
    (validar_email, "sem-arroba", TypeError),
    (validar_email, 123, TypeError),
    (validar_nome, "   ", TypeError),
    (validar_nome, "A" * 26, ValueError),
    (validar_id, "10", TypeError),
    (validar_id, 0, ValueError),
    (validar_status, "status-invalido", ValueError),
    (validar_telefone, "123", ValueError)  
])
def test_deve_rejeitar_entrada_invalida(funcao, entrada, erro):
     with pytest.raises(erro):
        funcao(entrada)