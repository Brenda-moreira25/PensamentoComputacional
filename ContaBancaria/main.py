from models.ContaBancaria import ContaBancaria

banco = []

banco.append(ContaBancaria( "Lauren", 100, 200, []))
banco.append(ContaBancaria( "Lucas", 100, 200, []))

while True:

    n = input("Deseja realizar uma operção: [s,n] ")
   
    if n == "s" :
        print("Digite a operação desejada sendo que :", "Sacar: 0 ", 
                              "depositar: 1", 
                              "trasnferir: 2")
        resposta1 = (input())
        
        if resposta1 == "0":
            titular = input("Digite o titular que deseja sacar: ")
            valor = float(input("Quanto deseja sacar: "))
            for conta in banco:
                if conta.titular == titular:
                    conta.sacar(valor)

        elif resposta1 == "1":
                titular = input("Digite o titular que deseja depositar: ")
                valor = float(input("Quanto deseja depositar: "))
                for conta in banco:
                    if conta.titular == titular:
                        conta.depositar()
            
        elif resposta1 == "2":
            titular = input("Digite o titular que deseja trasnferir: ")
            valor = float(input("Quanto deseja trsnferir: "))
            for conta in banco:
                    if conta.titular == titular:
                        conta.transferencia()
        
    elif n == "n":
        print("Operação não realizada/selecionada")
        break