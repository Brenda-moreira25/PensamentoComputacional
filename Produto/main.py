from models.produto import Produto


lista = []  
while True:

    tipo = input(f"Qual o tipo de produto: alimenticio ou eletronico!", ['1','2'])
    if tipo == '1':
        print("alimenticio")
        nome = input("Qual o nome do alimento: ")
        quantidade = int(input("Qual a quantidade do alimento: "))

    elif tipo == '2':
        print("eletronico")
    else:
        print("Tipo de produto inválido.")

    preco = float(input("Qual o preço do produto em BRL: "))
    if preco == produto.get_preco():
           print({produto.get_preco()})

           break

    #Método utilizado para trata erros e excessões
    try: #O que tiver dentro de try deve funcionar
        produto = Produto(tipo, preco)
        print(f"Prdouto criado com sucesso: {produto.tipo}, {produto.preco} BRL")
        break 

    except:#O que tiver dentro de except deve trata o erro.
          print("Erro: Vlaor invalido, tente novamente.")
    continue
    
