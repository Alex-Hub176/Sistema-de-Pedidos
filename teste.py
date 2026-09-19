from repository.produtos_repository import ProdutoRepository
from models.produtos import Produtos

repo = ProdutoRepository()
pro1 = Produtos("Calça Jeans", 79, 100)
ult = repo.consultar(3)
print(ult)