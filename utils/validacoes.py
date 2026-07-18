def ler_preco():
    while True:
        try:
            preco = float(input("Preço: "))

            if preco < 0:
                print("O preço não pode ser negativo.")
                continue

            return preco
        
        except ValueError:
            print("Digite um número válido.")



def ler_quantidade():
    while True:
        try:
            quantidade = int(input("Quantidade: "))

            if quantidade < 0:
                print("Digite um número válido.")
                continue

            return quantidade
        
        except ValueError:
            print("Digite um número válido.")



def ler_email():
    while True:
        email = str(input("Email: ")).strip()

        if "@" in email and "." in email:
            return email
        
        print("Email inválido")
