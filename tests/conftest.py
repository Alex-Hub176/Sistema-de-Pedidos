import os
import pytest
from dotenv import load_dotenv

load_dotenv(".env.test", override=True)

from database.conexao import conectar

@pytest.fixture(autouse=True)
def limpar_banco():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "TRUNCATE TABLE pedido_itens, pedidos, produtos, usuarios "
        "RESTART IDENTITY CASCADE" 
    )
    conexao.commit()
    cursor.close()
    conexao.close()
    yield




