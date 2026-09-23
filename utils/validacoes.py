def validar_preco(preco):
   if not isinstance(preco, (int, float)):
       raise TypeError("Preço deve ser um número.")
   if preco < 0:
       raise ValueError("Preço não pode ser negativo.")
   return preco


def validar_quantidade(qtd):
   if not isinstance(qtd, int):
       raise TypeError("Quantidade deve ser um número inteiro")
   if qtd < 0:
       raise ValueError("Quantidade não pode ser negativo.")
   return qtd


def validar_email(email: str):
    if not isinstance(email, str) or "@" not in email or "." not in email:
        raise TypeError("Email inválido")
    return email


def validar_nome(nome):
    if not isinstance(nome, str) or not nome.strip():
        raise TypeError("Nome não pode ser vazio")
    if len(nome) > 25:
        raise ValueError("Nome muito longo (máximo 25 caracteres).")
    return nome


def validar_id(id):
    if not isinstance(id, int):
        raise TypeError("Id deve ser um número inteiro")
    if id < 0:
        raise ValueError("O id não pode ser um número negativo")
    return id


def validar_telefone(telefone):
    numeros = "".join(c for c in telefone if c.isdigit())
    if len(numeros) not in (10, 11):
        raise ValueError("Telefone inválido")
    return telefone