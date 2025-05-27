from .produto import produto

while True:

    tipo = input(f"Qual o tipo de produto: alimenticio ou eletronico!", ['1','2'])
    if tipo == '1':
        print("alimenticio")
    elif produto == '2':
        print("eletronico")
    else:
        print("Tipo de produto inválido.")

    preco = float(input("Qual o preço do produto em BRL: "))
    if preco == self.__get_preco():
           print({preco})

           break

    #Método utilizado para trata erros e excessões
    try: #O que tiver dentro de try deve funcionar
        produto = produto(tipo, preco)
        print(f"Prdouto criado com sucesso: {produto.tipo}, {produto.preco} BRL")
        break 

    except:#O que tiver dentro de except deve trata o erro.
          print("Erro: Vlaor invalido, tente novamente.")
    continue
    
